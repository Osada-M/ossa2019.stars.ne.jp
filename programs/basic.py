import hashlib
import base64

password = input("password > ").encode("utf-8")

code = base64.b64encode(hashlib.sha1((password)).digest())

print(f"\n{code.decode('utf-8')}\n")
