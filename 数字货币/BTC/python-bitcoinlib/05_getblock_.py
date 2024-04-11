from bitcoin.rpc import RawProxy
import sys
import time
proxy = RawProxy( service_url='http://a:b@127.0.0.1:8333/',  btc_conf_file="/Users/lhqer/MY/2024/data/Bitcoin/bitcoin.conf" )
max_block_count = proxy.getblockcount()
sanctioned_addresses_XBT=[]
with open('/Users/lhqer/MY/2024/数字货币/OFAC/ofac-sanctioned-digital-currency-addresses/sanctioned_addresses_XBT.txt','r') as f:
    for line in f:
        sanctioned_addresses_XBT.append(line.strip('\n'))
# print(sanctioned_addresses_XBT)
set_sanctioned_addresses_XBT = set(sanctioned_addresses_XBT)
insert_query = ''' INSERT IGNORE INTO `transaction` (`height`, `txid`, `vin_idx`, `vin_address`, `vout_address`) VALUES (%s,%s, %s,%s, %s) ''' # futures.transaction
import pymysql
def get_conn_mysql(database):
    return pymysql.connect( host='127.0.0.1',  port=3306, user='root', password='12345678', database=database, )
def process_vout(height,block):
    tx_list = block['tx']
    print(tx_list)
    csv_data = []
    # 遍历交易
    for txid in tx_list:
        # print(txid)
        raw_tx = proxy.getrawtransaction(txid)
        decoded_tx = proxy.decoderawtransaction(raw_tx)
    # #     # # 输出
        # for idx, output in enumerate(decoded_tx['vout']):
        #     if 'address' in output['scriptPubKey']:
        #         vout_address = output['scriptPubKey']['address']
        #         print([height,txid,idx,vout_address])
        #         csv_data.append([height,txid,idx,vin_address,vout_address])
        #         # 将本次交易的输出地址加入制裁地址集合
        #         set_sanctioned_addresses_XBT.add(output['scriptPubKey']['address'])
            # pass
        pass
def process_vin(height,block):
    tx_list = block['tx']
    csv_data = []
    # 遍历交易
    for txid in tx_list:
        raw_tx = proxy.getrawtransaction(txid)
        decoded_tx = proxy.decoderawtransaction(raw_tx)
        # 先遍历输入，得到每一个输入的地址
        # for input in decoded_tx['vin']:
        for idx, input in enumerate(decoded_tx['vin']):
            if 'txid' in input and 'vout' in input:
                vin_txid = input['txid']
                vin_vout = input['vout']
                decoded_tx_1 = proxy.decoderawtransaction(proxy.getrawtransaction(vin_txid))
                if 'address' in decoded_tx_1['vout'][vin_vout]['scriptPubKey']:
                    vin_address = decoded_tx_1['vout'][vin_vout]['scriptPubKey']['address']
                    # 如果某个输入的地址是制裁地址
                    if vin_address in set_sanctioned_addresses_XBT:
                        # 输出
                        for output in decoded_tx['vout']:
                            if 'address' in output['scriptPubKey']:
                                vout_address = output['scriptPubKey']['address']
                                # print([height,txid,idx,vin_address,vout_address])
                                csv_data.append([height,txid,idx,vin_address,vout_address])
                                # 将本次交易的输出地址加入制裁地址集合
                                set_sanctioned_addresses_XBT.add(output['scriptPubKey']['address'])
    print("添加",len(csv_data))
    conn = get_conn_mysql("BTC")
    cursor = conn.cursor()
    cursor.executemany(insert_query, csv_data)
    conn.commit()
    conn.close()

def process_block(height):

    start = time.time() 
    if height > max_block_count:
        print("Block height too high")
        return
    print("Block height: ",height)
    block = proxy.getblock(proxy.getblockhash(height))
    # process_vin(height,block)
    process_vout(height,block)
    # print(block)

    end = time.time() 
    run_time = end - start   # 程序的运行时间，单位为秒
    print("耗时:", run_time/60, "min")
    print("全部区块将耗时:", run_time*830000/60/60/24, "天")
def main():
    process_block(617123)
    # for blockheight in range(617123,max_block_count):
    #     process_block(blockheight)
    pass

if __name__ == '__main__':
    main()
    print("最大区块：",max_block_count)

# CREATE TABLE `transaction` (
#   `id` int NOT NULL AUTO_INCREMENT,
#   `height` int DEFAULT NULL,
#   `txid` char(64) DEFAULT NULL,
#   `vin_idx` int DEFAULT NULL,
#   `vin_address` char(76) DEFAULT NULL,
#   `vout_address` char(76) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=24659 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;