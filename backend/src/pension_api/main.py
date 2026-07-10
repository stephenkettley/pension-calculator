from fastapi import FastAPI

app = FastAPI(
    title="Pension Calculator API",
    description="REST API for retirement planning and pension projections.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pension Calculator API!"}
