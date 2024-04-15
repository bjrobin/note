import asyncio
from bitcoinrpc import BitcoinRPC
rpc_client = BitcoinRPC.from_config("http://localhost:8333", ("a", "b"))
import json
import time
insert_query = 'INSERT INTO `address` (`height`,`address`,`p_address`) VALUES  '
sql_distinct_address = 'select distinct(address) from btc.address '
sql_height = 'select max(height) from btc.address '
from clickhouse_driver import Client
from clickhouse_driver import connect
block_count=0
set_sanctioned_addresses_XBT=None

first_height_stat = None ## 第一个制裁地址出现的高度
height_start = 220129

def get_sanctioned_address_CBT():
    global set_sanctioned_addresses_XBT
    sanctioned_addresses_XBT = []
    with open('/Users/lhqer/MY/2024/数字货币/OFAC/ofac-sanctioned-digital-currency-addresses/sanctioned_addresses_XBT.txt','r') as f:
        for line in f:
            sanctioned_addresses_XBT.append(line.strip('\n'))
    set_sanctioned_addresses_XBT = set(sanctioned_addresses_XBT)
    print("set_sanctioned_addresses_XBT:",len(set_sanctioned_addresses_XBT))
def get_conn(database):
    host='127.0.0.1' #服务器地址
    port =29000 #端口
    user='default' #用户名
    password='' #密码
    database=database #数据库
    send_receive_timeout = 5 #超时时间
    conn = Client(host=host, port=port, user=user, password=password,database=database, send_receive_timeout=send_receive_timeout)
    return conn
def get_conn_2(database):
    host='127.0.0.1' #服务器地址
    port =29000 #端口
    user='default' #用户名
    password='' #密码
    database=database #数据库
    send_receive_timeout = 5 #超时时间
    conn = connect('clickhouse://{user}:{password}@{host}:{port}/{database}'.format(user=user, password=password, host=host, port=port, database=database))
def write_json(data, filename='data.json'):
    logfile1=open(filename,mode='w')
    logfile1.write(data) #\n 换行符
    logfile1.flush()
    logfile1.close()
def process_vout(height,tx,csv_data):
    vout = tx['vout'] 
    for vout_index,vout_item in enumerate(vout):
        if 'scriptPubKey' in vout_item:
            if 'address' in vout_item['scriptPubKey']:
                vout_address = vout_item['scriptPubKey']['address']
                # print(vout_address)
                csv_data.append([height,tx['txid'] ,-1,vout_index,vout_address])
def process_vin(height,tx,csv_data):
    vin = tx['vin'] 
    for vin_index,vin_item in enumerate(vin):
        if 'prevout'  in vin_item:
            if 'scriptPubKey' in vin_item['prevout']:
                if 'address' in vin_item['prevout']['scriptPubKey']:
                    vin_address = vin_item['prevout']['scriptPubKey']['address']
                    # print(vin_address)
                    csv_data.append([height,tx['txid'] ,vin_index,-1,vin_address])

def process_vin_vout(height,tx,csv_data):
    global first_height_stat
    vin = tx['vin'] 
    for vin_index,vin_item in enumerate(vin):
        if 'prevout'  in vin_item:
            if 'scriptPubKey' in vin_item['prevout']:
                if 'address' in vin_item['prevout']['scriptPubKey']:
                    vin_address = vin_item['prevout']['scriptPubKey']['address']
                    # print(vin_address)
                    if vin_address in set_sanctioned_addresses_XBT:
                        if first_height_stat is None:
                            first_height_stat = height
                        vout = tx['vout'] 
                        for vout_index,vout_item in enumerate(vout):
                            if 'scriptPubKey' in vout_item:
                                if 'address' in vout_item['scriptPubKey']:
                                    vout_address = vout_item['scriptPubKey']['address']
                                    # print(len(set_sanctioned_addresses_XBT),vout_address)
                                    set_sanctioned_addresses_XBT.add(vout_address) # 内存中记住制裁地址
                                    csv_data.append([height,vin_address,vout_address]) # 几下当前块所有添加的地址
                        
                        # print("制裁列表长度：",len(set_sanctioned_addresses_XBT))
def execute_query(csv_data):
    conn = get_conn("btc")
    conn.execute('INSERT INTO `address` (`height`,`address`,`p_address`) VALUES', csv_data)
    conn.disconnect()
def query_distinct_address():
    conn = get_conn("btc")
    results = conn.execute(sql_distinct_address)
    for row in results:
        set_sanctioned_addresses_XBT.add(row[0])
    print("set_sanctioned_addresses_XBT:",len(set_sanctioned_addresses_XBT))
    # 关闭连接
    conn.disconnect()
def query_for_last_height():
    global height_start
    conn = get_conn("btc")
    results = conn.execute(sql_height)
    print("query_for_last_height results:",results)
    if results[0][0] is None:
        return
    if results[0][0] > 0:
        height_start = int(results[0][0])
    print("height_start:",height_start)
    conn.disconnect()

async def process_block(height):
    
    blockhash = await rpc_client.getblockhash(height)
    block = await rpc_client.getblock(blockhash,3)
    print("一共：",block_count,"\t当前：",height,"\t进度",height/block_count*100,"%","\t制裁列表长度：",len(set_sanctioned_addresses_XBT),"\t第一个制裁地址出现的高度：",first_height_stat)
    tx_list = block['tx']
    csv_data = []
    for tx in tx_list:
        # process_vin(height,tx,csv_data)
        # process_vout(height,tx,csv_data)
        process_vin_vout(height,tx,csv_data)
    if len(csv_data) > 0:
        execute_query(csv_data)
        csv_data = []

async def getblock_count():
    global block_count
    block_count = await rpc_client.getblockcount() 
    print("Block Count:", block_count)
    # return block_count
async def main():
    global block_count
    block_count = await rpc_client.getblockcount() 
    start = time.time() 
    print("---------------------------------------------------------------")
    print("height_start:", height_start)
    for i in range(height_start,block_count):
        await(process_block(i))
    print("---------------------------------------------------------------")
    # await rpc_client.aclose()
    end = time.time() 
    run_time = end - start   # 程序的运行时间，单位为秒
    print("-耗时:", run_time/60, "min")
    
if __name__ == "__main__":
    get_sanctioned_address_CBT()
    query_distinct_address()
    query_for_last_height()
    asyncio.run(main())
    # a = input('请输入。。。')
    # print (a)
