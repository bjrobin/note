address = '1ALis8zeW1XduXf98ZjoL4EKLen5mVA1q4'
private = '5KiUZd5as1TKsiwnt1KiPgiECtXiuF9BS1MxrAgedNrXcScm4d5'

from some_btc_library import make_transaction

tx_hex = make_transaction(
    inputs=[[address, private]],
    to='123rn4tNGhf1ZehQHLohYn8WRQYhjeGSCw',
    amount=3,
    miner_fee=0.0001
)

send_to_exteral_service(tx_hex)
print "transaction complete"