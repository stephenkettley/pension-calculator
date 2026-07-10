from enum import Enum

from pydantic import BaseModel, Field, model_validator


class ContributionFrequency(str, Enum):
    MONTHLY = "monthly"
    ANNUAL = "annual"


class PensionCalculationRequest(BaseModel):
    current_age: int = Field(..., ge=18, le=100)
    retirement_age: int = Field(..., ge=18, le=100)

    current_balance: float = Field(..., ge=0)

    contribution_amount: float = Field(..., ge=0)
    contribution_frequency: ContributionFrequency

    investment_growth_rate: float = Field(..., ge=0, le=100)

    @model_validator(mode="after")
    def validate_retirement_age(self):
        if self.retirement_age <= self.current_age:
            raise ValueError("Retirement age must be greater than current age")

        return self


class RetirementGoalRequest(BaseModel):
    current_age: int = Field(..., ge=18, le=100)

    retirement_age: int = Field(..., ge=18, le=100)

    current_balance: float = Field(..., ge=0)

    target_amount: float = Field(..., ge=0)

    annual_growth_rate: float = Field(..., ge=0, le=100)

    contribution_frequency: ContributionFrequency

    @model_validator(mode="after")
    def validate_retirement_age(self):
        if self.retirement_age <= self.current_age:
            raise ValueError("Retirement age must be greater than current age")

        return self
