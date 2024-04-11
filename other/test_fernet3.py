from cryptography.fernet import Fernet

# we will be encrypting the below string.
input = "hello geeks"

key = b'teu3ODx9Du5B9XrPTC5PX0Tnco9-TSGHBChcKHhjFy8='
fernet = Fernet(key)

def encrypt(message):
    return fernet.encrypt(message.encode())

def decrypt(message):
    return fernet.decrypt(message).decode()

encrypted_input = encrypt(input)

print("original string: ", input)
print("encrypted string: ", encrypted_input)
print("decrypted string: ", decrypt(encrypted_input))
