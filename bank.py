def load_data():
    data = open("data.txt", "r")
    lines = data.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line.rstrip("\n"))
    
    return new_lines

def make_data(lines):
    logins = {}
    for line in lines:
        user_info = line.split(",")
        print(user_info)
        logins[user_info[0]] = user_info[1]

    return logins

def get_user_info(username, data):
    for line in data:
        user_info = line.split(",")
        if username == user_info[0]:
            return user_info[2:]
    return None

def login(data, logins, username, password):
    if username in logins.keys():
        if password == logins[username]:
            user_info = get_user_info(username, data)
            print(f"Name: {user_info[0]}")
            print(f"Balance: {user_info[1]}")
        else: 
            print("username or password is incorrect")
    else: 
            print("username or password is incorrect")
        

data = load_data()
logins = make_data(data)

username = input("Enter name: ")
password = input("Enter Password: ")

login(data, logins, username, password)