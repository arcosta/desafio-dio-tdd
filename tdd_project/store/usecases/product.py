from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from uuid import UUID
import pymongo

from tdd_project.store.db.mongo import db_mongo
from tdd_project.store.schemas.product import (
    ProductIn,
    ProductOut,
    ProductUpdateOut,
    ProductUpdate,
)
from tdd_project.store.core.exceptions import NotFoundException
from tdd_project.store.models.product import ProductModel


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_mongo.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())

        await self.collection.insert_one(product_model.model_dump())

        return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if result is None:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)

    async def query(self) -> list[ProductOut]:
        # breakpoint()
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        # product = ProductUpdate(**body.model_dump(exclude_none=True))

        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )
        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        result = await self.collection.delete_one({"id": id})

        if result.deleted_count > 0:
            return True
        else:
            raise NotFoundException(message=f"Cant delete product with filter: {id}")


product_usecase = ProductUsecase()
