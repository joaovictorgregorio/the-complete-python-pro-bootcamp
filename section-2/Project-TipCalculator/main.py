from time import sleep
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print('Bem-vindo calculadora de gorjeta!!!\n')

value = float(input('Digite o valor da conta: R$'))
sleep(0.5)
percentage = int(input('Digite a porcentagem da gorjeta? 10, 12 ou 15? '))
sleep(0.5)
amount_of_people = int(input('Quantas pessoas vão dividir a conta? '))
sleep(0.5)

bill_amount_plus_tip = value + (value * percentage / 100)
account_value = bill_amount_plus_tip / amount_of_people

print(f'\033[32m\nProcessando...\n\033[m')
sleep(1)
print(f'Cada pessoa irá pagar: \033[32mR${account_value:.2f}')