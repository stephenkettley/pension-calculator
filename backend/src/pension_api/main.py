from fastapi import FastAPI

from pension_api.routers.health import router as health_router
from pension_api.routers.pension import router as pension_router

app = FastAPI(
    title="Pension Calculator API",
    description="REST API for retirement planning and pension projections.",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(pension_router)
