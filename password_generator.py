import random
### Password Generatore
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~',]

import random

print(" !! Welcome to the Password Generator !!! ")
inp_letter = int(input("Enter the number of letter you want\n"))
inp_number = int(input("Enter the number of numerical you want\n"))
inp_symbol = int(input("Enter the number of symbols you wants\n"))

password = []
for char in range(1, inp_letter + 1):
    a = random.choice(letter)
    password += a
#print(password)

for char in range(1, inp_number + 1):
    b = random.choice(number)
    password += b
#print(password)

for char in range(1, inp_symbol + 1):
    c = random.choice(symbol)
    password += c
#print(password)
random.shuffle(password)
your_password = ""
for char in password:
    your_password += char

print(f"Your password is {your_password}")
