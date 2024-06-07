from fastapi import FastAPI
from tdd_project.store.core.config import settings
from tdd_project.store.routers import api_router


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            # root_path=settings.ROOT_PATH,
            debug=True,
        )


app = App()
# app = FastAPI()

app.include_router(api_router)


@app.get("hello")
async def hello():
    return "Hellllo!!"
