class Chaicup:
    size = 150
    def describe(self):
        return f"A {self.size}ml of chai cup"
cup=Chaicup()
print(cup.describe())
cup_two = Chaicup()

cup_two.size= 90 #ml
print(Chaicup.describe(cup_two))