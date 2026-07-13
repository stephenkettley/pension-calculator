import logging

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

logger = logging.getLogger(__name__)

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
    logger.info(f"Pension calculation requested: {request.dict()}")
    result = calculate_pension(request)
    logger.info(f"Pension calculation completed for request: {request.dict()}")
    return result


@router.post(
    "/calculate_contribution",
    response_model=RetirementGoalResponse,
)
def calculate_retirement_goal_endpoint(
    request: RetirementGoalRequest,
):
    logger.info(f"Retirement goal calculation requested: {request.dict()}")
    result = calculate_required_contribution(request)
    logger.info(f"Retirement goal calculation completed for request: {request.dict()}")
    return result
