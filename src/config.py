WIDTH = 600
HEIGHT = 400

COLOR_DEFINITIONS = {
    "grey": (35, 35, 40),
    "light_grey": (70, 70, 90),
    "white": (255, 248, 240),
    "red": (239, 71, 111),
    "blue": (17, 138, 178)
}

COLORS = {
    "background": COLOR_DEFINITIONS["grey"],
    "healthy": COLOR_DEFINITIONS["white"],
    "infected": COLOR_DEFINITIONS["red"],
    "immune": COLOR_DEFINITIONS["blue"],
    "dead": COLOR_DEFINITIONS["grey"],
}

PANDEMIC_PARAMETERS = {
    "n_people": 1500,
    "size": 2,
    "speed": 0.01,
    "infect_dist": 5,
    "recover_time": 1000,
    "immune_time": 3000,
    "prob_catch": 0.1,
    "prob_death": 0.0001
}
