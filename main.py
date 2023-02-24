from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

################### Coffee Machine in OOP ###########################
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True


while is_on:  
  user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
  if user_choice == "off":
    is_on = False
  elif user_choice == "report":
    coffee_machine.report()
    money_machine.report()
  else:
    drink = menu.find_drink(user_choice)
    can_make_drink = coffee_machine.is_resource_sufficient(drink)
    if can_make_drink:   
      if money_machine.make_payment(drink.cost):
        coffee_machine.make_coffee(drink)