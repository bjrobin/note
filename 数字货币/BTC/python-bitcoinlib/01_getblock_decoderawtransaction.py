from bitcoin.rpc import RawProxy
import sys
proxy = RawProxy( service_url='http://a:b@127.0.0.1:8333/',  btc_conf_file="/Users/lhqer/MY/2024/data/Bitcoin/bitcoin.conf" )
block_count = proxy.getblockcount()
print(block_count)
all_addresses = set()

# 处理一个block
def process_block(blockheight,set_sanctioned_addresses_XBT,logfile):
    if blockheight > block_count:
        print("Block height too high")
        return
    print("Block height: ",blockheight)
    block = proxy.getblock(proxy.getblockhash(blockheight))
    tx_list = block['tx']
    # 遍历交易
    for tx_id in tx_list:
        # print(tx_id)
        raw_tx = proxy.getrawtransaction(tx_id)
        decoded_tx = proxy.decoderawtransaction(raw_tx)
        # 遍历vin
        for input in decoded_tx['vin']:
            if 'txid' in input and 'vout' in input:
                # print(input)
                txid = input['txid']
                vout = input['vout']
                # 得到某个输入的详情
                decoded_tx_1 = proxy.decoderawtransaction(proxy.getrawtransaction(txid))
                # print(decoded_tx_1['vout'][vout])
                if 'address' in decoded_tx_1['vout'][vout]['scriptPubKey']:
                    address = decoded_tx_1['vout'][vout]['scriptPubKey']['address']
                    # 如果某个输入的地址是制裁地址
                    if address in set_sanctioned_addresses_XBT:
                        # print(address)
                        # 遍历输出本次交易的输出
                        for output in decoded_tx['vout']:
                            if 'address' in output['scriptPubKey']:
                                # if output['scriptPubKey']['address'] in set_sanctioned_addresses_XBT:
                                    s = "("+address+") --> ("+output['scriptPubKey']['address']+")"
                                    # s = "("+address+") --> ("+output['scriptPubKey']['address']+") : "+tx_id
                                    print(s+" : "+tx_id)
                                    # 将本次交易的输出地址加入制裁地址集合
                                    set_sanctioned_addresses_XBT.add(output['scriptPubKey']['address'])
                                    logfile.write(s+'\n') #\n 换行符
                                    logfile.flush()

        # print(tx)
def main(sanctioned_addresses_XBT,logfile):

    # print(proxy.getblockcount())
    # return
    # blockheight=835318
    for blockheight in range(617123,block_count):
        process_block(blockheight,sanctioned_addresses_XBT,logfile)
    # blockheight=838402


if __name__ == '__main__':
    
    sanctioned_addresses_XBT=[]
    with open('/Users/lhqer/MY/2024/数字货币/OFAC/ofac-sanctioned-digital-currency-addresses/sanctioned_addresses_XBT.txt','r') as f:
        for line in f:
            sanctioned_addresses_XBT.append(line.strip('\n'))
    # print(sanctioned_addresses_XBT)
    set_sanctioned_addresses_XBT = set(sanctioned_addresses_XBT)
    logfile=open('log.puml',mode='w')
    main(set_sanctioned_addresses_XBT,logfile)