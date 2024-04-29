# 使用 Tron(TRX) 收款
# https://dmesg.app/tron-trx.html


# pip3 install tronpy
# A Quick Guide to Tron Network Interaction Using Python
# https://blog.arashtad.com/blog/a-quick-guide-to-tron-network-interaction-using-python/
from tronpy import Tron
import time
import json
# set timeout to 20s for a slow network
client = Tron(conf={'timeout': 20.0})  # The default provider, mainnet
# client = Tron(network="nile")
time.sleep(1)

# Getting Blockchain Info
def write_json(data, filename='get_transaction_info.json'):
    logfile1=open(filename,mode='w')
    logfile1.write(data)
    logfile1.flush()
    logfile1.close()

def main():
    write_json(json.dumps(client.get_transaction_info('661f1df88ce02b746efe7449c3c7a04d6d21a7fc019723c92679228d8275ad57')), 'get_transaction_info_661f1df88ce02b746efe7449c3c7a04d6d21a7fc019723c92679228d8275ad57.json')
if __name__ == '__main__':
    main()


