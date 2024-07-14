import os
os.system('cls')

# Funções já usadas com saídas


# Funções com saídas
def format_name(f_name, l_name):
    """Pegue um nome e um sobrenome e formate-os para retornar a versão maiúscula do nome"""
    if f_name == "" or l_name == "":
        return "Você não digitou nenhum nome"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# print(
#     format_name(
#         input("Digite seu primeiro nome? "), 
#         input("Digite seu sobrenome? ")
#     )
# )
