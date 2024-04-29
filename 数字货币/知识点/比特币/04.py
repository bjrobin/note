import bitcoinlib

# 创建一个比特币交易
tx = bitcoinlib.transactions.Transaction()

# 添加输入
tx.add_input("outpoint_txid", output_index)

# 添加输出
tx.add_output("recipient_address", amount)
tx.locktime = 0

# 对交易进行签名
private_key = bitcoinlib.keys.Key("private_key")
tx.sign(private_key)

# 尝试发送交易
try:
    tx.send()
except Exception as e:
    print("交易发送失败：%s" % e)