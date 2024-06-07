from fastapi import APIRouter
from tdd_project.store.controllers.product import router as product
from tdd_project.store.controllers.health import router as health

api_router = APIRouter()

api_router.include_router(product, prefix="/products")
api_router.include_router(health, prefix="/health")
