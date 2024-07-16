from random import randint
from time import sleep
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Bem-vindo ao Jokênpo.".upper() + "\n\033[1;33mDigite [1] para Pedra, [2] para Papel ou [3] para Tesoura.\033[m\n")
player = int(input("Digite sua jogada: "))
computer_play = randint(1, 3)

sleep(0.8)
print("\nJO")
sleep(0.8)
print("KEN")
sleep(0.8)
print("PO!!!\n")

if (player == 1):
    print("Você jogou: \n" + rock)
elif (player == 2):
    print("Você jogou: \n" + paper)
else:
    print("Você jogou: \n" + scissors)

if (computer_play == 1):
    print("O computador jogou: \n" + rock)
elif (computer_play == 2):
    print("O computador jogou: \n" + paper)
else:
    print("O computador jogou: \n" + scissors)

if (player == 1 and computer_play == 3) or (player == 2 and computer_play == 1) or (player == 3 and computer_play == 2):
    print("\n\033[1;32mVOCÊ VENCEU...\033[m")
elif (player == computer_play):
    print("\n\033[1;33mEMPATE...\033[m")
else:
    print("\n\033[1;31mVOCÊ PERDEU...\033[m")