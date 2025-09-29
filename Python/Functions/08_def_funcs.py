def phone_color(color= "white"):
    """Return the color of the phone"""
    return color

print(phone_color.__doc__) #returns the enclosed string inside a func
print(phone_color.__name__) # returns the name of the method


# example of a new built method by a user
def generate_bill(units =2):
    """
    calculates the total bill for the phone
    :param unit: Number of phone units bought
    : return: Total bill amount 
    """
    total = units*80000
    print(generate_bill.__doc__)
    print (total, " , Thank you for the order")

generate_bill()

