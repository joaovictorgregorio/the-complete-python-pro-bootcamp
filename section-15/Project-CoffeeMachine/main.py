from art import logo
from time import sleep
from data import MENU, resources
from os import system
from crayons import yellow, green


def latte():
    print(yellow("\nAqui está seu café com leite ☕. Aproveite!"))


def calculate_change(money):
    change = money - MENU["cafe com leite"]["cost"]
    print(f"Seu troco é R${change:.2f}")


def insert_coins():
    print(green("Por favor, insira as moedas.", bold=True))
    quarter = int(input("Quantas moedas de 25 centavos? "))
    quarter = quarter * 0.25
    dime = int(input("Quantas moedas de 10 centavos? "))
    dime = dime * 0.10
    nickel = int(input("Quantas moedas de 5 centavos? "))
    nickel = nickel * 0.05
    pennie = int(input("Quantas moedas de 1 centavo? "))
    pennie = pennie * 0.01

    money = quarter + dime + nickel + pennie
    print(f"Você inseriu R${money:.2f}")
    calculate_change(money)


def report():
    return f"Agua: {resources["water"]}ml\n" \
           f"Leite: {resources["milk"]}ml\n" \
           f"Café: {resources["coffee"]}g\n" \
           f"Dinheiro: R$0,00"


def coffe_machine():
    while True:
        home_menu = input("\nQue tipo de café gostaria de pedir? ").upper()
        if home_menu == "RELATORIO":
            print(report())
        elif home_menu == "CAFE COM LEITE":
            insert_coins()
            latte()
        else:
            break


def screen():
    system("cls")
    print(logo)

    sleep(0.5)
    print("3 Opções disponíveis: ", end="")
    print(yellow("[Expresso, café com leite e cappuccino]".upper(), bold=True))

    coffe_machine()


screen()