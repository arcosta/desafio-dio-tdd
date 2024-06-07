from bson import Decimal128
from decimal import Decimal
from pydantic import Field, AfterValidator
from typing import Optional, Annotated


from tdd_project.store.schemas.base import BaseSchemaMixin, OutMixin


class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin): ...


class ProductOut(ProductIn, OutMixin): ...


def convert_decimal_128(value):
    return Decimal128(str(value))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal_] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductOut): ...
