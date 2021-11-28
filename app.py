import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import blog
from db import models
from db.database import newengine


app = FastAPI(
    title="Blog API",
    description="This API was developed for teaching Fast API",
    version="0.0.1",
    terms_of_service="http://localhost:9000",
)
app.include_router(blog.router)


if __name__ == "__main__":
    uvicorn.run("app:app", port= 9000, reload=True)


origins = [
    'http://localhost:3000',
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

models.Base.metadata.create_all(newengine)