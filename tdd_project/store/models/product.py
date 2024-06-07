from tdd_project.store.models.base import CreateBaseModel
from tdd_project.store.schemas.product import ProductIn


class ProductModel(CreateBaseModel, ProductIn): ...
