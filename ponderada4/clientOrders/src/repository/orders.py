# src/repository/produtos.py

from models.orders import Order
from sqlalchemy.orm import Session
from datetime import datetime

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, order_id):
        return self.db.query(Order).get(order_id)

    def get_all(self):
        return self.db.query(Order).all()

    def add(self, order: Order):
        order.id = None
        order.data_criacao = datetime.now()
        self.db.add(order)
        self.db.flush()
        self.db.commit()
        return {"message": "Ordem cadastrada com sucesso"}

    def update(self, order_id, order):
        orderdb = self.db.query(Order).filter(Order.id == order_id).first()
        if orderdb is None:
            return {"message": "Ordem não encontrada"}
        order.data_modificacao = datetime.now()
        order = order.__dict__
        order.pop("_sa_instance_state")
        order.pop("data_criacao")
        order.pop("id")
        self.db.query(Order).filter(Order.id == order_id).update(order)
        self.db.flush()
        self.db.commit()
        return {"message": "Ordem finalizada com sucesso"}

    def delete(self, order_id):
        orderdb = self.db.query(Order).filter(Order.id == order_id).first()
        if orderdb is None:
            return {"message": "ordem não encontrada"}
        self.db.query(Order).filter(Order.id == order_id).delete()
        self.db.flush()
        self.db.commit()
        return {"message": "Ordem deletada com sucesso"}