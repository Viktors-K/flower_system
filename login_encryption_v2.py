from cryptography.fernet import Fernet
import csv

def add_line_to_csv(file_path, line):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(line)
    
def read_lines_from_csv(file_path):
    lines = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(row)
    return lines

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
    mode = (input("register or login? r/l"))
    if mode == 'r':
        username = input("Username:")
        password = input("Password:")
        encrypt_data()
    elif mode == 'l':
        username = input("Username:")
        password = input("Password:")
    # Decrypting data
    decrypted_data = decrypt_data(read_lines_from_csv("login.csv"))
    print("Decrypted:", decrypted_data)