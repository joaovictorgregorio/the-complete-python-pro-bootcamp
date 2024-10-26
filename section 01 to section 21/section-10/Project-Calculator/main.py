import os
import art

os.system("cls")

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    print("\033[36mBem-vindo à calculadora!")
    print("Vamos começar?\033[m")

    number1 = float(input("\nDigite o primeiro valor: "))
    print("Escolha a operação 👇")
    for symbol in operations:
        print(symbol)

    continue_calculator = True

    while continue_calculator:
        operation_symbol = input("Digite uma operação da linha acima: ")
        number2 = float(input("Digite o próximo valor: "))
        if operation_symbol in operations:
            operation = operations[operation_symbol]
            answer = operation(number1, number2)
            print(f"{number1:.1f} {operation_symbol} {number2:.1f} = {answer:.1f}")
            question = input(f"Digite [S] para calcular com \033[33m{answer:.1f}\033[m, ou digite [N] para começar um novo cálculo.: ").upper()
            if question not in ("S"): 
                if question in ("N"):
                    continue_calculator = False
                    os.system("cls")
                    calculator()
                else:
                    continue_calculator = False
                    print("\033[1;31mResposta inválida.\033[m")
                    
            else:
                number1 = answer
        else:
            continue_calculator = False
            print("\033[1;31mOperação inválida.\033[m")

calculator()