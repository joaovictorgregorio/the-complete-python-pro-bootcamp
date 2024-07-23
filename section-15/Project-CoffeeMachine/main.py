from art import logo
from time import sleep
from data import MENU, resources
from os import system
from crayons import yellow


def report():
    return f"Agua: {resources["water"]}ml\n" \
           f"Leite: {resources["milk"]}ml\n" \
           f"Café: {resources["coffee"]}g\n" \
           f"Dinheiro: R$0,00"


def screen():
    system("cls")
    print(logo)

    sleep(0.5)
    print("3 Opções disponíveis: ", end="")
    print(yellow("[Expresso, café com leite e cappuccino]".upper(), bold=True))

    home_menu = input("\nQue tipo de café gostaria de pedir? ")

    if home_menu == "RELATORIO".lower():
        print(report())


def coffe_machine():
    pass


screen()