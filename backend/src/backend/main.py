from fastapi import FastAPI

from .routers import health

app = FastAPI(title="AIO-Conquer2027 API")
app.include_router(health.router)
