from pension_api.models.requests import PensionCalculationRequest
from pension_api.models.responses import PensionCalculationResponse

from pension_api.core.exceptions import (
    InvalidRetirementAgeException,
)


def calculate_pension(
    pension_data: PensionCalculationRequest,
) -> PensionCalculationResponse:

    # Business validation
    if pension_data.retirement_age <= pension_data.current_age:
        raise InvalidRetirementAgeException()

    years_to_retirement = pension_data.retirement_age - pension_data.current_age

    total_months = years_to_retirement * 12

    annual_growth_rate = pension_data.annual_growth_rate / 100

    # Convert annual growth rate to effective monthly growth rate
    monthly_growth_rate = ((1 + annual_growth_rate) ** (1 / 12)) - 1

    current_balance = pension_data.current_balance

    monthly_contribution = (
        pension_data.contribution_amount
        if pension_data.contribution_frequency == "monthly"
        else pension_data.contribution_amount / 12
    )

    # Future value of current balance
    future_value_of_current_balance = (
        current_balance * (1 + monthly_growth_rate) ** total_months
    )

    # Future value of contributions
    if monthly_growth_rate == 0:

        future_value_of_contributions = monthly_contribution * total_months

    else:

        contribution_growth_factor = (
            (1 + monthly_growth_rate) ** total_months - 1
        ) / monthly_growth_rate

        future_value_of_contributions = (
            monthly_contribution * contribution_growth_factor
        )

    projected_balance = future_value_of_current_balance + future_value_of_contributions

    return PensionCalculationResponse(
        current_balance=current_balance,
        projected_balance=round(
            projected_balance,
            2,
        ),
        years_to_retirement=years_to_retirement,
        monthly_contribution=round(
            monthly_contribution,
            2,
        ),
    )
