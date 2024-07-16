import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\033[1;34mBem-vindo ao gerador de senhas contra hackers!!!\033[m")
nr_letters= int(input("\nQuantas letras você quer que tenha? ")) 
nr_symbols = int(input("Quantos símbolos você quer que tenha? "))
nr_numbers = int(input("Quantos números você quer que tenha? "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

character_list = list(password)
random.shuffle(character_list)
scrambled_password = ''.join(character_list)

print(f"\nSua senha é: \033[32m{scrambled_password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P