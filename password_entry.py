"""Reuben Koshy"""

password = input("Enter a Password: ")

while len(password) >= 0:
    if len(password) >= 8:
        print("Valid Password")
        print('*' * len(password))
        break
    else:
        print("Invalid password. Must be at least 8 characters in length")
        password = input("Enter a Password: ")
