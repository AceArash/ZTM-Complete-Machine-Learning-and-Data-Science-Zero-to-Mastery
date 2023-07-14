# Exercise Password Checker
username = input('What is your UserName? ')
password = input('What is your password? ')

password_length = len(password)

hidden_password = '*' * password_length


print(f'{username}, your password, {hidden_password}, is {len(password-password_length)} letters long')

# print('{username}', password {secret} is {6} letters long')

# print('*' * 10)
# Restaring again on 09-07-2023 time: 12:15