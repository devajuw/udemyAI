#Method Resolution Order
class A:
    label = "A:base Class"
class B(A):
    label = "B: Masala Blend"
class C(A):
    label = "C: Herbal Blend"
class D(B,C): #If its class D(C,B)... the output would be C instead
    pass
cup = D()
print(cup.label)