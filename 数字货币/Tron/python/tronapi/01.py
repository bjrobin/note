from tronapi import Tron
from collections.abc import Mapping
full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io'
tron = Tron(full_node, solidity_node, event_server)
tron.default_block = 'latest'
print(tron.get_block())