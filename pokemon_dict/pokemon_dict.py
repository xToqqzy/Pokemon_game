import random
pokemon_dict = {
    "Pikachu": {
        "name": "Pikachu",
        "type": "Electric",
        "hp": 100,
        "speed": 90,
        "attacks": [
            {"name": "Thunderbolt", "min_damage": 40,
                "max_damage": 50, "multi_hit": False},
            {"name": "Quick Attack", "min_damage": 10,
                "max_damage": 15, "multi_hit": True}
        ]
    },
    "Squirtle": {
        "name": "Squirtle",
        "type": "Water",
        "hp": 120,
        "speed": 40,
        "attacks": [
            {"name": "Water Gun", "min_damage": 30,
                "max_damage": 40, "multi_hit": False},
            {"name": "Quick Attack", "min_damage": 10,
                "max_damage": 20, "multi_hit": True}
        ]
    },
    "Charmander": {
        "name": "Charmander",
        "type": "Fire",
        "hp": 80,
        "speed": 60,
        "attacks": [
            {"name": "Ember", "min_damage": 40,
                "max_damage": 50, "multi_hit": False},
            {"name": "Quick Attack", "min_damage": 10,
                "max_damage": 15, "multi_hit": True}
        ]
    },
    "Bulbasaur": {
        "name": "Bulbasaur",
        "type": "Grass",
        "hp": 130,
        "speed": 40,
        "attacks": [
            {"name": "Vine Whip", "min_damage": 30,
                "max_damage": 45, "multi_hit": False},
            {"name": "Tackle", "min_damage": 5, "max_damage": 20, "multi_hit": True}
        ]
    },
    "Eevee": {
        "name": "Eevee",
        "type": "Normal",
        "hp": 100,
        "speed": 100,
        "attacks": [
            {"name": "Tackle", "min_damage": 20,
                "max_damage": 35, "multi_hit": False},
            {"name": "Quick Attack", "min_damage": 10,
                "max_damage": 15, "multi_hit": True}
        ]
    },
    "Gengar": {
        "name": "Gengar",
        "type": "Ghost",
        "hp": 70,
        "speed": 120,
        "attacks": [
            {"name": "Shadow Ball", "min_damage": 50,
                "max_damage": 65, "multi_hit": False},
            {"name": "Quick Attack", "min_damage": 20,
                "max_damage": 40, "multi_hit": True}
        ]
    },
    "Blissey": {
        "name": "Blissey",
        "type": "Normal",
        "hp": 250,
        "speed": 30,
        "attacks": [
            {"name": "Dazzling Gleam", "min_damage": 20,
                "max_damage": 30, "multi_hit": False},
            {"name": "Quick Attack", "min_damage": 10,
                "max_damage": 20, "multi_hit": True}
        ]
    },
    "Fearow": {
        "name": "Fearow",
        "type": "Flying",
        "hp": 91,
        "speed": 130,
        "attacks": [
            {"name": "Aerial Ace", "min_damage": 40,
                "max_damage": 50, "multi_hit": False},
            {"name": "Quick Attack", "min_damage": 10,
                "max_damage": 15, "multi_hit": True}
        ]
    }
}

type_chart = {
    "electric": {
        "strong_against": ["water", "flying"],
        "weak_against": ["ground"],
    },
    "fire": {
        "strong_against": ["grass"],
        "weak_against": ["water"],
    },
    "water": {
        "strong_against": ["fire"],
        "weak_against": ["grass"],
    },
    "normal": {
        "strong_against": [],
        "weak_against": ["normal"],
    },
    "flying": {
        "strong_against": ["grass"],
        "weak_against": ["electric"],
    },
    "ghost": {
        "strong_against": ["normal"],
        "weak_against": ["ghost"],
    },
}


def calculate_damage(pokemon, attack_name):
    attack = None
    for atk in pokemon['attacks']:
        if atk['name'] == attack_name:
            attack = atk
            break

    if attack is None:
        return 0

    # Generate random damage between min_damage and max_damage
    damage = random.randint(attack['min_damage'], attack['max_damage'])

    # If it's a multi-hit attack, repeat it a random number of times (between 2 and 5)
    if attack['multi_hit']:
        multi_hit_count = random.randint(2, 5)
        total_damage = sum(random.randint(
            attack['min_damage'], attack['max_damage']) for _ in range(multi_hit_count))
        return total_damage
    else:
        return damage

    # Voorbeeld van hoe het werkt:
    pikachu = pokemon_dict["Pikachu"]
    damage = calculate_damage(pikachu, "Quick Attack")
    print(f"Damage: {damage}")
