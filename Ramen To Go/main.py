from tkinter import *
import time
from money import MoneyMachine
from inventory import Inventory

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# init charges and balance to be 0
CHARGES = 0
BALANCE = 0
# init order amount for all 12 items
ORDER_AMOUNT = [0] * 12

# create instance of classes
inventory = Inventory()
money_machine = MoneyMachine()

# import item names
ITEMS = inventory.item_name
# import prices
PRICE = inventory.price
# import stocks
INVENTORY = inventory.stocks

# initialize the window
window = Tk()
window.title("Ramen To Go")
window.config(padx=60, pady=60, bg=YELLOW)

# function to add order and charge
def select(item_num):
    global ORDER_AMOUNT
    global CHARGES
    if inventory.stock_sufficient(ORDER_AMOUNT, item_num):
        ORDER_AMOUNT[item_num] += 1
        CHARGES += PRICE[item_num]
        charge_label.config(text=f'Total Charge: ${CHARGES}')
        my_order()
    else:
        canvas_message.itemconfig(message, text=f'Sorry, {ITEMS[item_num]} is currently\nout of stock.'
                                                f'We will stock up ASAP!')

def select_button_rm1():
    select(0)

def select_button_rm2():
    select(1)

def select_button_rm3():
    select(2)

def select_button_rm4():
    select(3)

def select_button_su():
    select(4)

def select_button_ms():
    select(5)

def select_button_tpr():
    select(6)

def select_button_ic():
    select(7)

def select_button_cn1():
    select(8)

def select_button_cn2():
    select(9)

def select_button_cn3():
    select(10)

def select_button_cn4():
    select(11)


#function to show my orders
def my_order():
    order_text = "Your orders:"
    for i in range(len(ORDER_AMOUNT)):
        if ORDER_AMOUNT[i] != 0:
            order_text += f"\n{ITEMS[i]} x {ORDER_AMOUNT[i]}" + f"      ${ORDER_AMOUNT[i] * PRICE[i]} "
    canvas_message.itemconfig(message, text=order_text)


# function to clear all the orders and charges
def clear_order():
    global ORDER_AMOUNT
    global CHARGES
    ORDER_AMOUNT = [0] * 12
    CHARGES = 0
    canvas_message.itemconfig(message, text='Message box:\nGood day!\nPlease select your orders.')
    charge_label.config(text=f'Total Charge: ${CHARGES}')


# function to insert coins
def insert_coin():
    try:
        global BALANCE
        BALANCE += float(insert_entry.get())
        balance_label.config(text=f'Balance: ${BALANCE}')
        insert_entry.delete(0, END)
    except ValueError as ex:
        canvas_message.itemconfig(message, text='Please insert a real coin :)')
        insert_entry.delete(0, END)


# function to pay and process orders
def pay_button():
    global BALANCE, CHARGES, ORDER_AMOUNT
    money_machine.receive_money(BALANCE)
    if CHARGES != 0 and BALANCE != 0:
        if money_machine.make_payment(CHARGES):
            inventory.process_order(ORDER_AMOUNT)
            canvas_message.itemconfig(message, text=f"Order is being processed.\n"
                                                    f"You inserted {money_machine.CURRENCY}{BALANCE}.\n"
                                                    f"Total charge {money_machine.CURRENCY}{CHARGES}.\n"
                                                    f"Here is {money_machine.CURRENCY}{money_machine.change} in change.\n"
                                                    f"Great choice!\n"
                                                    f"Enjoy your delicious meal!")
        else:
            canvas_message.itemconfig(message, text=f"Sorry that's not enough money.\n"
                                                    f"You inserted {money_machine.CURRENCY}{BALANCE}.\n"
                                                    f"Total charge {money_machine.CURRENCY}{CHARGES}.\n"
                                                    f"{money_machine.CURRENCY}{money_machine.change} refunded.")
        BALANCE, CHARGES = 0, 0
        ORDER_AMOUNT = [0] * 12
        balance_label.config(text=f'Balance: ${BALANCE}')
        charge_label.config(text=f'Total Charge: ${CHARGES}')
    elif CHARGES == 0:
        canvas_message.itemconfig(message, text="Please select your orders.")
    elif BALANCE == 0:
        canvas_message.itemconfig(message, text="Please insert coins.")


# User interface section!
# create canvas. buttons and display window

# ramen window
canvas_ramen = Canvas(width=500, height=110, bg='white', highlightthickness=0)
rm_img_1 = PhotoImage(file='rm1.png')
canvas_ramen.create_image(70, 50, image=rm_img_1) # coordinate of top left coner is 0,0
rm_img_2 = PhotoImage(file='rm2.png')
canvas_ramen.create_image(190, 50, image=rm_img_2)
rm_img_3 = PhotoImage(file='rm3.png')
canvas_ramen.create_image(310, 50, image=rm_img_3)
rm_img_4 = PhotoImage(file='rm4.png')
canvas_ramen.create_image(430, 50, image=rm_img_4)
canvas_ramen.grid(column=0, row=0, columnspan=12, rowspan=2)

# ramen select button
select_button_rm1=Button(text=f'${PRICE[0]} Select', font=(FONT_NAME, 15), command=select_button_rm1, highlightthickness=0, padx=6, pady=6)
select_button_rm1.grid(column=1, row=2)
select_button_rm2=Button(text=f'${PRICE[1]} Select', font=(FONT_NAME, 15), command=select_button_rm2, highlightthickness=0, padx=6, pady=6)
select_button_rm2.grid(column=4, row=2)
select_button_rm3=Button(text=f'${PRICE[2]} Select', font=(FONT_NAME, 15), command=select_button_rm3, highlightthickness=0, padx=6, pady=6)
select_button_rm3.grid(column=7, row=2)
select_button_rm4=Button(text=f'${PRICE[3]} Select', font=(FONT_NAME, 15), command=select_button_rm4, highlightthickness=0, padx=6, pady=6)
select_button_rm4.grid(column=10, row=2)

