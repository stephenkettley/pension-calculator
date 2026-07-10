from enum import Enum

from pydantic import BaseModel, Field


class ContributionFrequency(str, Enum):
    MONTHLY = "monthly"
    ANNUAL = "annual"


class PensionCalculationRequest(BaseModel):
    current_age: int = Field(..., ge=18, le=100)

    retirement_age: int = Field(..., ge=18, le=100)

    current_balance: float = Field(..., ge=0)

    contribution_amount: float = Field(..., ge=0)

    contribution_frequency: ContributionFrequency

    annual_growth_rate: float = Field(
        ...,
        ge=0,
        le=100,
    )


class RetirementGoalRequest(BaseModel):
    current_age: int = Field(..., ge=18, le=100)

    retirement_age: int = Field(..., ge=18, le=100)

    current_balance: float = Field(..., ge=0)

    target_amount: float = Field(..., gt=0)

    annual_growth_rate: float = Field(
        ...,
        ge=0,
        le=100,
    )

    contribution_frequency: ContributionFrequency
