def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(2,80)
print(my_bill)
# or do this
print("Bill Amt. for the table:", calculate_bill(2, 40))