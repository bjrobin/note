from bitcoin.rpc import RawProxy
# python-bitcoinlib

# Peter Todd提供的Python比特币库，共识库和节点

# pycoin

# Richard Kiss提供的Python比特币库

# pybitcointools

# Vitalik Buterin提供的Python比特币库
# pip install python-bitcoinlib
# https://github.com/tianmingyun/MasterBitcoin2CN/blob/master/ch03.md
# Create a connection to local Bitcoin Core node
p = RawProxy( service_url='http://a:b@127.0.0.1:8333/',  btc_conf_file="/Users/lhqer/MY/2024/data/Bitcoin/bitcoin.conf" )

# # Run the getblockchaininfo command, store the resulting data in info
# info = p.getblockchaininfo()

# # Retrieve the 'blocks' element from the info
# print(info)
# print(info['blocks'])


# Alice's transaction ID
txid = "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

# First, retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(txid)

# Decode the transaction hex into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx)

# Retrieve each of the outputs from the transaction
for output in decoded_tx['vout']:
    print(output)
    # print(output['scriptPubKey']['addresses'], output['value'])