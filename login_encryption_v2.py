from cryptography.fernet import Fernet
import csv

def add_line_to_csv(file_path, data):
    try:
        with open(file_path, 'a',) as csvfile:
            writer = csv.writer(csvfile)
            print(f'Data: {data}')
            writer.writerow(data)
    except IOError as e:
        print(f"Error writing to CSV file: {e}")
        raise e
    
def read_lines_from_csv(file_path):
    lines = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(row)
    return lines

# Function to encrypt data
def encrypt_data(data,cipher):
    return cipher.encrypt(data.encode())

# Function to decrypt data
def decrypt_data(encrypted_data,cipher):
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()

# Example usage
if __name__ == "__main__":
    csv_name = "C:\\Users\\vvkocetoks\\OneDrive - Rīgas domes izglītības iestādes\\Desktop\\flower_system\\login.csv"
    # Set the key to a specific value
    key = b'sw1pm3p6Ss-cOJv04L5hhbwoVmP9USS9A8lDP7oKcs0='
    print(f"Key: {key}")  # Print the key
    main_cipher = Fernet(key)
    # Encrypting data
    mode = (input("register or login? r/l"))
    if mode == 'r':
        username = input("Username:")
        password = input("Password:")
        safe_pass = str(encrypt_data(password,main_cipher))
        line = [username,safe_pass[2:-1]]
        
        add_line_to_csv(csv_name, line)
        print(line)
    elif mode == 'l':
        username = input("Username:")
        password = input("Password:")
        safe_pass = str(encrypt_data(password,main_cipher))
        line = f"{username}:{safe_pass[2:-1]}"
        if line in read_lines_from_csv(csv_name):
            print("Correct login.")
        else:
            print("Incorrect login.")
    # Decrypting data
