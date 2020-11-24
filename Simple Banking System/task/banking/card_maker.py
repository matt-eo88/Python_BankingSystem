from random import randint


def generate_card():
    card_number = "400000"
    for _ in range(10):
        n = randint(0, 9)
        card_number += str(n)
    return card_number


def generate_pin():
    pin = ""
    for _ in range(4):
        pin += str(randint(0, 9))
    return pin
