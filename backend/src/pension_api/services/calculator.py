from pension_api.models.requests import PensionCalculationRequest
from pension_api.models.responses import (
    PensionCalculationResponse,
    YearProjection,
)


def calculate_pension(
    pension_data: PensionCalculationRequest,
) -> PensionCalculationResponse:

    years_to_retirement = pension_data.retirement_age - pension_data.current_age

    balance = pension_data.current_balance

    total_contributions = pension_data.current_balance

    projection = []

    annual_growth_rate = pension_data.investment_growth_rate / 100

    current_age = pension_data.current_age

    for _ in range(years_to_retirement):

        balance *= 1 + annual_growth_rate

        balance += pension_data.annual_contribution

        total_contributions += pension_data.annual_contribution

        current_age += 1

        projection.append(
            YearProjection(
                age=current_age,
                balance=round(balance, 2),
            )
        )

    total_growth = balance - total_contributions

    return PensionCalculationResponse(
        years_to_retirement=years_to_retirement,
        projected_balance=round(balance, 2),
        total_contributions=round(total_contributions, 2),
        total_growth=round(total_growth, 2),
        projection=projection,
    )
