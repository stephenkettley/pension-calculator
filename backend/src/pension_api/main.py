from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from pension_api.core.exceptions import PensionAPIException
from pension_api.routers import pension


app = FastAPI(
    title="Pension Calculator API",
    description="API for retirement planning calculations",
    version="1.0.0",
)


@app.exception_handler(PensionAPIException)
async def pension_exception_handler(
    request: Request,
    exc: PensionAPIException,
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "error": {
                "code": exc.code,
                "message": exc.message,
            },
        },
    )


app.include_router(
    pension.router,
)


@app.get("/")
def root():
    return {"message": "Welcome to the Pension Calculator API"}
