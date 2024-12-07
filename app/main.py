from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database import Engine
from routers import router
import store


app = FastAPI()

origins = [
    "http://localhost:8000"
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

store.Base.metadata.create_all(bind= Engine)
app.include_router(router= router)

@app.get("/")
def home():
    return "Home"