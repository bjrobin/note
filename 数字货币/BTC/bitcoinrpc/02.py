import asyncio
from bitcoinrpc import BitcoinRPC
rpc_client = BitcoinRPC.from_config("http://localhost:8333", ("a", "b"))
import json
import time
# insert_query = 'INSERT IGNORE INTO `transaction` (`height`, `txid`, `vin_idx`, `vout_idx`, `address`) VALUES (%s,%s,%s,%s,%s)'
insert_query = 'INSERT INTO `transaction` (`height`, `txid`, `vin_idx`, `vout_idx`, `address`) VALUES (%s,%s,%s,%s,%s) '
import pymysql
block_count=0
sanctioned_addresses_XBT=[]
with open('/Users/lhqer/MY/2024/数字货币/OFAC/ofac-sanctioned-digital-currency-addresses/sanctioned_addresses_XBT.txt','r') as f:
    for line in f:
        sanctioned_addresses_XBT.append(line.strip('\n'))
set_sanctioned_addresses_XBT = set(sanctioned_addresses_XBT)
first_height_stat = None ## 第一个制裁地址出现的高度

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

def process_vin_vout(height,tx):
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
                                    print(len(set_sanctioned_addresses_XBT),vout_address)
                                    set_sanctioned_addresses_XBT.add(vout_address)
def execute_query(csv_data):
    conn = get_conn_mysql("BTC")
    cursor = conn.cursor()
    cursor.executemany(insert_query, csv_data)
    conn.commit()
    conn.close()
async def process_block(height):
    
    # start = time.time() 
    blockhash = await rpc_client.getblockhash(height)
    block = await rpc_client.getblock(blockhash,3)
    # write_json(json.dumps(block), filename='getblock_617119_3.json')
    # print("---------------------------------------------------------------")
    print("一共：",block_count,"\t当前：",height,"\进度",height/block_count*100,"%","\t制裁列表长度：",len(set_sanctioned_addresses_XBT))
    tx_list = block['tx']
    csv_data = []
    for tx in tx_list:
        # process_vin(height,tx,csv_data)
        # process_vout(height,tx,csv_data)
        process_vin_vout(height,tx)
    
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
def main():

    # global block_count
    # block_count =getblock_count()
    # block_count = await rpc_client.getblockcount() 
    # print("Block Count:", block_count)

    start = time.time() 
    print("---------------------------------------------------------------")


    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # loop = asyncio.get_event_loop()
    tasks2 = [ asyncio.ensure_future( getblock_count()), ]
    loop.run_until_complete(asyncio.wait(tasks2))

    tasks = []
    for j in range(0,block_count,100):
        for i in range(j,j+100):
            tasks.append( asyncio.ensure_future( process_block(i) ) )
        loop.run_until_complete(asyncio.wait(tasks))

    print("---------------------------------------------------------------")
    # 耗时: 0.20995036363601685 min
    # 全部区块将耗时: 3.1037224694266916 天
    # await process_block(617123)
    # for i in range(617123,617123+10):
    #     asyncio.run( process_block(i))
    print("---------------------------------------------------------------")
    # # step1 创建一个事件循环
    # loop = asyncio.get_event_loop()
    # # step2 将异步函数（协程）加入事件队列
    # tasks = [
    # asyncio.run(process_block(617123))
        # process_block(617123+1),
        # process_block(617123+2),
        # process_block(617123+3),
        # process_block(617123+4),
        # process_block(617123+5),
        # process_block(617123+6),
        # process_block(617123+7),
        # process_block(617123+8),
        # process_block(617123+9),

    # ]
    # # step3 执行事件队列 直到最晚的一个事件被处理完毕后结束
    # asyncio.wait(tasks)
    print("---------------------------------------------------------------")
    # await rpc_client.aclose()
    end = time.time() 
    run_time = end - start   # 程序的运行时间，单位为秒
    print("-耗时:", run_time/60, "min")
    print("-全部区块将耗时:", run_time*(830000-617123)/60/60/24/10, "天")
    print("",first_height_stat)
    
if __name__ == "__main__":

    main()
    # asyncio.run(process_block(617123))
    # asyncio.run(process_block(617124))
    a = input('请输入一个东西')
    print (a)

# 18.4: Accessing Bitcoind with Python
# https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/18_4_Accessing_Bitcoind_with_Python.md