class Chai:
    temp = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temp)

cutting.temp = "mild"
cutting.cup = "small"
print("after changing", cutting.temp )
print("cup size is ", cutting.cup )
print("Direct look into class ", Chai.temp )

# del cutting.cup 
# no fall back hence error
del cutting.temp
print(cutting.cup)
print(cutting.temp)