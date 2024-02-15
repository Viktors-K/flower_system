from cryptography.fernet import Fernet
import csv
import base64

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
    encrypted = cipher.encrypt(data.encode())
    return base64.b64encode(encrypted)

# Function to decrypt data
def decrypt_data(encrypted_data,cipher):
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data))
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
        safe_pass = encrypt_data(password,main_cipher)
        line = [username,safe_pass]
        add_line_to_csv(csv_name, line)
    elif mode == 'l':
        username = input("Username:")
        password = input("Password:")
        stored_lines = read_lines_from_csv(csv_name)
        for stored_line in stored_lines:
            stored_username, stored_encrypted_password = stored_line
            if stored_username == username:
                stored_password = decrypt_data(stored_encrypted_password, main_cipher)
                if stored_password == password:
                    print("Correct login.")
                    break
        else:
            print("Incorrect login.")
    # Decrypting data
