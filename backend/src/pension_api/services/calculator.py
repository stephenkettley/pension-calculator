import logging

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

logger = logging.getLogger(__name__)


def calculate_pension(
    pension_data: PensionCalculationRequest,
) -> PensionCalculationResponse:
    if pension_data.retirement_age <= pension_data.current_age:
        logger.warning(
            f"Invalid retirement age: retirement_age={pension_data.retirement_age} "
            f"<= current_age={pension_data.current_age}"
        )
        raise InvalidRetirementAgeException()

    years_to_retirement = pension_data.retirement_age - pension_data.current_age
    total_months = years_to_retirement * 12
    annual_growth_rate = pension_data.annual_growth_rate / 100

    monthly_growth_rate = ((1 + annual_growth_rate) ** (1 / 12)) - 1
    current_balance = pension_data.current_balance
    monthly_contribution = (
        pension_data.contribution_amount
        if pension_data.contribution_frequency == ContributionFrequency.MONTHLY
        else pension_data.contribution_amount / 12
    )

    logger.debug(
        f"Calculation inputs: years_to_retirement={years_to_retirement}, "
        f"monthly_growth_rate={monthly_growth_rate:.6f}, "
        f"monthly_contribution={monthly_contribution}"
    )

    future_value_of_current_balance = current_balance * (1 + monthly_growth_rate) ** total_months

    if monthly_growth_rate == 0:
        logger.debug("Growth rate is 0 — using linear contribution sum instead of annuity formula")
        future_value_of_contributions = monthly_contribution * total_months
    else:
        contribution_growth_factor = (((1 + monthly_growth_rate) ** total_months) - 1) / monthly_growth_rate
        future_value_of_contributions = monthly_contribution * contribution_growth_factor

    projected_balance = future_value_of_current_balance + future_value_of_contributions
    total_contributions = monthly_contribution * total_months
    total_growth = projected_balance - current_balance - total_contributions

    projection = []
    balance = current_balance
    contributions_so_far = 0
    growth_so_far = 0
    for year in range(1, years_to_retirement + 1):
        for _ in range(12):
            monthly_growth = balance * monthly_growth_rate
            growth_so_far += monthly_growth
            balance += monthly_growth
            balance += monthly_contribution
            contributions_so_far += monthly_contribution
        projection.append(
            YearProjection(
                age=(pension_data.current_age + year),
                balance=round(balance, 2),
                contributions=round(contributions_so_far, 2),
                growth=round(growth_so_far, 2),
            )
        )

    logger.info(
        f"Pension calculation completed: years_to_retirement={years_to_retirement}, "
        f"projected_balance={round(projected_balance, 2)}, "
        f"total_contributions={round(total_contributions, 2)}, "
        f"total_growth={round(total_growth, 2)}"
    )

    return PensionCalculationResponse(
        years_to_retirement=years_to_retirement,
        projected_balance=round(projected_balance, 2),
        total_contributions=round(total_contributions, 2),
        total_growth=round(total_growth, 2),
        projection=projection,
    )
