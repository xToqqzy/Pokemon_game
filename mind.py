import random

type_chart = {
    "Fire": {"strong": ["Grass"], "weak": ["Water"]},
    "Water": {"strong": ["Fire"], "weak": ["Grass"]},
    "Grass": {"strong": ["Water"], "weak": ["Fire"]},
    "Electric": {"strong": ["Water"], "weak": []},
    "Ghost": {"strong": ["Psychic"], "weak": []},
    "Fighting": {"strong": ["Normal"], "weak": []},
    "Dragon": {"strong": ["Dragon"], "weak": []},
    "Normal": {"strong": [], "weak": ["Fighting"]}
}

pokemon_data = {
    "Charizard": {"type": "Fire", "hp": 80, "attack": 85, "defense": 70, "speed": 100, "moves": {1: ("Flamethrower", "Fire"), 2: ("Fire Spin", "Fire", True)}},
    "Blastoise": {"type": "Water", "hp": 90, "attack": 80, "defense": 85, "speed": 78, "moves": {1: ("Water Gun", "Water"), 2: ("Hydro Pump", "Water", True)}},
    "Venusaur": {"type": "Grass", "hp": 85, "attack": 82, "defense": 83, "speed": 80, "moves": {1: ("Vine Whip", "Grass"), 2: ("Razor Leaf", "Grass", True)}},
    "Pikachu": {"type": "Electric", "hp": 70, "attack": 75, "defense": 60, "speed": 110, "moves": {1: ("Thunderbolt", "Electric"), 2: ("Thunder Shock", "Electric", True)}},
    "Gengar": {"type": "Ghost", "hp": 75, "attack": 90, "defense": 65, "speed": 105, "moves": {1: ("Shadow Ball", "Ghost"), 2: ("Lick", "Ghost", True)}},
    "Machamp": {"type": "Fighting", "hp": 88, "attack": 95, "defense": 85, "speed": 65, "moves": {1: ("Punch", "Fighting"), 2: ("Karate Chop", "Fighting", True)}},
    "Dragonite": {"type": "Dragon", "hp": 100, "attack": 90, "defense": 90, "speed": 80, "moves": {1: ("Dragon Claw", "Dragon"), 2: ("Twister", "Dragon", True)}},
    "Snorlax": {"type": "Normal", "hp": 120, "attack": 85, "defense": 95, "speed": 30, "moves": {1: ("Body Slam", "Normal"), 2: ("Headbutt", "Normal", True)}}
}


def calculate_damage(attacker, defender, move):
    name, move_type, *multi_hit = move
    base_damage = random.randint(10, 20)
    effectiveness = 1.0
    if move_type in type_chart:
        if defender["type"] in type_chart[move_type]["strong"]:
            effectiveness = 1.2
            effect_text = "It was super effective!"
        elif defender["type"] in type_chart[move_type]["weak"]:
            effectiveness = 0.8
            effect_text = "It was not very effective."
        else:
            effect_text = "It was a normal hit."
    else:
        effect_text = "It was a normal hit."

    damage = int(base_damage * effectiveness)
    if multi_hit:
        hit_times = random.randint(2, 5)
        total_damage = damage * hit_times
        return total_damage, effect_text, hit_times
    return damage, effect_text, None


def battle(player_pokemon, ai_pokemon, round_name):
    print(f"\nBattle: {player_pokemon['name']} vs {ai_pokemon['name']}")
    print(
        f"{player_pokemon['name']} Speed: {player_pokemon['speed']}, {ai_pokemon['name']} Speed: {ai_pokemon['speed']}")
    first, second = (player_pokemon, ai_pokemon) if player_pokemon["speed"] >= ai_pokemon["speed"] else (
        ai_pokemon, player_pokemon)
    print(f"{first['name']} heeft de hoogste snelheid en begint!")

    while player_pokemon["hp"] > 0 and ai_pokemon["hp"] > 0:
        for attacker, defender in [(first, second), (second, first)]:
            if defender["hp"] <= 0:
                break

            if attacker == player_pokemon:
                input("Jij bent aan de beurt! Druk op 'a' om verder te gaan.")
                move_choice = int(input(
                    f"Choose your attack: 1-{attacker['moves'][1][0]}, 2-{attacker['moves'][2][0]}: "))
            else:
                input("De tegenstander is aan de beurt! Druk op 'a' om verder te gaan.")
                move_choice = random.choice([1, 2])

            move = attacker["moves"][move_choice]
            damage, effect_text, hits = calculate_damage(
                attacker, defender, move)
            defender["hp"] -= damage
            print(
                f"{attacker['name']} used {move[0]}! It dealt {damage} damage. {effect_text}")
            if hits:
                print(f"The attack hit {hits} times!")
            print(f"{defender['name']} has {max(0, defender['hp'])} HP left.")

            if defender["hp"] <= 0:
                print(f"{defender['name']} fainted!")
                if defender == player_pokemon:
                    print(
                        f"Je hebt verloren in de {round_name}. Je bent klaar!")
                    return None
                return attacker


def tournament(player_choice):
    remaining_pokemon = list(pokemon_data.keys())
    remaining_pokemon.remove(player_choice)
    random.shuffle(remaining_pokemon)
    rounds = ["Kwartfinale", "Halve finale", "Finale"]
    player = {"name": player_choice, **pokemon_data[player_choice]}

    for i in range(3):
        ai = {"name": remaining_pokemon.pop(
        ), **pokemon_data[remaining_pokemon[-1]]}
        print(f"\nVolgende ronde: {rounds[i]} tegen {ai['name']}")
        input("Druk op 'a' om te starten.")
        winner = battle(player, ai, rounds[i])
        if winner != player:
            return
    print("Gefeliciteerd! Je hebt het toernooi gewonnen!")


player_choice = input("Kies je Pokémon: " +
                      ", ".join(pokemon_data.keys()) + ": ")
tournament(player_choice)
