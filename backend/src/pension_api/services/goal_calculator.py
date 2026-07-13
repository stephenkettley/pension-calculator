import logging

from pension_api.core.exceptions import (
    InvalidRetirementAgeException,
    InvalidTargetAmountException,
)
from pension_api.models.requests import RetirementGoalRequest
from pension_api.models.responses import (
    RetirementGoalResponse,
    YearProjection,
)

logger = logging.getLogger(__name__)


def calculate_required_contribution(
    goal_data: RetirementGoalRequest,
) -> RetirementGoalResponse:

    if goal_data.retirement_age <= goal_data.current_age:
        logger.warning(
            f"Invalid retirement age: retirement_age={goal_data.retirement_age} <= current_age={goal_data.current_age}"
        )
        raise InvalidRetirementAgeException()

    if goal_data.target_amount <= 0:
        logger.warning(
            f"Invalid target amount: target_amount={goal_data.target_amount}"
        )
        raise InvalidTargetAmountException()

    years_to_retirement = (
        goal_data.retirement_age - goal_data.current_age
    )

    total_months = years_to_retirement * 12

    annual_growth_rate = (
        goal_data.annual_growth_rate / 100
    )

    monthly_growth_rate = (
        (1 + annual_growth_rate) ** (1 / 12)
    ) - 1

    logger.debug(
        f"Goal calculation inputs: "
        f"years_to_retirement={years_to_retirement}, "
        f"monthly_growth_rate={monthly_growth_rate:.6f}, "
        f"target_amount={goal_data.target_amount}"
    )

    future_value_of_current_balance = (
        goal_data.current_balance
        * (1 + monthly_growth_rate) ** total_months
    )

    remaining_amount_needed = (
        goal_data.target_amount
        - future_value_of_current_balance
    )

    if remaining_amount_needed <= 0:
        required_monthly_contribution = 0

    elif monthly_growth_rate == 0:
        required_monthly_contribution = (
            remaining_amount_needed
            / total_months
        )

    else:
        contribution_factor = (
            (
                (1 + monthly_growth_rate)
                ** total_months
                - 1
            )
            / monthly_growth_rate
        )

        required_monthly_contribution = (
            remaining_amount_needed
            / contribution_factor
        )

    required_contribution = (
        required_monthly_contribution * 12
    )

    monthly_contribution = (
        required_monthly_contribution
    )

    if monthly_growth_rate == 0:
        future_value_of_contributions = (
            monthly_contribution * total_months
        )
    else:
        contribution_growth_factor = (
            (
                (1 + monthly_growth_rate)
                ** total_months
                - 1
            )
            / monthly_growth_rate
        )

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
        - goal_data.current_balance
        - total_contributions
    )

    projection = []

    balance = goal_data.current_balance
    contributions_so_far = 0
    growth_so_far = 0

    for year in range(
        1,
        years_to_retirement + 1,
    ):
        for _ in range(12):
            monthly_growth = (
                balance * monthly_growth_rate
            )

            growth_so_far += monthly_growth

            balance += monthly_growth
            balance += monthly_contribution

            contributions_so_far += (
                monthly_contribution
            )

        projection.append(
            YearProjection(
                age=goal_data.current_age + year,
                balance=round(balance, 2),
                contributions=round(
                    contributions_so_far,
                    2,
                ),
                growth=round(
                    growth_so_far,
                    2,
                ),
            )
        )

    logger.info(
        f"Goal calculation completed: "
        f"years_to_retirement={years_to_retirement}, "
        f"required_contribution={round(required_contribution, 2)}"
    )

    return RetirementGoalResponse(
        years_to_retirement=years_to_retirement,
        required_contribution=round(
            required_contribution,
            2,
        ),
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