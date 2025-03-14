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

}
