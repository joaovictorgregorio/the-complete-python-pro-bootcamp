import art, game_data, random, time, os

os.system("cls")

def screen():
    print(art.logo)
    
    higher_lower_game()


def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"

def higher_lower_game():
    score = 0
    game_should_continue = True
    account_b = random.choice(game_data.data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(game_data.data)

        if account_a == account_b:
            account_b = random.choice(game_data.data)

        print(f"  Compare A: \033[1;33m{account_a['name']}\033[m, a {account_a['description']}, de {account_a['country']}")
        print(art.vs)
        print(f"  Contra B: \033[1;33m{account_b['name']}\033[m, a {account_b['description']}, de {account_b['country']}")

        guess = input("Quem tem mais seguidores nas redes sociais? Digite 'A' ou 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system("cls")
        print(art.logo)

        if is_correct:
            score += 1
            print(f" \033[1;32mVocê acertou\033[m, sua pontuação atual: \033[1;33m{score}\033[m")

        else:
            game_should_continue = False
            print(f" Desculpe, você errou. Seu score final é de: {score}")
    
screen()

