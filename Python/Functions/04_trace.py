def add_vat(price, vat_rate):
    return price * (100+vat_rate)/100
orders = [100, 90, 800]

for price in orders:
    final_amount = add_vat(price, 20)
    print(f"Original Price: {price}, price post tax: {final_amount}")