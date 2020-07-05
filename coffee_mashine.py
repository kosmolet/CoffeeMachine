class CoffeeMachine:
	
 	def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.run = True

    def run_machine(self):
        while self.run:
            self.selection(input("Write action (buy, fill, take, remaining, exit):"))

    def status(self):
        print()
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")
        print()

    def take(self):
        global money
        print("I Gave you $" + str(self.money))
        self.money = 0
        print()

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        print()

    def buy(self, option):
        choice = int(option)
        if choice == 1:
            if self.water - 250 > 0:
                if self.coffee - 16 > 0:
                    if self.cups - 1 > 0:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 250
                        self.coffee -= 16
                        self.cups -= 1
                        self.money += 4
                    else:
                        print("Sorry, not enough cups!")
                else:
                    print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough water!")

        if choice == 2:
            if self.water - 350 > 0:
                if self.milk - 75 > 0:
                    if self.coffee - 20 > 0:
                        if self.cups - 1 > 0:
                            print("I have enough resources, making you a coffee!")
                            self.water -= 350
                            self.milk -= 75
                            self.coffee -= 20
                            self.cups -= 1
                            self.money += 7
                        else:
                            print("Sorry, not enough cups!")
                    else:
                        print("Sorry, not enough coffee beans!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough water!")

        if choice == 3:
            if self.water - 200 > 0:
                if self.milk - 100 > 0:
                    if self.coffee - 12 > 0:
                        if self.cups - 1 > 0:
                            print("I have enough resources, making you a coffee!")
                            self.water -= 200
                            self.milk -= 100
                            self.coffee -= 12
                            self.cups -= 1
                            self.money += 6
                        else:
                            print("Sorry, not enough cups!")
                    else:
                        print("Sorry, not enough coffee beans!")
                else:
                    print("Sorry, not enough milk!")
            else:
                print("Sorry, not enough water!")

    def quit_coffee_machine(self):
        self.run = False

    def selection(self, choice):
        if choice == 'take':
            self.take()
        elif choice == 'fill':
            self.fill()
        elif choice == 'remaining':
            self.status()
        elif choice == 'exit':
            self.quit_coffee_machine()
        elif choice == 'buy':
            option_num = input("What do you want to buy?\n"
                               "1 - espresso,\n"
                               "2 - latte,\n"
                               "3 - cappuccino,\n"
                               "back - to main menu: ")
            if option_num in ['1', '2', '3']:
                self.buy(option_num)
        else:
            print("Unknown command")


machine = CoffeeMachine()
machine.run_machine()
