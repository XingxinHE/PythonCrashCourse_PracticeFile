import json

def get_stored_usernumber():
    file_name = 'usernumber.json'
    try:
        with open(file_name) as file:
            usernumber = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return usernumber

def get_new_usernumber():
    fav_num = input("What is your favorite number?")
    file_name = 'usernumber.json'
    with open(file_name, 'w') as file:
        json.dump(fav_num, file)
    return fav_num
    
        



def fav_num():
    """Accquire your favorite number."""
    
    fav_num = get_stored_usernumber()
    
    if fav_num:
        print("Your favorite number is "+fav_num+"!")
    
    else:
        fav_num = get_new_usernumber()
        print("Now we remember your favorite number is "+fav_num+".")

fav_num()
