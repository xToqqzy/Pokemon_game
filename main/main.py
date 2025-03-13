import random
import sys

pokemon_dict = {
    "Pikachu": {
        "name": "Pikachu",
        "hp": 30,
        "moves": ["Thunderbolt", "Quick Attack"]
    },
    "Charmander": {
        "name": "Charmander",
        "hp": 35,
        "moves": ["Ember", "Scratch"]
    },
}


def random_pokemon():
    return random.choice(list(pokemon_dict.values()))


def display_pokemon(pokemon):
    print(
        f"{pokemon['name']} - HP: {pokemon['hp']} | Moves: {', '.join(pokemon['moves'])}")


def player_turn(player_pokemon):
    print(f"Choose a move for {player_pokemon['name']}:")
    for i, move in enumerate(player_pokemon['moves'], 1):
        print(f"{i}. {move}")
    choice = int(input("Enter the number of your chosen move: "))
    return player_pokemon['moves'][choice - 1]


def enemy_turn(enemy_pokemon):
    return random.choice(enemy_pokemon['moves'])


def calculate_damage():
    return random.randint(5, 15)


def battle(player_pokemon, enemy_pokemon):
    print(f"A wild {enemy_pokemon['name']} appears!\n")
    print(
        f"Your Pokémon: {player_pokemon['name']} VS Wild {enemy_pokemon['name']}")

    turns = 5
    while turns > 0:
        print(
            f"\n{player_pokemon['name']} HP: {player_pokemon['hp']} | {enemy_pokemon['name']} HP: {enemy_pokemon['hp']}")

        player_move = player_turn(player_pokemon)
        player_damage = calculate_damage()
        print(
            f"{player_pokemon['name']} uses {player_move}! It does {player_damage} damage.")
        enemy_pokemon['hp'] -= player_damage

        if enemy_pokemon['hp'] <= 0:
            print(
                f"{enemy_pokemon['name']} fainted! {player_pokemon['name']} wins the battle!\n")
            return True

        enemy_move = enemy_turn(enemy_pokemon)
        enemy_damage = calculate_damage()
        print(
            f"{enemy_pokemon['name']} uses {enemy_move}! It does {enemy_damage} damage.")
        player_pokemon['hp'] -= enemy_damage

        if player_pokemon['hp'] <= 0:
            print(
                f"{player_pokemon['name']} fainted! {enemy_pokemon['name']} wins the battle!\n")
            return False

        turns -= 1

    if player_pokemon['hp'] > enemy_pokemon['hp']:
        print(f"\n{player_pokemon['name']} wins the battle!")
        return True
    elif enemy_pokemon['hp'] > player_pokemon['hp']:
        print(f"\n{enemy_pokemon['name']} wins the battle!")
        return False
    else:
        print("\nIt's a draw!")
        return None


def start_game():
    tournament_wins = 0
    total_battles = 0

    while True:
        print(f"Pokemon Text Based Attack Game")
        print(
            f"Tournament Wins: {tournament_wins} | Total Battles: {total_battles}")
        user_choice = input(
            "Press 'P' to play, 'Q' to quit, 'S' to see tournament score: ")

        if user_choice.lower() == "p":
            print("Game starting...\n")

            player_pokemon = random_pokemon()
            enemy_pokemon = random_pokemon()

            display_pokemon(player_pokemon)
            display_pokemon(enemy_pokemon)

            player_wins = battle(player_pokemon, enemy_pokemon)
            total_battles += 1

            if player_wins:
                tournament_wins += 1
                if tournament_wins == 4:
                    print("\nCongratulations! You've won the tournament!")
                    play_again = input("Do you want to play again? (Y/N): ")
                    if play_again.lower() == "n":
                        print("Thanks for playing!")
                        break
                    else:
                        tournament_wins = 0
                        total_battles = 0
                else:
                    print(f"You've won {tournament_wins} game(s). Keep going!")
            else:
                print("You lost this battle. Better luck next time!")

        elif user_choice.lower() == "q":
            print("Thanks for playing!")
            sys.exit()

        elif user_choice.lower() == "s":
            print(
                f"Tournament Wins: {tournament_wins} | Total Battles Played: {total_battles}")


start_game()
