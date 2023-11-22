from colorama import Fore, Back, Style
import os

stock_level = {
    "green banana": {"stock": 10, "price": 50},
    "yellow banana": {"stock": 5, "price": 45},
    "spotted banana": {"stock": 17, "price": 35},
    "brown banana": {"stock": 3, "price": 10},
    "banana-shaped chocolate": {"stock": 15, "price": 25}
}
stock_count = 50
unhealthy_sale = False


def delivery(*items):
    global stock_level, stock_count
    item_to_add = []
    if not items:
        print("No items to deliver")
        while True:
            choice = input("Please enter the item to deliver: ")
            if choice in stock_level:
                print(f"Adding {choice} to delivery")
            else:
                print("Sorry, we do not stock that item")
            item_to_add.append(choice)
            cont = input("Do you want to add another item? (y/n): ")
            if cont.lower() == "n":
                break
            elif cont.lower() == "y":
                continue
            else:
                print(f"{Back.RED}That is not a valid option{Back.RESET}")
    else:
        for x in items:
            item_to_add.append(x)
        print(f"Adding {item_to_add} to delivery")
    for item in item_to_add:
        if item in stock_level:
            stock_level[item]["stock"] += 1
            stock_count += 1
    print("Delivery complete")
    print(f"{stock_count} items in stock.")
    input("Press ENTER to continue")
    os.system("cls" if os.name == "nt" else "clear")

def print_stock():
    print("Current stock:")
    for items in stock_level:
        new_price = stock_level[items]["price"]
        stock = stock_level[items]['stock']
        price = stock_level[items]['price']
        total_price = stock * price
        stock_low = ""
        if stock < 5:
            stock_low = f"{Back.YELLOW}warning:{Back.RESET}{Fore.RED}Stock Low{Fore.RESET}:     "
        print(f"{stock_low}{stock} {items} at {price}p each.      {Fore.YELLOW}Total Price: {total_price}p{Style.RESET_ALL}")
    input("Press ENTER to continue")
    os.system("cls" if os.name == "nt" else "clear")


def sell_item(item):
    global stock_level, stock_count, unhealthy_sale
    if item == "banana-shaped chocolate":
        unhealthy_sale = True
    else:
        unhealthy_sale = False
    stock_level[item]["stock"] = stock_level[item]["stock"] - 1
    stock_count = stock_count -1
    print(f"{Fore.YELLOW} there are now {stock_level[item]['stock']} {item} left in stock{Style.RESET_ALL}")
    input("Press ENTER to continue")
    os.system("cls" if os.name == "nt" else "clear")

if unhealthy_sale:
    print(f"{Back.RED}{Fore.RED}warning:{Back.RESET} unhealthy sale made{Style.RESET_ALL}")

def user_interface():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to the banana shop kiosk.")
    print("Please choose from the following options:")
    print("1. Check Stock")
    print("2. Sell Item")
    print("3. Delivery")
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("That is not a valid option")
    os.system("cls" if os.name == "nt" else "clear")
    if choice == 1:
        ui.stock()
    elif choice == 2:
        ui.sell()
    elif choice == 3:
        ui.delivery()
    else:
        print(f"{Back.RED}That is not a valid option{Back.RESET}")

class ui:
    def stock():
        print_stock()
    def sell():
        sale = False
        total_cost = 0
        while not sale:
            item = input(f"Please enter the item to sell: {Fore.YELLOW}")
            if item in stock_level:
                if stock_level[item]["stock"] > 0:
                    total_cost += stock_level[item]["price"]
                    sell_item(item)
                else:
                    print("Sorry, we are out of stock of that item")
            else:
                print("Sorry, we do not stock that item")
            cont = input("Do you want to sell another item? (y/n): ")
            if cont == "y":
                continue
            elif cont == "n":
                sale = True
            else:
                print(f"{Back.RED}That is not a valid option{Back.RESET}")
    def delivery():
        delivery()

# Do not edit below this line #


while True:
    user_interface()
