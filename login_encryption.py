from cryptography.fernet import Fernet

# Set the key to a specific value
key = b'sw1pm3p6Ss-cOJv04L5hhbwoVmP9USS9A8lDP7oKcs0='
print(f"Key: {key}")  # Print the key
cipher_suite = Fernet(key)

# Function to encrypt data
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

# Function to decrypt data
def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()

# Example usage
if __name__ == "__main__":
    # Encrypting data
    plaintext = "Sensitive login information"
    encrypted_data = encrypt_data(plaintext)
    print("Encrypted:", encrypted_data)

    # Decrypting data
    decrypted_data = decrypt_data(encrypted_data)
    print("Decrypted:", decrypted_data)