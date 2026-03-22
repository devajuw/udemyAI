from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True
product_one = Product(id =1, name="laptop", price=9090, in_stock= True)
product_two = Product(id =2, name="KB", price=987)

# Error
# product_three = Product(name="Mouse") 