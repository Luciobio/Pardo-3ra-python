""" from google.colab import drive
drive.mount('/drive/') """

import json
import getpass

def setCredentials(path,data):
  try:
    with open(path + 'data.json', 'w') as file:
      json.dump(data, file, indent=4)
  except FileNotFoundError:
    print('\033[0;31mNo such file or directory:\033[0m', path,'.\n')

def getCredentials(path):
  try:
    with open(path + '/data.json') as file:
      data = json.load(file)
      #print('\033[0;32mSuccess!\033[0m')
  except json.JSONDecodeError:
    print('\033[0;31mFile has errors and cannot be loaded.\033[0m')
  except FileNotFoundError:
    print('\033[0;31mNo such file or directory:\033[0m', path,'.\n') 
  return data

path = '/drive/MyDrive/'

data = {}
data['credentials'] = []

setCredentials(path,data)


def alreadyExist(user, data):
  for record in data['credentials']:
    if record['Username'] == user:
      return True
  return False

def signIn():
    data = getCredentials(path)

    while True:
      print('\033[0;34mUser Sign in\033[0m')
      username = input('Enter Username: ')
      password = getpass.getpass('Enter Password: ')

      if len(username) < 4 or len(password) < 6:
          print('\033[3;33mUsername should be at least 4 characters long, and password should be at least 6 characters long.\033[0m\n')
      elif alreadyExist(username,data):
        print('\033[3;33mSorry, this username is already taken, please select a different one.\033[0m\n') 
      else:
          data['credentials'].append({'Username': username, 'Password': password})
          setCredentials(path,data)
          print('\n\033[3;32mCredentials saved successfully!\033[0m\n')
          break

def logIn():
    data = getCredentials(path)
    if len(data['credentials']) < 1:
      print('\033[0;36mThere are no registered users, please Sign in first.\033[0m')
      return

    print('\033[0;34mUser Login\033[0m')
    username = input('Enter Username: ')
    password = getpass.getpass('Enter Password: ')

    for record in data['credentials']:
        if record['Username'] == username:
            if record['Password'] == password:
                print('\033[1;32mAccess granted!\033[0m\n')
                return
            else:
                print('\033[3;33mWrong password!\033[0m\n')
                return

    print("\033[1;31mThe user doesn't exist!\033[0m\n")

def showUserList():
    data = getCredentials(path)
    if len(data['credentials']) < 1:
      print('\033[0;36mThere are no registered users, please Sign in first.\033[0m')
      return

    print('\033[0;34mUser List\033[0m')
    print('\033[36;3;4mUsername   -   Password\033[0m')
    for record in data['credentials']:
        print(f"{record['Username']}   -   {record['Password']}")
    print('\n')

def start(): 
  while True:
      choice = input('Select an option:\n1 - User Sign In\n2 - User Log In\n3 - Print the list of users\nOr type "exit" to end.\n\n')

      if choice == '1':
          signIn()
      elif choice == '2':
          logIn()
      elif choice == '3':
          showUserList()
      elif choice.lower() == 'exit':
          print('\033[36;3;4mGood Bye! Come again soon =D !\033[0m')
          break

      else:
          print('\033[3;33m"'+choice+'"' + ' is not a valid option.\033[0m\n')


start()