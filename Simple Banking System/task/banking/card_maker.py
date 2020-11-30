from random import randint


# Creates a card of length 15
# is_luhn method will generate
# the 16th digit (checksum)
def generate_card():
    card_number = "400000"
    for _ in range(9):
        n = randint(0, 9)
        card_number += str(n)
    return card_number


def generate_pin():
    pin = ""
    for _ in range(4):
        pin += str(randint(0, 9))
    return pin


# implementation of Luhn algorithm
def make_luhn():
    card = generate_card()
    numbers = list(card)
    counter = 1
    for index, char in enumerate(numbers):
        n = int(char)
        if counter % 2 != 0:
            n *= 2
        if n > 9:
            n -= 9
        numbers[index] = str(n)
        counter += 1
    checksum = make_checksum(numbers)
    card += str(checksum)
    return card


# finds checksum
def make_checksum(numbers):
    sum_ = 0
    for n in numbers:
        x = int(n)
        sum_ += x
    # return 10 - (sum_ % 10)
    checksum = 0
    for i in range(10):
        x = sum_ + i
        if x % 10 == 0:
            checksum = i
            break

    return checksum


# Checks if the given card number
# passes the Luhn algorithm
def is_luhn(number):
    numbers = list(number)
    last = int(numbers.pop())
    counter = 1
    for index, char in enumerate(numbers):
        n = int(char)
        if counter % 2 != 0:
            n *= 2
        if n > 9:
            n -= 9
        numbers[index] = n
        counter += 1
    sum_ = 0
    for n in numbers:
        sum_ += n
    return (sum_ + last) % 10 == 0
