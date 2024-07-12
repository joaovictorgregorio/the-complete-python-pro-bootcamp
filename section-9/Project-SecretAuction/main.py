import os
import time
import art

os.system('cls')

print(art.logo)
bids = {}
bidding_finished = False

def find_highest_binder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nO vencedor é \033[33m{winner.capitalize()}\033[m com uma oferta de \033[1;32mR${highest_bid}\033[m")

while bidding_finished == False:
    name = input("\nDigite o nome do participante: ")
    bid = int(input("Qual o valor do lance? R$"))
    bids[name] = bid
    should_continue = input("Deseja cadastrar outro participante? Digite [sim] ou [nao]: ").lower()
    if should_continue == "nao":
        bidding_finished = True
        find_highest_binder(bids)
    elif should_continue == "sim":
        os.system('cls')
        print(art.logo)

