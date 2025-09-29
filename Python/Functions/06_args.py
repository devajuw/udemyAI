#Args & kwargs
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("extras", extras)
special_chai("Cinnamon", "Cardamom", Sweetener = "Honey", foam= "yes")


# HANDLING MULTIPLE returns EXAMPLE
def chai():
    return 60, 70 ,78
sold, remaining, _ = chai() # _ was used to just avoid error and maybe store a value that wont be used later
print("sold", sold)
print("remaining", remaining)