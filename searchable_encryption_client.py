import json
from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Step 1
kf = input("Enter the name of keyword file :")
f = open(kf,"r")

tf = "trapdoor_"+kf
f1 = open(tf,"a+")

for keyword in f.readlines() :
	data = keyword.encode('utf-8')

	key = pad(b'secret', 16)

	cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
	ct_bytes = cipher.encrypt(pad(data, AES.block_size))
	L = ct_bytes[:8]
	hash_object1 = SHA256.new(L+b'secret')
	hashkey = hash_object1.digest()
#	print()
#	iv = b64encode(cipher.iv).decode('utf-8')

	prs = get_random_bytes(8)

	hash_object = SHA256.new(prs+hashkey)
	hash = hash_object.digest()

	t = prs + hash[:8]

	c = bytearray(len(ct_bytes))
	for i in range(len(ct_bytes)):
		c[i] = ct_bytes[i] ^ t[i]
#	print(c)	
	trapdoor = b64encode(c).decode('utf-8')

	f1.write(trapdoor+"\n")

f.close()
f1.close()
