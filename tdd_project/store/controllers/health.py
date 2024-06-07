from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get(path="/info")
async def get():
    return "OK"
