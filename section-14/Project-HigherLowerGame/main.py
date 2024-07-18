import art, game_data, random, time, os

def random_selection():
    random_selection_one = random.choice(game_data.data)
    key_name_one = random_selection_one["name"]
    key_description_one = random_selection_one["description"]
    key_country_one = random_selection_one["country"]

    print(f"\n  Compare A: {key_name_one}, um(a) {key_description_one}, do(a) {key_country_one}", end="")

    print(art.vs)
    random_selection_two = random.choice(game_data.data)
    key_name_two = random_selection_two["name"]
    key_description_two = random_selection_two["description"]
    key_country_two = random_selection_two["country"]

    print(f"  Contra B: {key_name_two}, um(a) {key_description_two}, do(a) {key_country_two}")



def menu():
    os.system("cls")

    print(art.logo)
    random_selection_one = random.choice(game_data.data)
    key_name_one = random_selection_one["name"]
    key_description_one = random_selection_one["description"]
    key_country_one = random_selection_one["country"]

    print(f"\n  Compare A: \033[1;33m{key_name_one}\033[m, um(a) {key_description_one}, do(a) {key_country_one}", end="")

    print(art.vs)
    random_selection_two = random.choice(game_data.data)
    key_name_two = random_selection_two["name"]
    key_description_two = random_selection_two["description"]
    key_country_two = random_selection_two["country"]
    
    print(f"  Contra B: \033[1;33m{key_name_two}\033[m, um(a) {key_description_two}, do(a) {key_country_two}")

    more_followers = input("\nQuem tem mais seguidores? Digite 'A' ou 'B': ").upper()

    if random_selection_one["follower_count"] > random_selection_two["follower_count"] and more_followers == "A":
        print("Você acertou!")
        print(random_selection_one)
        print(random_selection_two)
    elif random_selection_one["follower_count"] < random_selection_two["follower_count"] and more_followers == "B":
        print("Você acertou!")
        print(random_selection_two)
        print(random_selection_one)
    else:
        print("Você errou!")
        print(random_selection_one)
        print(random_selection_two)

menu()

