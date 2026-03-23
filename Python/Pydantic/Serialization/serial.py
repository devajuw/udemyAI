from typing import List
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address : Address
    tags: List[str] =[]

    model_config = ConfigDict(
        json_encoders = {datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user= User(
    id=1,
    name="Dev",
    email="d@dogla.com",
    createdAt=datetime(2025,3,23,13,50),
    address = Address(
        street = "random Street",
        city="Godda",
        zip_code="81412"
    ),
    is_active = False,
    tags = ["Premium", "Subscriber"]   
)

python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json() #Json str example
print("="*30)
print(json_str)
