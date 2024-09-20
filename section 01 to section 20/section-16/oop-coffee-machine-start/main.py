from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from os import system
from time import sleep
from crayons import yellow

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

system("cls")
print(logo)
while True:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        print(yellow("off".upper()))
        sleep(2)
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)