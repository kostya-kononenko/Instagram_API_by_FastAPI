from fastapi import FastAPI
from instagram import models as instagram_model
from users import models as user_model
from database.database import engine
from users.routers import router as user_router
from instagram.routers import router as instagram_router
from fastapi.staticfiles import StaticFiles
from auth.routers import router as auth_router


app = FastAPI()

app.include_router(user_router)
app.include_router(instagram_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


instagram_model.Base.metadata.create_all(engine)
user_model.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
