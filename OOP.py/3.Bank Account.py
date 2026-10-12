class Bank:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance")


b1 = Bank(5000)

print(b1.get_balance())

b1.set_balance(8000)

print(b1.get_balance())