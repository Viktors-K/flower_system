from cryptography.fernet import Fernet
 
# we will be encrypting the below string.
messages = ['abc','def','ghi','jkl']
 
# generate a key for encryption and decryption
# You can use fernet to generate 
# the key or use random key generator
# here I'm using fernet to generate key
 
key = b'teu3ODx9Du5B9XrPTC5PX0Tnco9-TSGHBChcKHhjFy8='
# Instance the Fernet class with the key
 
fernet = Fernet(key)
print(key)
# then use the Fernet class instance 
# to encrypt the string string must
# be encoded to byte string before encryption
encrypted_messages = []
for item in messages:
    encrypted_item = item.encode()
    encrypted_messages.append(encrypted_item)
    print("original string: ", item)
    print("encrypted string: ", encrypted_item)
 
# decrypt the encrypted string with the 
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
for item in encrypted_messages:
    unencrypted_item = fernet.decrypt(item).decode()
    encrypted_messages.append(unencrypted_item)
    print("decrypted string: ", unencrypted_item)
 
