import asyncio
from bitcoinrpc import BitcoinRPC
rpc_client = BitcoinRPC.from_config("http://localhost:8333", ("a", "b"))
import json
import time
def write_json(data, filename='data.json'):
    logfile1=open(filename,mode='w')
    logfile1.write(data) #\n 换行符
    logfile1.flush()
    logfile1.close()
def process_vout(tx):
    vout = tx['vout'] 
    for vout_item in vout:
        if 'scriptPubKey' in vout_item:
            if 'address' in vout_item['scriptPubKey']:
                print(vout_item['scriptPubKey']['address'])
def process_vin(tx):
    vin = tx['vin'] 
    for vin_item in vin:
        if 'prevout'  in vin_item:
            if 'scriptPubKey' in vin_item['prevout']:
                if 'address' in vin_item['prevout']['scriptPubKey']:
                    print(vin_item['prevout']['scriptPubKey']['address'])
async def process_block(height):
    start = time.time() 
    blockhash = await rpc_client.getblockhash(height)
    block = await rpc_client.getblock(blockhash,3)
    # write_json(json.dumps(block), filename='getblock_617119_3.json')
    print("---------------------------------------------------------------")
    tx_list = block['tx']
    csv_data = []
    for tx in tx_list:
        process_vin(tx)
        process_vout(tx)
    end = time.time() 
    run_time = end - start   # 程序的运行时间，单位为秒
    print("耗时:", run_time/60, "min")
    print("全部区块将耗时:", run_time*830000/60/60/24, "天")
async def main():
    block_count = await rpc_client.getblockcount() 
    print("---------------------------------------------------------------")
    print("Block Count:", block_count)
    print("---------------------------------------------------------------\n")
    await process_block(617119)
    await rpc_client.aclose()
    
if __name__ == "__main__":
    asyncio.run(main())

# 18.4: Accessing Bitcoind with Python
# https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line/blob/master/18_4_Accessing_Bitcoind_with_Python.md