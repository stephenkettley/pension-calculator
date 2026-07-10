from pydantic import BaseModel

from pension_api.models.requests import ContributionFrequency


class YearProjection(BaseModel):
    age: int
    balance: float


class PensionCalculationResponse(BaseModel):
    years_to_retirement: int
    projected_balance: float
    total_contributions: float
    total_growth: float
    projection: list[YearProjection]


class RetirementGoalResponse(BaseModel):
    target_amount: float
    required_contribution: float
    contribution_frequency: ContributionFrequency
    years_to_retirement: int
    already_reached_goal: bool
