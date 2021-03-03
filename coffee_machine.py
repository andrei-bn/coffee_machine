class CoffeeMachine:
    coffee = [['espresso', 250, 0, 16, 1, 4],
                   ['latte', 350, 75, 20, 1, 7],
                   ['cappuccino', 200, 100, 12, 1, 6]]

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def state_machine(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'{self.money} of money')
        print()

    def buy_coffee(self, type_):
        # data coffee[type, water, milk, beans, glass, money]
        self.water -= self.coffee[int(type_) - 1][1]
        self.milk -= self.coffee[int(type_) - 1][2]
        self.coffee_beans -= self.coffee[int(type_) - 1][3]
        self.disposable_cups -= self.coffee[int(type_) - 1][4]
        self.money += self.coffee[int(type_) - 1][5]

    def fill_coffee_machine(self):
        self.water += int(input("Write how many ml of water the coffee machine has: "))
        self.milk += int(input("Write how many ml of water the coffee machine has: "))
        self.coffee_beans += int(input("Write how many grams of coffee beans the coffee machine has: "))
        self.disposable_cups += int(input("Write how many cups of coffee you will need: "))

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def check_cooking_coffee(self, type_):
        sorry = 'Sorry, not enough '
        if self.water - self.coffee[int(type_) - 1][1] < 0:
            return sorry + 'water!'
        elif self.milk - self.coffee[int(type_) - 1][2] < 0:
            return sorry + 'milk!'
        elif self.coffee_beans - self.coffee[int(type_) - 1][3] < 0:
            return sorry + 'coffee beans!'
        elif self.disposable_cups - self.coffee[int(type_) - 1][4] < 0:
            return sorry + 'disposable cups!'
        else:
            return ''


def main():
    obj = CoffeeMachine()
    while True:
        action = input('Write action (buy, fill, take, remaining, exit): ')
        if action == 'buy':
            type_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, '
                                '3 - cappuccino, back - to main menu: ')
            if type_coffee == 'back':
                continue
            else:
                res_check = obj.check_cooking_coffee(type_coffee)
                if res_check == '':
                    obj.buy_coffee(type_coffee)
                    print('I have enough resources, making you a coffee!')
                else:
                    print(res_check)
        elif action == 'fill':
            obj.fill_coffee_machine()
        elif action == 'take':
            obj.take_money()
        elif action == 'remaining':
            print()
            obj.state_machine()
        elif action == 'exit':
            break


main()
