class TeaLeaf:
    def __init__(Self, age):
        Self.age = age
    @property
    def age(Self):
        return Self._age + 2
    @age.setter
    def age(Self, age):
        if 1 <= age <= 5:
            Self._age = age
        else:
            raise ValueError(" Tea Leaves must be between 1 and 5 ")
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 6 #error coz of conditional above
print(leaf.age)