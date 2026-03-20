def process_order(item , quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total Cost of tea is {cost}")
    except KeyError:
        print("Sorry that chai is not on Menu")
    except TypeError:
        print("Quantity must be a number")

# process_order("ginger", 2)
process_order("ginger", "two")
