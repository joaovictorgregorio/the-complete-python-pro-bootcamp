from os import system

system("cls")
"""Quando uma função está ligada a um objeto, chama-se então um método"""


class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Matias")
user_2 = User("002", "Jack")
print(user_1.id, user_1.username, user_1.followers)
print(user_2.id, user_2.username, user_2.followers)

print("\n")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


"""
# Criação da clase User
class User:
    def __init__(self) -> None:
        print("Novo usuário criado!")


# Criação do objeto user_1
user_1 = User()

# Atribuindo valores aos atributos do objeto user_1
#  Um atributo é uma variável que está associada a um objeto
user_1.id = "001"
user_1.username = "Matias"

# Imprimindo os atributos do objeto user_1
print(user_1.id, user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "Jack"
print(user_2.id, user_2.username)
"""