
from cryptography.fernet import Fernet

key=Fernet.generate_key()
print(key)
msg="heloo"
encodemsg=msg.encode()
print(encodemsg)
encr=Fernet(key).encrypt(encodemsg)
print(encr)
decr=Fernet(key).decrypt(encr)
decodedecry=decr.decode()
print(decodedecry)