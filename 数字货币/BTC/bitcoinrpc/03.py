import asyncio
from bitcoinrpc import BitcoinRPC
rpc_client = BitcoinRPC.from_config("http://localhost:8333", ("a", "b"))
import json
import time
# insert_query = 'INSERT IGNORE INTO `transaction` (`height`, `txid`, `vin_idx`, `vout_idx`, `address`) VALUES (%s,%s,%s,%s,%s)'
# insert_query = 'INSERT INTO `transaction` (`height`, `txid`, `vin_idx`, `vout_idx`, `address`) VALUES (%s,%s,%s,%s,%s) '
insert_query = 'INSERT INTO `address` (`height`,`address`,`p_address`) VALUES (%s,%s,%s) '
sql_first = 'select distinct(address) from btc.address '
sql_height = 'select max(height) from btc.address '
import pymysql
block_count=0
sanctioned_addresses_XBT=[]
with open('/Users/lhqer/MY/2024/数字货币/OFAC/ofac-sanctioned-digital-currency-addresses/sanctioned_addresses_XBT.txt','r') as f:
    for line in f:
        sanctioned_addresses_XBT.append(line.strip('\n'))
set_sanctioned_addresses_XBT = set(sanctioned_addresses_XBT)
first_height_stat = None ## 第一个制裁地址出现的高度
height_start = 220129

def get_conn_mysql(database):
    return pymysql.connect( host='127.0.0.1',  port=3306, user='root', password='12345678', database=database, )
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
    conn = get_conn_mysql("BTC")
    cursor = conn.cursor()
    cursor.executemany(insert_query, csv_data)
    conn.commit()
    conn.close()
def query_first():
    conn = get_conn_mysql("BTC")
    cursor = conn.cursor()
    cursor.execute(sql_first)
    results = cursor.fetchall()
    print("sanctioned_addresses_XBT:",len(sanctioned_addresses_XBT))
    for row in results:
        sanctioned_addresses_XBT.append(row[0])
    print("sanctioned_addresses_XBT:",len(sanctioned_addresses_XBT))
    conn.close()
def query_for_last_height():
    global height_start
    conn = get_conn_mysql("BTC")
    cursor = conn.cursor()
    cursor.execute(sql_height)
    results = cursor.fetchall()
    print("results:",results)
    if results[0][0] is None:
        return
    height_start = int(results[0][0])
    print("height_start:",height_start)
    conn.close()

async def process_block(height):
    
    # start = time.time() 
    blockhash = await rpc_client.getblockhash(height)
    block = await rpc_client.getblock(blockhash,3)
    # write_json(json.dumps(block), filename='getblock_617119_3.json')
    # print("---------------------------------------------------------------")
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
            
    
    # execute_query(csv_data)

    # end = time.time() 
    # run_time = end - start   # 程序的运行时间，单位为秒
    # print("耗时:", run_time/60, "min")
    # print("全部区块将耗时:", run_time*(830000-617123)/60/60/24, "天")

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
    # 一共： 838986   当前： 220129   进度 25.397324865969157 %       制裁列表长度： 386      第一个制裁地址出现的高度： 220129
    for i in range(height_start,block_count):
        await(process_block(i))
    print("---------------------------------------------------------------")
    # await rpc_client.aclose()
    end = time.time() 
    run_time = end - start   # 程序的运行时间，单位为秒
    print("-耗时:", run_time/60, "min")
    
if __name__ == "__main__":
    query_first()
    query_for_last_height()
    asyncio.run(main())
    # a = input('请输入。。。')
    # print (a)

# 18.4: Accessing Bitcoind with Python
# https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/18_4_Accessing_Bitcoind_with_Python.md