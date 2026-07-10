from pydantic import BaseModel


class YearProjection(BaseModel):
    age: int
    balance: float


class PensionCalculationResponse(BaseModel):
    years_to_retirement: int
    projected_balance: float
    total_contributions: float
    total_growth: float
    projection: list[YearProjection]
