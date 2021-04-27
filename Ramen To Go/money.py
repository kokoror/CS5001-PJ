class MoneyMachine:
    def __init__(self):
        self.CURRENCY = "$"
        self.profit = 0
        self.money_received = 0
        self.change = 0

    def report(self):
        """ profit"""
        return f"Money: {self.CURRENCY}{self.profit}"

    def receive_money(self, balance):
        """update machine's balance"""
        self.money_received = balance

    def make_payment(self, price):
        """
        Returns True when payment is accepted,
        or False if insufficient.
        """
        if self.money_received >= price:
            self.change = round(self.money_received - price, 2)
            self.profit += price
            self.money_received = 0
            return True
        else:
            self.change = self.money_received
            self.money_received = 0
            return False
