from fastapi import APIRouter

from pension_api.models.requests import (
    PensionCalculationRequest,
    RetirementGoalRequest,
)
from pension_api.models.responses import (
    PensionCalculationResponse,
    RetirementGoalResponse,
)
from pension_api.services.calculator import calculate_pension
from pension_api.services.goal_calculator import calculate_required_contribution

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


@router.post(
    "/goal",
    response_model=RetirementGoalResponse,
)
def calculate_retirement_goal_endpoint(
    request: RetirementGoalRequest,
):
    return calculate_required_contribution(request)
