import os
import time
import art

os.system('cls')

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    cipher_text = ""

    if direction != "Codificar".lower() and direction != "Decodificar".lower():
        time.sleep(0.3)
        print("\033[1;31mOpção inválida.\033[m")
    else:
        text = input("\nDigite sua mensagem: ").lower()
        shift = int(input("\nDigite o número do turno: "))
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if direction == "Codificar".lower():
                    new_position = (position + shift) % len(alphabet)
                    cipher_text += alphabet[new_position]
                else:
                    new_position = (position - shift) % len(alphabet)
                    cipher_text += alphabet[new_position]
        
        print(f"\nO texto codificado é: \033[1;32m{cipher_text}\033[m")

direction = input("\nDigite \033[33m[Codificar]\033[m para criptografar, digite \033[33m[Decodificar]\033[m para descriptografar: ")

while True:
    caesar(text="", shift=0, direction=direction)
    time.sleep(0.3)
    answer = input("\nDigite \033[33m[S]\033[m para sair ou \033[33m[C]\033[m para continuar: ").lower()
    if answer == "s":
        print("\nObrigado por usar o programa!")
        break
    direction = input("\nDigite \033[33m[Codificar]\033[m para criptografar, digite \033[33m[Decodificar]\033[m para descriptografar: ")
