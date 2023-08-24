from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
machine = True

while machine:
    print("Welcome to the coffee machine!")
    choice = input(f"What would you like to have? {menu.get_items()} ").lower()

    if choice == "report":
        print(coffee_maker.report())
    else:
        drink = menu.find_drink(choice)
        print(drink.cost)
        if coffee_maker.is_resource_sufficient(drink):
            cost = money_machine.process_coins()
            if cost > drink.cost:
                print(f"Here's your return!{(cost-drink.cost).__round__(2)}")
                coffee_maker.make_coffee(drink)
                machine = input("Would you like to have more coffee?")
                if machine == "no":
                    print("Machine Turning off....")
        else:
            print("Resources insufficient!😞 Machine Turning off....")
            machine = False
