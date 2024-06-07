import asyncio
import pytest
from uuid import UUID
from httpx import AsyncClient, ASGITransport

from tdd_project.store.db.mongo import db_mongo
from tdd_project.store.schemas.product import ProductIn, ProductUpdate, ProductOut
from tdd_project.store.usecases.product import product_usecase
from tdd_project.tests.factories import product_data, products_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_mongo.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collection_names = await mongo_client.get_database().list_collection_names()
    for collection in collection_names:
        if collection.startswith("system"):
            continue
        await mongo_client.get_database()[collection].delete_many({})


@pytest.fixture
def product_id() -> UUID:
    return UUID("d41fe178-c903-4414-b8c3-21a0ffc9a0bf")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def products_in():
    return [ProductIn(**product) for product in products_data()]


@pytest.fixture
def product_up(product_id):
    return ProductUpdate(**product_data(), id=product_id)


@pytest.fixture
async def product_inserted(product_in) -> ProductOut:
    return await product_usecase.create(body=product_in)


@pytest.fixture
async def products_inserted(products_in):
    return [await product_usecase.create(body=product_in) for product_in in products_in]


@pytest.fixture
async def client() -> AsyncClient:
    from tdd_project.store.main import app

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    return "/products/"
