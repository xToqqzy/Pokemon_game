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
    "Charizard": {"type": "Fire", "hp": 80, "attack": 85, "speed": 100, "moves": [("Flamethrower", "Fire"), ("Fire Spin", "Fire")]},
    "Blastoise": {"type": "Water", "hp": 90, "attack": 80, "speed": 78, "moves": [("Water Gun", "Water"), ("Hydro Pump", "Water")]},
    "Venusaur": {"type": "Grass", "hp": 85, "attack": 82, "speed": 80, "moves": [("Vine Whip", "Grass"), ("Razor Leaf", "Grass")]},
    "Pikachu": {"type": "Electric", "hp": 70, "attack": 75, "speed": 110, "moves": [("Thunderbolt", "Electric"), ("Thunder Shock", "Electric")]},
    "Gengar": {"type": "Ghost", "hp": 75, "attack": 90, "speed": 105, "moves": [("Shadow Ball", "Ghost"), ("Lick", "Ghost")]},
    "Machamp": {"type": "Fighting", "hp": 88, "attack": 95, "speed": 65, "moves": [("Punch", "Fighting"), ("Karate Chop", "Fighting")]},
    "Dragonite": {"type": "Dragon", "hp": 100, "attack": 90, "speed": 80, "moves": [("Dragon Claw", "Dragon"), ("Twister", "Dragon")]},
    "Snorlax": {"type": "Normal", "hp": 120, "attack": 85, "speed": 30, "moves": [("Body Slam", "Normal"), ("Headbutt", "Normal")]}
}


def calculate_damage(attacker, defender, move):
    move_name, move_type = move
    base_damage = random.randint(10, 20)
    effect_text = "Het was een normale hit."

    if move_type in type_chart:
        if defender["type"] in type_chart[move_type]["strong"]:
            base_damage = int(base_damage * 1.2)
            effect_text = "Het was super effectief!"
        elif defender["type"] in type_chart[move_type]["weak"]:
            base_damage = int(base_damage * 0.8)
            effect_text = "Het was niet erg effectief."

    return base_damage, effect_text, move_name


def battle(player, opponent):
    print(f"\n--- {player['name']} vs {opponent['name']} ---")
    print(
        f"{player['name']} Speed: {player['speed']} | {opponent['name']} Speed: {opponent['speed']}")

    first, second = (player, opponent) if player["speed"] >= opponent["speed"] else (
        opponent, player)
    print(f"{first['name']} is sneller en begint!")

    while player["hp"] > 0 and opponent["hp"] > 0:
        for attacker, defender in [(first, second), (second, first)]:
            if defender["hp"] <= 0:
                break

            if attacker == player:
                input("Jij bent aan de beurt! Druk op 'a' om aan te vallen.")
                move = attacker["moves"][int(
                    input("Kies je aanval (1 of 2): ")) - 1]
            else:
                move = random.choice(attacker["moves"])

            damage, effect_text, move_name = calculate_damage(
                attacker, defender, move)
            defender["hp"] -= damage
            print(
                f"{attacker['name']} gebruikte {move_name}! {effect_text} {defender['name']} heeft nog {max(0, defender['hp'])} HP.")

            if defender["hp"] <= 0:
                print(f"{defender['name']} is verslagen!")
                return attacker


def tournament(player_choice):
    remaining_pokemon = [p for p in pokemon_data.keys() if p != player_choice]
    random.shuffle(remaining_pokemon)
    rounds = ["Kwartfinale", "Halve finale", "Finale"]
    player = {"name": player_choice, **pokemon_data[player_choice]}

    for round_name in rounds:
        ai_pokemon = remaining_pokemon.pop()
        opponent = {"name": ai_pokemon, **pokemon_data[ai_pokemon]}
        print(f"\n{round_name}: {player['name']} tegen {opponent['name']}!")
        input("Druk op 'a' om te beginnen.")

        winner = battle(player, opponent)
        if winner != player:
            print(f"Je bent uitgeschakeld in de {round_name}.")
            return

    print("Gefeliciteerd! Je hebt het toernooi gewonnen!")


player_choice = input("Kies je Pokémon: " +
                      ", ".join(pokemon_data.keys()) + ": ")
tournament(player_choice)
