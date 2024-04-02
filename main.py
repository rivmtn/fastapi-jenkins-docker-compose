from fastapi import FastAPI, APIRouter

app = FastAPI(root_path="/api")
router = APIRouter(prefix="/api")


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(router)
