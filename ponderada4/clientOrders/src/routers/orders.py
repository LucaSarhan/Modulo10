# src/routers/orders.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.orders import Order as OrderSchema
from services.orders import OrderService
from databases import database
import logging

LOGGER = logging.getLogger(__name__)

router = APIRouter(
    prefix="/clientOrders",
    tags=["clientOrders"],
)

@router.get("/orders/{order_id}")
async def get_order(order_id: int, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders/{order_id}", "order_id": order_id, "method": "GET"})
    orderService = OrderService(db)
    return orderService.get(order_id)

@router.get("/orders")
async def get_orders(db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders", "method": "GET"})
    orderService = OrderService(db)
    return orderService.get_all()

@router.post("/orders")
async def create_order(order: OrderSchema, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders", "method": "POST", "order": order.dict()})
    orderService = OrderService(db)
    return orderService.add(order=order)

@router.put("/orders/{order_id}")
async def update_order(order_id: int, order: OrderSchema, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders/{order_id}", "method": "PUT", "order_id": order_id, "order": order.dict()})
    orderService = OrderService(db)
    return orderService.update(order_id, order=order)

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int, db: Session = Depends(database.get_db)):
    LOGGER.info({"message": "Acessando a rota /orders/{order_id}", "method": "DELETE", "order_id": order_id})
    orderService = OrderService(db)
    return orderService.delete(order_id)