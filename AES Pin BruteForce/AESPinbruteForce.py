import base64
from Crypto.Cipher import AES
from Crypto.Hash import MD5
import re
enc = "<AES Encoded String under double quotes>"

uuid = re.compile('<Custom Regex>')

abyte = base64.b64decode(enc)

iv = abyte[0:16]

data = abyte[16:]

for x in range(0, 9999):
	pin = "%04d" % x
	h =  MD5.new()
	h.update(pin.encode())
	key = h.digest()[0:16]
	try:
		cipher = AES.new(key, AES.MODE_CBC, iv)
		clear = cipher.decrypt(data)
		if uuid.match(str(clear)):
			print(clear)
	except Exception as err:
		pass
