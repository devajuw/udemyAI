class ChaiOrder:
    def __init__(self,type_,size):
        self.type= type_
        self.size= size
    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 90)
print(order.summary())
order_two = ChaiOrder("Lemon", 80)
print(order_two.summary())