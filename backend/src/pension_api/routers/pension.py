from fastapi import APIRouter

from pension_api.models.requests import PensionCalculationRequest
from pension_api.models.responses import PensionCalculationResponse
from pension_api.services.calculator import calculate_pension

router = APIRouter(
    prefix="/pension",
    tags=["Pension"],
)


@router.post(
    "/calculate_pension",
    response_model=PensionCalculationResponse,
)
def calculate(
    request: PensionCalculationRequest,
):
    return calculate_pension(request)
