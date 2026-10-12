class Mobile:

    def __init__(self, brand1, price1):
        self.brand = brand1
        self.price = price1

    def geta(self):
        return self.brand

    def seta(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Brand : {self.brand} Price : {self.price}")


class Smartphone(Mobile):

    def __init__(self, brand, price, camera):
        super().__init__(brand, price)
        self.camera = camera

    def geta(self):
        return self.camera

    def seta(self, newcamera):
        self.camera = newcamera

    def display(self):
        super().display()
        print(f"Camera : {self.camera}")


m1 = Mobile("Nokia", 5000)
s1 = Smartphone("Samsung", 25000, "50 MP")

m1.display()
s1.display()