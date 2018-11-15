import sys
from base64 import b64decode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

keyword = input("Enter a word :")
data = (keyword+"\n").encode('utf-8')

key = pad(b'secret', 16)

cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
L1 = ct_bytes[:8]
hash_object1 = SHA256.new(L1+b'secret')
hashkey = hash_object1.digest()


tf = input("Enter the name of a trapdoor file :")
f = open(tf,"r")

for t in f.readlines():
	tk = b64decode(t)
	c = bytearray(len(ct_bytes))
	for i in range(len(ct_bytes)):
		c[i] = ct_bytes[i] ^ tk[i]
	L = c[:8]
	R = c[8:]

	hash_object = SHA256.new(L+hashkey)
	hash = hash_object.digest()
	if (hash[:8] == R) :
		print ("true")
		sys.exit()
print("false")
f.close()