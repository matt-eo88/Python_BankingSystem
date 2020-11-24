class Card:

    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
        self.balance = 0

    def get_number(self):
        return self.number

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance
