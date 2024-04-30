import hashlib
import codecs

publickey = codecs.decode('03c3ecb76ac26a69d80525245f3886b1a8b41a5c56038e96a7a003ddcfac524cbc', 'hex')
s = hashlib.new('sha256', publickey).digest()
r = hashlib.new('ripemd160', s).digest()

print(codecs.encode(s, 'hex').decode("utf-8"))
print(codecs.encode(r, 'hex').decode("utf-8"))

# 01634d164eb397dde916405580e0f6fe0f3dc0b647f7568d29d5f824e138bac2
# 907ee8b73f268afa5fccabeaaf17c3d49b3559a3