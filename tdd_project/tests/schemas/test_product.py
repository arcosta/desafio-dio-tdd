from pydantic import ValidationError
import pytest
from uuid import UUID
from tdd_project.store.schemas.product import ProductIn
from tdd_project.tests.factories import product_data


def test_schemas_return_success():
    product = ProductIn.model_validate(product_data())

    assert product.name == "arroz branco"
    assert product.quantity == 10
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {
        "name": "arroz branco",
        "quantity": 10,
        "price": 3.50,
        #    'status': True
    }

    with pytest.raises(ValidationError) as err:
        _ = ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {
            "name": "arroz branco",
            "quantity": 10,
            "price": 3.50,
        },
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }
