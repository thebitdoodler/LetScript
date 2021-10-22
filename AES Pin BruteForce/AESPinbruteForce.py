import base64
from Crypto.Cipher import AES
from Crypto.Hash import MD5
import re

# Taking Encoded string from user
enc = "<AES Encoded String under double quotes>"

# Making custom regex to retrieve desired pattern
uuid = re.compile('<Custom Regex>')

# decoding base64 string
abyte = base64.b64decode(enc)

iv = abyte[0:16]

data = abyte[16:]


# Bruteforcing the PIN 
for x in range(0, 9999):
	pin = "%04d" % x
	h =  MD5.new()
	h.update(pin.encode())
	key = h.digest()[0:16]
	# Creating exceptions to escape any error
	try:
		cipher = AES.new(key, AES.MODE_CBC, iv)
		clear = cipher.decrypt(data)
		if uuid.match(str(clear)):
			print(clear)
	except Exception as err:
		pass
