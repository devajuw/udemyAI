from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code:str
class User(BaseModel):
    id: int
    name: str
    address: Address
address = Address(
    street='123',
    city= "Godda",
    postal_code="814133"
)

user_data = {
    "id": 1,
    "name": "Dev",
    "address": {
        "street": "321 something",
        "city": "Paris",
        "postal_code": "343453"
    }
}
user = User(**user_data)
print(user)