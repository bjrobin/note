
from tronpy import Tron
import time
import json
client = Tron(conf={'timeout': 20.0})  # The default provider, mainnet


def main():
    time.sleep(1)
    print(json.dumps(client.get_latest_block_id()))
if __name__ == '__main__':
    main()


