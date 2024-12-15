import asyncio
from collections import Counter
from sqlalchemy.orm import Session
from .models import Purchase, Product


async def get_recommendation(user_id: int, db: Session):
    # Получаем все покупки пользователя
    user_purchases = db.query(Purchase).filter(Purchase.user_id == user_id).all()
    purchased_product_ids = {purchase.product_id for purchase in user_purchases}

    # Получаем все покупки других пользователей
    all_purchases = db.query(Purchase).all()

    # Группируем покупки по продуктам
    product_counter = Counter()

    for purchase in all_purchases:
        if purchase.user_id != user_id and purchase.product_id not in purchased_product_ids:
            product_counter[purchase.product_id] += 1

    if not product_counter:
        return None

    # Находим самый популярный продукт среди кандидатов
    recommended_product_id = product_counter.most_common(1)[0][0]

    return recommended_product_id
