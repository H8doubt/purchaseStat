from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str

class ProductCreate(BaseModel):
    name: str

class PurchaseCreate(BaseModel):
    user_id: int
    product_id: int

class Recommendation(BaseModel):
    product_id: int