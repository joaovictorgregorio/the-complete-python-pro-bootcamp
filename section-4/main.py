import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

# RANDOM MODULE
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)


# UNDERSTANDING THE OFFSET AND APPENDING ITEMS TO LISTS
''' states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

print(states_of_america[-2])

states_of_america.append("JoaoIsland") # Adiciona o item ao final da lista
states_of_america.extend(["MarrocosIsland", "AlaskaIsland"]) # Adiciona vários itens ao final da lista

print(states_of_america) '''

# INDEXERRORS AND WORKING WITH NESTED LISTS
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # Uma lista que contém duas listas
print(dirty_dozen[1][1]) # Primeiro [1] representa a lista, segundo [1] representa o item dentro da lista