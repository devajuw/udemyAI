# file = open("order.txt", "w")
# try:
#     file.write("I have wriiten this")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("Hello World is boring af")