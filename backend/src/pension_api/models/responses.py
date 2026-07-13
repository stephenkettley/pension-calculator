from pydantic import BaseModel

from pension_api.models.requests import ContributionFrequency


class YearProjection(BaseModel):
    age: int
    balance: float
    contributions: float
    growth: float


class PensionCalculationResponse(BaseModel):
    years_to_retirement: int
    projected_balance: float
    total_contributions: float
    total_growth: float
    projection: list[YearProjection]


class RetirementGoalResponse(BaseModel):
    years_to_retirement: int
    required_contribution: float
    total_contributions: float
    total_growth: float
    projection: list[YearProjection]
