from art import logo
from time import sleep
from data import MENU, resources
from os import system
from crayons import yellow, green, red

"""Função para melhorar a repetição do código
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(yellow("\nAqui está seu café com leite ☕. Aproveite!"))
"""


def expresso():
    resources["water"] -= MENU["expresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["expresso"]["ingredients"]["coffee"]
    resources["money"] += MENU["expresso"]["cost"]
    print(yellow("\nAqui está seu expresso ☕. Aproveite!", bold=True))


def cappucino():
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    resources["money"] += MENU["cappuccino"]["cost"]
    print(yellow("\nAqui está seu cappuccino ☕. Aproveite!", bold=True))


def latte():
    resources["water"] -= MENU["cafe com leite"]["ingredients"]["water"]
    resources["milk"] -= MENU["cafe com leite"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["cafe com leite"]["ingredients"]["coffee"]
    resources["money"] += MENU["cafe com leite"]["cost"]
    print(yellow("\nAqui está seu café com leite ☕. Aproveite!", bold=True))


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Desculpe, não temos {item} suficiente.")
            return False
    return True


def calculate_change(money):
    change_of_money = money - MENU["cafe com leite"]["cost"]
    print(f"Seu troco é R${change_of_money:.2f}")


def insert_coins(drink):
    print(green("Por favor, insira as moedas...", bold=True))
    quarter = int(input("Quantas moedas de 25 centavos? ")) * 0.25
    dime = int(input("Quantas moedas de 10 centavos? ")) * 0.10
    nickel = int(input("Quantas moedas de 5 centavos? ")) * 0.05
    pennie = int(input("Quantas moedas de 1 centavo? ")) * 0.01

    money = quarter + dime + nickel + pennie

    if money < drink["cost"]:
        print(red("Dinheiro insuficiente. Sua compra foi cancelada."))
        sleep(3)
        screen()

    print(f"Você inseriu R${money:.2f}")
    calculate_change(money)

    if drink == MENU["cafe com leite"]:
        latte()
    elif drink == MENU["cappuccino"]:
        cappucino()
    else:
        expresso()


def report():
    return f"Agua: {resources["water"]}ml\n" \
           f"Leite: {resources["milk"]}ml\n" \
           f"Café: {resources["coffee"]}g\n" \
           f"Dinheiro: R${resources["money"]}"


def coffe_machine():
    while True:
        home_menu = input("\nQue tipo de café gostaria de pedir? ").lower()
        if home_menu == "sair":
            print(yellow("Máquina desligada para manutenção".upper()))
            sleep(3)
            break
        elif home_menu == "relatorio":
            print(report())
        else:
            drink = MENU[home_menu]
            if is_resources_sufficient(drink["ingredients"]):
                insert_coins(drink)


def screen():
    system("cls")
    sleep(0.5)
    print(logo)
    sleep(0.5)
    print("3 Opções disponíveis: ", end="")
    print(yellow("[Expresso, café com leite e cappuccino]".upper()))
    coffe_machine()


screen()