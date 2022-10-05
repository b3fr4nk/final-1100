def load_data():
    """ 
    takes a .txt file and makes it a list each element in list is one line

    returns:
    list of user information
    """

    data = open("data.txt", "r")
    lines = data.readlines()

    new_lines = []

    #removes new line character from data
    for line in lines:
        new_lines.append(line.rstrip("\n"))
    
    return new_lines


def make_data(lines):
    """
    makes a dict of username and passwords

    Args: lines is the raw list from load_data()

    returns: dict of logins with username as a key and password as data
    """
    logins = {}
    for line in lines:
        user_info = line.split(",")
        print(user_info)
        logins[user_info[0]] = user_info[1]

    return logins

def get_user_info(username, data):
    """
    gets the user info corresponding to their username

    Args: username (string), data(list)

    returns: the users info if the username exists, None if username does not exist
    """

    for line in data:
        user_info = line.split(",")
        if username == user_info[0]:
            return user_info[2:]
    return None

def login(data, logins, username, password):
    """
    logs in user and displays account info

    Args: data(list), logins(dict), username(string), password(string)
    
    """
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