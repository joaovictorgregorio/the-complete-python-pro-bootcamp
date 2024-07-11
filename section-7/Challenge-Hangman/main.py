import random
from time import sleep
import os
import sys

def close_application():
    sys.exit()

os.system('cls')
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["porcodaterra", "babuino", "camelo"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(f"A palavra selecionada pelo sistema foi: {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"

while "_" in display:
    guess = input("Adivinhe uma letra: ").lower()

    if guess in display:
        print("Você já adivinhou essa letra. Tente novamente.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            guess = input("Adivinhe uma letra: ").lower()
            if lives == 0:
                print("\033[31mVocê perdeu!")
                close_application()

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("\033[32mVocê venceu!")
        break
