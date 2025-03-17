import random

# 8 Pokémon met hun stats en aanvallen
pokemon_dict = {
    "Pikachu": {
        "name": "Pikachu",
        "type": "Electric",
        "hp": 100,
        "speed": 90,
        "attacks": [
            {"name": "Thunderbolt", "min_damage": 40, "max_damage": 50},
            {"name": "Quick Attack", "min_damage": 10, "max_damage": 15}
        ]
    },
    "Squirtle": {
        "name": "Squirtle",
        "type": "Water",
        "hp": 120,
        "speed": 40,
        "attacks": [
            {"name": "Water Gun", "min_damage": 30, "max_damage": 40},
            {"name": "Quick Attack", "min_damage": 10, "max_damage": 20}
        ]
    },
    "Charmander": {
        "name": "Charmander",
        "type": "Fire",
        "hp": 80,
        "speed": 60,
        "attacks": [
            {"name": "Ember", "min_damage": 40, "max_damage": 50},
            {"name": "Quick Attack", "min_damage": 10, "max_damage": 15}
        ]
    },
    "Bulbasaur": {
        "name": "Bulbasaur",
        "type": "Grass",
        "hp": 130,
        "speed": 40,
        "attacks": [
            {"name": "Vine Whip", "min_damage": 30, "max_damage": 45},
            {"name": "Tackle", "min_damage": 5, "max_damage": 20}
        ]
    },
    "Eevee": {
        "name": "Eevee",
        "type": "Normal",
        "hp": 100,
        "speed": 100,
        "attacks": [
            {"name": "Tackle", "min_damage": 20, "max_damage": 35},
            {"name": "Quick Attack", "min_damage": 10, "max_damage": 15}
        ]
    },
    "Gengar": {
        "name": "Gengar",
        "type": "Ghost",
        "hp": 70,
        "speed": 120,
        "attacks": [
            {"name": "Shadow Ball", "min_damage": 50, "max_damage": 65},
            {"name": "Quick Attack", "min_damage": 20, "max_damage": 40}
        ]
    },
    "Blissey": {
        "name": "Blissey",
        "type": "Normal",
        "hp": 250,
        "speed": 30,
        "attacks": [
            {"name": "Dazzling Gleam", "min_damage": 20, "max_damage": 30},
            {"name": "Quick Attack", "min_damage": 10, "max_damage": 20}
        ]
    },
    "Fearow": {
        "name": "Fearow",
        "type": "Flying",
        "hp": 91,
        "speed": 130,
        "attacks": [
            {"name": "Aerial Ace", "min_damage": 40, "max_damage": 50},
            {"name": "Quick Attack", "min_damage": 10, "max_damage": 15}
        ]
    }
}

# Type-effectiveness chart
type_chart = {
    "electric": {"strong_against": ["water", "flying"], "weak_against": ["ground"]},
    "fire": {"strong_against": ["grass"], "weak_against": ["water"]},
    "water": {"strong_against": ["fire"], "weak_against": ["grass"]},
    "normal": {"strong_against": [], "weak_against": ["normal"]},
    "flying": {"strong_against": ["grass"], "weak_against": ["electric"]},
    "ghost": {"strong_against": ["normal"], "weak_against": ["ghost"]},
}

# Functie om schade te berekenen


def calculate_damage(pokemon, attack_name):
    for attack in pokemon['attacks']:
        if attack['name'] == attack_name:
            return random.randint(attack['min_damage'], attack['max_damage'])
    return 0  # Als de aanval niet wordt gevonden

# Functie om te bepalen wie eerst aanvalt


def decide_turn(pokemon1, pokemon2):
    if pokemon1["speed"] > pokemon2["speed"]:
        return pokemon1, pokemon2
    elif pokemon1["speed"] < pokemon2["speed"]:
        return pokemon2, pokemon1
    else:
        return pokemon1, pokemon2

# Functie om de type-effecten toe te passen


def apply_type_effects(attacker, defender, damage):
    attacker_type = attacker["type"].lower()
    defender_type = defender["type"].lower()

    if defender_type in type_chart[attacker_type]["strong_against"]:
        return damage * 1.3  # 30% meer schade
    elif defender_type in type_chart[attacker_type]["weak_against"]:
        return damage * 0.7  # 30% minder schade
    return damage

# Functie om het gevecht te simuleren


def battle(pokemon1, pokemon2):
    # Wie valt eerst aan?
    attacker, defender = decide_turn(pokemon1, pokemon2)
    print(f"{attacker['name']} valt eerst aan!")

    # Kies een aanval voor de aanvaller
    # We gebruiken de eerste aanval (zoals Thunderbolt, Water Gun)
    attack_name = attacker["attacks"][0]["name"]
    damage = calculate_damage(attacker, attack_name)
    print(
        f"{attacker['name']} gebruikt {attack_name} en doet {damage} schade!")

    # Pas type-effect toe
    damage = apply_type_effects(attacker, defender, damage)

    # Verlaag de HP van de verdediger
    defender["hp"] -= damage
    print(f"{defender['name']} heeft nog {defender['hp']} HP over!")

    # Controleer of de verdediger nog leeft
    if defender["hp"] <= 0:
        print(f"{defender['name']} is verslagen!")
    else:
        # De andere Pokémon valt nu aan
        attacker, defender = defender, attacker
        attack_name = attacker["attacks"][0]["name"]
        damage = calculate_damage(attacker, attack_name)
        print(
            f"{attacker['name']} gebruikt {attack_name} en doet {damage} schade!")

        # Pas type-effect toe
        damage = apply_type_effects(attacker, defender, damage)

        # Verlaag de HP van de nieuwe verdediger
        defender["hp"] -= damage
        print(f"{defender['name']} heeft nog {defender['hp']} HP over!")

        if defender["hp"] <= 0:
            print(f"{defender['name']} is verslagen!")


# Simuleer een gevecht tussen twee Pokémon
pikachu = pokemon_dict["Pikachu"]
squirtle = pokemon_dict["Squirtle"]
battle(pikachu, squirtle)
