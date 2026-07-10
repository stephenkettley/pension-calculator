from pydantic import BaseModel, Field


class PensionCalculationRequest(BaseModel):
    current_age: int = Field(..., ge=18, le=100)
    retirement_age: int = Field(..., ge=18, le=100)

    current_balance: float = Field(..., ge=0)
    annual_contribution: float = Field(..., ge=0)

    investment_growth_rate: float = Field(..., ge=0, le=100)
