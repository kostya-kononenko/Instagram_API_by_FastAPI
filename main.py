from fastapi import FastAPI
from instagram import models as instagram_model
from users import models as user_model
from database.database import engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


instagram_model.Base.metadata.create_all(engine)
user_model.Base.metadata.create_all(engine)
