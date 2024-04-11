from cryptography.fernet import Fernet
import csv

csv_name = "C:\\Users\\vvkocetoks\\OneDrive - Rīgas domes izglītības iestādes\\Desktop\\flower_system\\other\\login_test.csv"

# we will be encrypting the below string.
user = input("Username: ")
input = input("Username: ")

key = b'teu3ODx9Du5B9XrPTC5PX0Tnco9-TSGHBChcKHhjFy8='
fernet = Fernet(key)

def encrypt(message):
    return fernet.encrypt(message.encode())

def decrypt(message):
    return fernet.decrypt(message).decode()

def add_line_to_csv(file_path, data):
    with open(file_path, 'a',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


def read_lines_from_csv(file_path):
    lines = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            lines.append(row)
    return lines

def read_users(file_name):
    data = read_lines_from_csv(file_name)
    users = []
    for i in range(0, len(data)):
        temp = data[i]
        user = {}
        user.update({'name': temp[0], 'password': temp[1]})
        users.append(user)
    return users