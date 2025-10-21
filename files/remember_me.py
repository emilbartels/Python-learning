from pathlib import Path
import json


def get_stored_userdata(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        userdata = json.loads(contents)
        return userdata
    else:
        return None

def get_new_userdata(path):
    """Prompt for a new userdata."""
    userdata = {}

    #Prompt for username and adds the key-value pair to the dictionary userdata
    username = input("What is your username? ")
    userdata['username'] = username

    #Prompt for age and adds the key-value pair to the dictionary userdata
    age = input("How old are you? ")  
    userdata['age'] = age

    #Prompt for gender and adds the key-value pair to the dictionary userdata
    gender = input("What gender are you? ")
    userdata['gender'] = gender

    contents = json.dumps(userdata)
    path.write_text(contents)
    return userdata

#“Before printing a welcome back message in greet_user(),
#  ask the user if this is the correct username. 
# If it’s not, call get_new_username() to get the correct username.”

def greet_user(path):
    """Greet the user by name."""
    path = Path(path)
    userdata = get_stored_userdata(path)
    
    verify_user = input(f"Is {userdata.get('username')} the correct user? (yes/no) ")
    if verify_user == 'no':
        get_new_userdata(path)
    else:
        if userdata:
            print(f'Welcome {userdata.get('username')}')
            print(f'You are a {userdata.get('gender')}, and are {userdata.get('age')} years old')
        else:
            userdata = get_new_userdata(path)
            print(f"We'll remember you when you come back!")

greet_user('chilltime.json')