def chai_cust():
    print("What chai would you like today ?")
    order = yield
    while True:
        print(f"Prepping {order}")
        order = yield
stall = chai_cust()
next(stall) #Start Generator
stall.send("Masala Chai")
stall.send("Sunny Chai")