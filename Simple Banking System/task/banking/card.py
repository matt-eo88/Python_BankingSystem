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

    def set_balance(self, balance):
        self.balance = balance

    def add_balance(self, balance):
        self.balance += balance

    def take_balance(self, balance):
        self.balance -= balance
