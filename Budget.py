class Category:
    amount = 0

    # Constructor

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # Methods
    def deposit(self, amount):
        self.amount += amount
        print("You have made a deposit of {} in {} category".format(amount, self.category))
        return "Your current balance is " + str(self.amount)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self, amount):
        if amount <= self.amount:
            return True
        else:
            return False
        # This should return a boolean if amount is less than self amount

    def withdraw(self, amount):
        if self.check_balance(amount):
            self.amount -= amount
            print("You have made a withdrawal of {} in {} category".format(amount, self.category))
            print("current_balance is " + str(self.amount))
        else:
            print("You have insufficient funds for the requested amount. Please try again")

    def transfer(self, amount, category):
        self.amount -= amount
        category.amount += amount
        print("You have made a transfer from {} to {} in the amount of {}.".format(self.category, category.category, amount))
    # transfer between 2 categories


balance_category = Category("Bank Balance", 33000)
housing_category = Category("Mortgage", 1100)
clothing_category = Category("Clothing", 270)
income_category = Category("Paycheck", 14000)
food_category = Category("Groceries", 1600)

# Deposit into Bank Balance and show new balance
print(balance_category.deposit(3700))

# Check Current Balance in housing category is more than 30000
print(housing_category.check_balance(30000))

# Withdraw from Food category
print(food_category.withdraw(115))

# Withdraw too much from housing category
print(housing_category.withdraw(1998815))

# Transfer from income to clothing
income_category.transfer(100, clothing_category)

# Transfer from income to housing
income_category.transfer(1200, housing_category)

# Transfer from bank to food
balance_category.transfer(1300, food_category)