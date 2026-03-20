class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala":20, "ginger": 67}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an Integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} of {flavor} chai: {total} rupees")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank you for visiting chaicode")

bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)