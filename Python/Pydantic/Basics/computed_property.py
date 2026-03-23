from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price : float
    quantity: int
    @computed_field
    @property
    def total_price(self)-> float:
        return self.price * self.quantity

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float
    @computed_field
    @property
    def total_amt(self) -> float:
        return self.nights * self.rate_per_night
booking = Booking(
    user_id=123,
    room_id=11,
    nights=1,
    rate_per_night=450
)

print(booking.total_amt)
print(booking.model_dump())