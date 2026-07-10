from pension_api.models.responses import (
    PensionCalculationResponse,
    YearProjection,
)
from pension_api.models.requests import (
    PensionCalculationRequest,
    ContributionFrequency,
)


def calculate_pension(
    pension_data: PensionCalculationRequest,
) -> PensionCalculationResponse:

    years_to_retirement = pension_data.retirement_age - pension_data.current_age

    total_months = years_to_retirement * 12

    balance = pension_data.current_balance

    total_contributions = pension_data.current_balance

    annual_growth_rate = pension_data.investment_growth_rate / 100

    monthly_growth_rate = annual_growth_rate / 12

    projection = []

    current_age = pension_data.current_age

    for month in range(total_months):

        # Apply monthly investment growth

        balance *= 1 + monthly_growth_rate

        # Apply contribution based on frequency

        if pension_data.contribution_frequency == ContributionFrequency.MONTHLY:

            balance += pension_data.contribution_amount

            total_contributions += pension_data.contribution_amount

        elif pension_data.contribution_frequency == ContributionFrequency.ANNUAL:

            # Add annual contribution at the end of each year

            if month % 12 == 11:

                balance += pension_data.contribution_amount

                total_contributions += pension_data.contribution_amount

        # Store yearly snapshot for graph

        if month % 12 == 11:

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
