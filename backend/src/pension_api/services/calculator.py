from pension_api.core.exceptions import (
    InvalidRetirementAgeException,
)
from pension_api.models.requests import (
    ContributionFrequency,
    PensionCalculationRequest,
)
from pension_api.models.responses import (
    PensionCalculationResponse,
    YearProjection,
)


def calculate_pension(
    pension_data: PensionCalculationRequest,
) -> PensionCalculationResponse:

    # Business validation
    if pension_data.retirement_age <= pension_data.current_age:
        raise InvalidRetirementAgeException()

    years_to_retirement = (
        pension_data.retirement_age - pension_data.current_age
    )

    total_months = years_to_retirement * 12

    annual_growth_rate = pension_data.annual_growth_rate / 100

    # Convert annual growth rate to effective monthly rate
    monthly_growth_rate = (
        (1 + annual_growth_rate) ** (1 / 12)
    ) - 1

    current_balance = pension_data.current_balance

    monthly_contribution = (
        pension_data.contribution_amount
        if pension_data.contribution_frequency
        == ContributionFrequency.MONTHLY
        else pension_data.contribution_amount / 12
    )

    # Future value of current balance
    future_value_of_current_balance = (
        current_balance
        * (1 + monthly_growth_rate) ** total_months
    )

    # Future value of contributions
    if monthly_growth_rate == 0:
        future_value_of_contributions = (
            monthly_contribution * total_months
        )
    else:
        contribution_growth_factor = (
            ((1 + monthly_growth_rate) ** total_months) - 1
        ) / monthly_growth_rate

        future_value_of_contributions = (
            monthly_contribution
            * contribution_growth_factor
        )

    projected_balance = (
        future_value_of_current_balance
        + future_value_of_contributions
    )

    total_contributions = (
        monthly_contribution * total_months
    )

    total_growth = (
        projected_balance
        - current_balance
        - total_contributions
    )

    # Yearly projection
    projection = []

    balance = current_balance

    for year in range(1, years_to_retirement + 1):

        for _ in range(12):
            balance *= (1 + monthly_growth_rate)
            balance += monthly_contribution

        projection.append(
            YearProjection(
                age=pension_data.current_age + year,
                balance=round(balance, 2),
            )
        )

    return PensionCalculationResponse(
        years_to_retirement=years_to_retirement,
        projected_balance=round(projected_balance, 2),
        total_contributions=round(
            total_contributions,
            2,
        ),
        total_growth=round(
            total_growth,
            2,
        ),
        projection=projection,
    )