from numpy.ma.mrecords import mrecarray

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cf_maker = CoffeeMaker()
mny_mach = MoneyMachine()

end_session = False

while not end_session:
    name_of_order = input(f"What would you like? ({menu.get_items()}): ")
    if name_of_order == "off":
        end_session = True
    elif name_of_order == "report":
        cf_maker.report()
        mny_mach.report()
    elif name_of_order in menu.get_items():
        order = menu.find_drink(name_of_order)
        if cf_maker.is_resource_sufficient(order):
            if mny_mach.make_payment(order.cost):
                cf_maker.make_coffee(order)
            else:
                print("Not enough coins!")
        else:
            print("Not enough resources.")
    else:
        print("Not a valid input")

