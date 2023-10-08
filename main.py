from fastapi import FastAPI
from posts import models as post_model
from users import models as user_model
from comments import models as comment_model
from database.database import engine
from users.routers import router as user_router
from posts.routers import router as post_router
from auth.routers import router as auth_router
from comments.routers import router as comment_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user_router)
app.include_router(post_router)
app.include_router(auth_router)
app.include_router(comment_router)


post_model.Base.metadata.create_all(engine)
user_model.Base.metadata.create_all(engine)
comment_model.Base.metadata.create_all(engine)


origins = ["http://localhost:3000",
           "http://localhost:3001",
           "http://localhost:3002"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


app.mount("/images", StaticFiles(directory="images"), name="images")