# side window
canvas_side = Canvas(width=500, height=110, bg='white', highlightthickness=0)
su_img = PhotoImage(file='sh.png')
canvas_side.create_image(70, 50, image=su_img) # coordinate of top left coner is 0,0
ms_img = PhotoImage(file='ms.png')
canvas_side.create_image(190, 50, image=ms_img)
tpr_img = PhotoImage(file='tpr.png')
canvas_side.create_image(310, 50, image=tpr_img)
ic_img = PhotoImage(file='ic.png')
canvas_side.create_image(430, 50, image=ic_img)
canvas_side.grid(column=0, row=3, columnspan=12, rowspan=2)

# side select
select_button_su = Button(text=f'${PRICE[4]} Select', font=(FONT_NAME, 15), command=select_button_su, highlightthickness=0, padx=6, pady=6)
select_button_su.grid(column=1, row=5)
select_button_ms = Button(text=f'${PRICE[5]} Select', font=(FONT_NAME, 15), command=select_button_ms, highlightthickness=0, padx=6, pady=6)
select_button_ms.grid(column=4, row=5)
select_button_tpr = Button(text=f'${PRICE[6]} Select', font=(FONT_NAME, 15), command=select_button_tpr, highlightthickness=0, padx=6, pady=6)
select_button_tpr.grid(column=7, row=5)
select_button_ic = Button(text=f'${PRICE[7]} Select', font=(FONT_NAME, 15), command=select_button_ic, highlightthickness=0, padx=6, pady=6)
select_button_ic.grid(column=10, row=5)

# cup noodle window
canvas_cn = Canvas(width=500, height=110, bg='white', highlightthickness=0)
cn_img_1 = PhotoImage(file='cn1.png')
canvas_cn.create_image(70, 50, image=cn_img_1) # coordinate of top left coner is 0,0
cn_img_2 = PhotoImage(file='cn2.png')
canvas_cn.create_image(190, 50, image=cn_img_2)
cn_img_3 = PhotoImage(file='cn3.png')
canvas_cn.create_image(310, 50, image=cn_img_3)
cn_img_4 = PhotoImage(file='cn4.png')
canvas_cn.create_image(430, 50, image=cn_img_4)
canvas_cn.grid(column=0, row=6, columnspan=12, rowspan=2)

# cup noodle select button
select_button_cn1=Button(text=f'${PRICE[8]} Select', font=(FONT_NAME, 15), command=select_button_cn1, highlightthickness=0, padx=6, pady=6)
select_button_cn1.grid(column=1, row=8)
select_button_cn2=Button(text=f'${PRICE[9]} Select', font=(FONT_NAME, 15), command=select_button_cn2, highlightthickness=0, padx=6, pady=6)
select_button_cn2.grid(column=4, row=8)
select_button_cn3=Button(text=f'${PRICE[10]} Select', font=(FONT_NAME, 15), command=select_button_cn3, highlightthickness=0, padx=6, pady=6)
select_button_cn3.grid(column=7, row=8)
select_button_cn4=Button(text=f'${PRICE[11]} Select', font=(FONT_NAME, 15), command=select_button_cn4, highlightthickness=0, padx=6, pady=6)
select_button_cn4.grid(column=10, row=8)

# customer operating window

canvas_shop = Canvas(width=300, height=200, bg=YELLOW, highlightthickness=0)
shop_img = PhotoImage(file='rmshop.png')
canvas_shop.create_image(160, 30, image=shop_img, )
canvas_shop.create_text(160, 100, text="Welcome to Ramen To Go!", font=(FONT_NAME, 21, 'bold'))
canvas_shop.grid(column=12, row=0, rowspan=4, columnspan=3)

# price label
charge_label=Label(text=f'Total Charge: ${CHARGES}', anchor='w', font=(FONT_NAME, 15, 'bold'), bg='white')
charge_label.grid(column=12, row=3)

balance_label=Label(text=f'Balance: ${BALANCE}', font=(FONT_NAME, 15, 'bold'), bg='white')
balance_label.grid(column=12, row=4)

# pay button
pay_button=Button(text='Pay', font=(FONT_NAME, 15), command=pay_button, highlightthickness=0)
pay_button.grid(column=14, row=3)

# coin insert area
insert_entry = Entry(width=3, font=(FONT_NAME, 15), highlightthickness=0)
insert_entry.grid(column=13, row=4)

insert_coin_button=Button(text='Insert Coin', font=(FONT_NAME, 15), command=insert_coin, highlightthickness=0)
insert_coin_button.grid(column=14, row=4)

# my order button
myorder_button=Button(text='My Order', font=(FONT_NAME, 15), command=my_order, highlightthickness=0)
myorder_button.grid(column=12, row=5)

# clear order button
clear_button=Button(text='Clear', font=(FONT_NAME, 15), command=clear_order, highlightthickness=0)
clear_button.grid(column=14, row=5)
# message box

canvas_message = Canvas(width=220, height=150, bg='white', highlightthickness=0)
message = canvas_message.create_text(0, 0, anchor='nw', text='Message box:\nHungry?🍜\n'
                                                             'You\'ve come to the right place!\n'
                                                             'Please select your order...')
canvas_message.grid(column=12, row=6, rowspan=3, columnspan=3)

window.mainloop()
