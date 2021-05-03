class Budget:
    def __init__(self, category, amount):
        self.category = ["Food", "Clothing", "Entertainment"]
        self.amount = amount

    #methods
    def deposit(self):
        amount = print(input("How much would you like to deposit?: \n"))
        return amount

    def check_balance(self):
        pass

    def withdraw(self):
        pass

    def transfer(self):
        pass

category_0 = Budget("Clothing", 1000)
category_1 = Budget("Food", 1000)
category_2 = Budget("Entertainment", 1000)

print(category_0.deposit())
print(category_0.check_balance())
print(category_0.withdraw())
