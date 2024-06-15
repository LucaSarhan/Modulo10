# src/services/orders.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from repository.orders import OrderRepository
from models.orders import Order
from schemas.orders import Order as OrderSchema

class OrderService:
    def __init__(self, db: Session):
        self.repository = OrderRepository(db)

    def get(self, order_id):
        order = self.repository.get(order_id)
        if order is None:
            raise HTTPException(status_code=404, detail="Ordem não encontrada")
        return order

    def get_all(self):
        return self.repository.get_all()

    def add(self, order : OrderSchema):
        order = Order(**order.dict())
        return self.repository.add(order)

    def update(self, order_id, order : OrderSchema):
        order = Order(**order.dict())
        return self.repository.update(order_id, order)

    def delete(self, order_id):
        return self.repository.delete(order_id)