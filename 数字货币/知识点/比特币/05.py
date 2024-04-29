import bitcoin
from bitcoinlib.transactions import *
from bitcoinlib.services.services import *
import requests

amount = 19605 # in satoshis
t = Transaction(fee=5000, outputs=[Output(amount, address="to address")])
transaction_inputs = [
    ("b0514d3d47bffdf588e14e0324c88e4934a36423f011d634b4e379b3a65c5207", 0, "wif private key"),
    ("4e831f9221470f93cc0cd2e0ef0e2f731c5bbfde0e8fc2ae430b31149ffd25bb", 0, "wif private key")
]
for ti in transaction_inputs:
    ki = Key(ti[2])
    t.add_input(prev_txid=ti[0], output_n=ti[1], keys=ki.public())
icount = 0
for ti in transaction_inputs:
    ki = Key(ti[2])
    t.sign(ki.private_byte, icount)
    icount += 1

print(t.verify())
rawhextx = t.raw_hex()
tx = Service().sendrawtransaction(rawhextx)
print(tx)


# https://github.com/petertodd/python-bitcoinlib