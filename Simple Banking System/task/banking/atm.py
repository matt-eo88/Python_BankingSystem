from card_maker import make_luhn, generate_pin, is_luhn
from card import Card
from database_manager import DatabaseManager


class ATM:

    def __init__(self):
        self.is_on = True
        self.cards = []
        self.current_user = None
        self.data_manager = DatabaseManager()

    def start_system(self):

        while self.is_on:
            print('''
                    1. Create an account
                    2. Log into account
                    0. Exit
                    ''')
            action = input()
            if action == "1":
                self.create_card()
            elif action == "2":
                self.login()
            elif action == "0":
                self.exit()
            else:
                print("Command unknown")

    def create_card(self):
        card_number = make_luhn()
        card_pin = generate_pin()
        card = Card(card_number, card_pin)
        self.cards.append(card)
        self.data_manager.insert(card)
        print("Your card has been created")
        print("Your card number:")
        print(card.get_number())
        print("Your card pin:")
        print(card.get_pin())

    def login(self):
        print("Enter your card number:")
        n = input()
        print("Enter your pin:")
        p = input()
        if self.data_manager.is_card(n, p):
            print("You have successfully logged in!")
            self.current_user = self.data_manager.get_card(n, p)
            self.login_menu()
        else:
            print("Wrong card number or PIN!")

    def login_menu(self):
        off = False
        while not off:
            print('''
                    1. Balance
                    2. Add income
                    3. Do transfer
                    4. Close account
                    5. Log out
                    0. Exit''')
            action = input()
            if action == "1":
                print("Balance:", self.current_user.get_balance())
            elif action == "2":
                print("Enter income:")
                income = int(input())
                self.current_user.add_balance(income)
                self.data_manager.add_income(self.current_user.get_number(), income)
                print("Income was added!")
            elif action == "3":
                self.do_transfer()
            elif action == "4":
                self.data_manager.delete_account(self.current_user)
                print("The account has been closed!")
                self.reset_user()
                off = True
            elif action == "5":
                print("You have successfully logged out!")
                self.reset_user()
                off = True
            elif action == "0":
                off = True
                self.exit()

    def do_transfer(self):
        print("Transfer")
        print("Enter the card number:")
        recipient = input()
        if recipient == self.current_user.get_number():
            print("You can't transfer money to the same account!")
            return
        if not is_luhn(recipient):
            print("Probably you made a mistake in the card number. Please try again!")
            return
        if not self.data_manager.exists(recipient):
            print("Such a card does not exist.")
            return
        print("Enter how much money you want to transfer:")
        amount = int(input())
        if self.current_user.get_balance() < amount:
            print("Not enough money!")
            return
        self.data_manager.transfer(amount, recipient, self.current_user)
        self.current_user.take_balance(amount)
        print("Success!")

    def reset_user(self):
        self.current_user = None

    def exit(self):
        self.is_on = False
        print("Bye!")
