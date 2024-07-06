from time import sleep
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo à ilha do Tesouro.\nSua missão é encontrar o tesouro.")
choice_one = input("\nPara qual lado você deseja seguir [direita] ou [esquerda]? ")

if (choice_one == "esquerda"):
    choice_two = input("Escolha [nadar] ou [esperar]: ")
    if (choice_two == "esperar"):
        choice_three = input("Qual porta deseja abrir? [Azul], [Vermelha] ou [Amarela]? ")
        if (choice_three == "Vermelha".lower()):
            print("\033[1;31m\nQueimado pelo fogo. Game Over!!!")
        elif (choice_three == "Azul".lower()):
            print("\033[1;31m\nComido por feras. Gamer Over!!!")
        elif (choice_three == "Amarela".lower()):
            print("\033[1;32m\nParabéns. Você venceu!!!")
        else:
            print("\033[1;31mGamer Over!!!")
    else:
        print("\033[1;31m\nAtacado por trutas. Game Over!!!")
else:
    print("\033[1;31m\nCaiu em um buraco. Game Over!!!")
