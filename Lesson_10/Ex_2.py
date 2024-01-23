'''Write a Python program that asks the user to enter a password. Keep asking for the
password until the correct password "secret" is entered. Provide appropriate feedback
to the user.'''

while True:
    a = input('Enter the password: ')

    if a == 'secret':
        print('Correct password! Access granted.')
        break
    else:
        print('Incorrect password. Try again.')