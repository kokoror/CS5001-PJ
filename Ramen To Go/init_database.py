# initiate the database
import pandas as pd

item_database = {'item_name':['Tonkotsu Ramen', 'Mazesoba', 'Chicken Ramen', 'Shoyu Ramen', 'Assorted Sushi',
                              'Miso Soup', 'Tempura', 'Mochi Ice cream', 'Cup noodle #1', 'Cup noodle #2',
                              'Cup noodle #3', 'Cup noodle #4'],
                 'price': [8, 9, 7, 8, 5, 2, 4, 3, 2, 2, 2, 2],
                 'inventory': [20] * 12}

db = pd.DataFrame(item_database)

db.to_csv('database.csv', index=False)
