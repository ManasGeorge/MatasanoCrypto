from base64 import b64decode
from Crypto.Cipher import AES

f = open("7.txt",'r')
ciphertext = f.read()
ciphertext = b64decode(ciphertext)
key = "YELLOW SUBMARINE"
cipher = AES.new(key)

plaintext = ""
blocks = [ciphertext[x:x+16] for x in range(0,len(ciphertext)-16,16)]
for block in blocks:
	plaintext += cipher.decrypt(block)

print plaintext