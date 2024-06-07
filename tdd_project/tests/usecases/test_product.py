import pytest
from uuid import UUID
from tdd_project.store.usecases.product import product_usecase
from tdd_project.store.schemas.product import ProductOut, ProductUpdateOut
from tdd_project.store.core.exceptions import NotFoundException


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "arroz branco"


async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "arroz branco"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("61688afb-117f-4fc2-8371-bd56aff269ec"))

    assert (
        err.value.message
        == "Product not found with filter: 61688afb-117f-4fc2-8371-bd56aff269ec"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success():
    # TODO: implementar query com parametros
    result = await product_usecase.query()

    assert isinstance(result, list)
    assert len(result) > 1


async def test_usecases_update_should_return_success(product_up, product_inserted):
    product_up.price = 1.6
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("61688afb-117f-4fc2-8371-bd56aff269ec"))

    assert (
        err.value.message
        == "Cant delete product with filter: 61688afb-117f-4fc2-8371-bd56aff269ec"
    )
