'''programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Recuperando um item do dicionário
print(programming_dictionary["Bug"] + "\n")

# Adicionando um novo item ao dicionário
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Criando um dicionário vazio
empty_dictionary = {}

# Limpar um dicionário
programming_dictionary = {}
print(programming_dictionary)

# Editar um item no dicionário
programming_dictionary["Bug"] = "Um erro no programa que impede o programa de ser executado corretamente."
print(programming_dictionary)

# Loop em um dicionário
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
'''

##################################################################################################### 

# Aninhamento
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Aninhando uma lista em um dicionário
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Aninhando um dicionário em outro dicionário
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Aninhando um dicionário dentro de uma lista
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]