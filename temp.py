class AppleBasket():
    apple_quantity = 0
    def __init__(self, ac, aq):
        self.apple_color = ac
        self.apple_quantity = aq
    def increase(self):
        self.apple_quantity += 1
    def __str__(self):
        print(f"A basket of {self.apple_quantity} {self.apple_color} apples.")

        
a1 = AppleBasket("red", 1)
a1.increase()
print(a1)