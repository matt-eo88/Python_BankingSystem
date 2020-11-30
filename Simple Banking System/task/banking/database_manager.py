import _sqlite3
from card import Card


class DatabaseManager:

    def __init__(self):
        self.conn = _sqlite3.connect("card.s3db")
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS card(
        id INTEGER NOT NULL PRIMARY KEY,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0)""")
        self.conn.commit()

    def insert(self, card):  # change parameters
        number = card.get_number()
        pin = card.get_pin()
        balance = card.get_balance()
        query = """
        INSERT INTO card(number, pin, balance)
        VALUES({}, {}, {})""".format(number, pin, balance)
        self.cur.execute(query)
        self.conn.commit()

    def is_card(self, number, pin):
        query = """
        SELECT number, pin FROM card
        WHERE number = {} AND pin = {}""".format(number, pin)
        self.cur.execute(query)
        self.conn.commit()
        result = self.cur.fetchone()
        if result is None:
            return False
        if result[0] == number and result[1] == pin:
            return True

    def get_card(self, number, pin):
        query = """
                SELECT number, pin, balance FROM card
                WHERE number = {} AND pin = {}""".format(number, pin)
        self.cur.execute(query)
        self.conn.commit()
        result = self.cur.fetchone()
        card = Card(result[0], result[1])
        card.set_balance(result[2])
        return card
