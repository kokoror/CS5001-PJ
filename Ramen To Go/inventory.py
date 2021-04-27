import pandas as pd

# add exception handling for reading file
try:
    item_db = pd.read_csv('database.csv')
except FileNotFoundError:
    print('File not found.')

class Inventory:
    # init the inventory: read from csv file
    def __init__(self):
        self.item_name = item_db.item_name
        self.stocks = item_db.inventory
        self.price = item_db.price

    # evaluate if stock is sufficient
    def stock_sufficient(self, order_amount, item_num):
        """Returns True when order can be made, False if stocks are insufficient."""
        can_make = True
        if order_amount[item_num] + 1 > self.stocks[item_num]:
            can_make = False
        return can_make

    def process_order(self, order_list):
        """Deducts the number of orders from the stock."""
        try:
            for i in range(len(order_list)):
                self.stocks[i] -= order_list[i]
            item_db['inventory'] = self.stocks
            item_db.to_csv('database.csv', index=False)
        except:
            print('something went wrong')

