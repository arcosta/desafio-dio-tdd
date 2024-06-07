from motor.motor_asyncio import AsyncIOMotorClient

from tdd_project.store.core.config import settings


class MongoClient:
    def __init__(self):
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    def get(self) -> AsyncIOMotorClient:
        return self.client


db_mongo = MongoClient()
