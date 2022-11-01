import json

def greet_user():
    user_name = input('''what's your name?''')
    file_name = user_name + '.json'
    try:
        with open(file_name) as file_object:
            user_messege = json.load(file_object)
            print('Welcome back, '+ user_messege + '!')
    except FileNotFoundError:
        with open(file_name, 'w') as file_object:
            json.dump(user_name,file_object)
            print('Hello ' + user_name +'! We will remember you next time!')

greet_user()



