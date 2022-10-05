def load_data():
    """ 
    takes a .txt file and makes it a list each element in list is one line

    returns:
    list of user information
    """

    data = open("data.txt", "r")
    lines = data.readlines()

    new_lines = []
    data_list = []

    #removes new line character from data
    for line in lines:
        new_lines.append(line.rstrip("\n"))

    

    for line in new_lines:
        data_list.append(line.split(","))
    
    return data_list

def make_data(lines):
    """
    makes a dict of username and passwords

    Args: lines is the raw list from load_data()

    returns: dict of logins with username as a key and password as data
    """
    logins = {}
    for line in lines:
        logins[line[0]] = line[1]

    return logins

def get_user_info(username):
    """
    gets the user info corresponding to their username

    Args: username (string), data(list)

    returns: the users info if the username exists, None if username does not exist
    """

    for line in range(len(data)):
        if username == data[line][0]:
            return [data[line][2:], line]
    return None

def print_user_info(user):

    user_info = get_user_info(username)[0]
    print(f"Name: {user_info[0]}")
    print(f"Balance: {user_info[1]}")

def login(username, password):
    """
    logs in user and displays account info

    Args: data(list), logins(dict), username(string), password(string)
    
    """
    if username in logins.keys():
        if password == logins[username]:
            print_user_info(username)
            return True
            
    print("Username and/or Password are incorrect")
    return False

def update_balance(user, new_balance):
    user_info = get_user_info(user)

    data[user_info[1]][3] = new_balance

def add_interest(rate):
    """
    adds set interest rate to all account balances

    Args: rate(float) 
    """
    for user_info in data:
        balance = float(user_info[3])
        balance *= 1 + rate

        user_info[3] = balance

def transfer(username, password, amount, toUser):
    if amount.isnumeric():
        amount = float(amount)
        if login(username, password):
            fromU = get_user_info(username)[0]
            if fromU[1] > amount and toUser in logins:
                toU = get_user_info(toUser)[0]

                fromU[1] = float(fromU[1]) - amount
                toU[1] = float(toU[1]) + amount

                update_balance(username, fromU[1])
                update_balance(toUser, toU[1])

                print("transfer succesful")
                print(fromU)
                print(toU)

                return True
            else:
                print("user does not exist or your balance is to low")
    else:
        print("please enter a numeric value")
        
    print("transfer not succesful")
    return False    

def deposit(username, password, amount):
    if amount.isnumeric:
        amount = float(amount)
        if login(username, password):
            balance = float(get_user_info(username)[0][1])
            balance += amount



            print(f"new balance: {balance}")
            update_balance(username, balance)
            print("success")
            return True
    else:
        print("amount not numeric")
    print("not a success")

def withdrawl(username, password, amount):
    if amount.isnumeric:
        amount = float(amount)
        if login(username, password):
            balance = float(get_user_info(username)[0][1])
            balance -= amount

            print(f"new balance: {balance}")
            update_balance(username, balance)
            print("success")
            return True
    else:
        print("amount not numeric")
    print("not a success")

data = load_data()
logins = make_data(data)

username = "aman"
password = "1234"

add_interest(0.005)

deposit(username, password, "50")
withdrawl(username, password, "55")