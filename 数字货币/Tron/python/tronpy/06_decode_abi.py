
from tronpy import Tron
from tronpy.abi import trx_abi
from tronpy.abi import tron_abi
import time
import json
client = Tron(conf={'timeout': 20.0})  # The default provider, mainnet


def main():
    time.sleep(1)
    print(tron_abi.decode_abi(['address', 'uint256'],bytes.fromhex('a9059cbb000000000000000000000041dc2c107c0f8633d8236daa46d0e640e2c375f6ac000000000000000000000000000000000000000000000000000000008e277354')))
    # print(tron_abi.decode_abi(['address', 'uint256'],bytes.fromhex('000000000000000000000041dc2c107c0f8633d8236daa46d0e640e2c375f6ac000000000000000000000000000000000000000000000000000000008e277354')))
    # print(trx_abi.decode_abi(['address', 'uint256'],bytes.fromhex('0000000000000000000000007564105e977516c53be337314c7e53838967bdac0000000000000000000000000000000000000000000000000000000005f5e100')))
if __name__ == '__main__':
    main()


