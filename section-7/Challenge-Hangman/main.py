import random
from time import sleep
import os
import sys
from hangman_words import word_list
import hangman_art

os.system('cls')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)
print(f"\nA palavra selecionada pelo sistema foi: {chosen_word}")

display = []
for _ in range(word_length):
    display += "_"

while "_" in display:
    guess = input("Adivinhe uma letra: ").lower()

    os.system('cls')

    if guess in display:
        print("\033[33mVocê já adivinhou essa letra. Tente novamente.\033[m")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"A letra \033[1;36m{guess.upper()}\033[m não está na palavra. \033[1;31mVocê perdeu uma vida.\033[m")
        lives -= 1
        if lives == 0:
            print("\033[1;31mVocê perdeu!")
            break

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("\033[1;32mVocê venceu!")
        break

    print(hangman_art.stages[lives])
