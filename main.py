from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from recommendation_system.database import SessionLocal, engine, Base
from recommendation_system.models import User, Product, Purchase
from recommendation_system.schemas import UserCreate, ProductCreate, PurchaseCreate, Recommendation
from recommendation_system.recommendations import get_recommendation
import uvicorn
import asyncio

app = FastAPI()

# Создание таблиц в БД
@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=int)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.id

@app.post("/products/", response_model=int)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product.id


@app.post("/purchases/")
async def create_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = Purchase(user_id=purchase.user_id, product_id=purchase.product_id)
    db.add(db_purchase)
    db.commit()
    return {"message": "Purchase created"}


@app.get("/recommendations/{user_id}", response_model=Recommendation)
async def recommend_product(user_id: int, db: Session = Depends(get_db)):
    recommended_product_id = await get_recommendation(user_id, db)

    if recommended_product_id is None:
        raise HTTPException(status_code=404, detail="No recommendations found")

    return Recommendation(product_id=recommended_product_id)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)