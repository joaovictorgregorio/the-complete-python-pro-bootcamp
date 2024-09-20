import random
import time
import os
import art

draw_number = random.randint(1, 100)
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def menu():
    os.system("cls")
    print(art.logo)
    time.sleep(0.5)
    print("\033[7;35;47m\nBEM-VINDO AO JOGO DE ADIVINHAÇÃO DE NÚMEROS...\n\033[m")
    time.sleep(0.5)
    print("  Muito prazer, eu sou o computador por trás deste jogo e neste momento. \n  Estou pensando em um número entre \033[1;36m1\033[m e \033[1;36m100\033[m")

    # print(draw_number)

    choose_difficulty = input("\nEscolha a dificuldade: \033[1;36m[FÁCIL]\033[m ou \033[1;36m[DIFÍCIL]\033[m: ").upper()
    if choose_difficulty == "FACIL":
        game(attempts=EASY_LEVEL_ATTEMPTS)
    elif choose_difficulty == "DIFICIL":
        game(attempts=HARD_LEVEL_ATTEMPTS)
    else:
        print("\033[1;31mOpção inválida!!!\033[m")
        time.sleep(1)
        print("Voltando para o menu...")
        time.sleep(1)
        return menu()
    
def game(attempts):
    while attempts > 0:
        print(f"\nVocê tem {attempts} tentativas para adivinhar o número.")
        guess = int(input("Digite um número: "))
        if guess == draw_number:
            print(f"\nParabéns! Você acertou 😎. O número é: {draw_number}")
            return
        elif guess < draw_number:
            print("Muito baixo! Tente novamente.")
            attempts -= 1
        else:
            print("Muito alto! Tente novamente.")
            attempts -= 1
    print(f"\nVocê esgotou todas as tentativas. O número era {draw_number}.")

menu()