from pension_api.models.requests import (
    RetirementGoalRequest,
    ContributionFrequency,
)

from pension_api.models.responses import (
    RetirementGoalResponse,
)

from pension_api.core.exceptions import (
    InvalidRetirementAgeException,
    InvalidTargetAmountException,
)


def calculate_retirement_goal(
    goal_data: RetirementGoalRequest,
) -> RetirementGoalResponse:

    # Business validation
    if goal_data.retirement_age <= goal_data.current_age:
        raise InvalidRetirementAgeException()

    if goal_data.target_amount <= 0:
        raise InvalidTargetAmountException()

    years_to_retirement = goal_data.retirement_age - goal_data.current_age

    total_months = years_to_retirement * 12

    annual_growth_rate = goal_data.annual_growth_rate / 100

    # Convert annual growth rate to effective monthly growth
    monthly_growth_rate = ((1 + annual_growth_rate) ** (1 / 12)) - 1

    # Calculate future value of current balance
    future_value_of_current_balance = (
        goal_data.current_balance * (1 + monthly_growth_rate) ** total_months
    )

    # Determine remaining amount required
    remaining_amount_needed = goal_data.target_amount - future_value_of_current_balance

    already_reached_goal = False

    if remaining_amount_needed <= 0:

        required_monthly_contribution = 0
        already_reached_goal = True

    else:

        # Handle no investment growth
        if monthly_growth_rate == 0:

            required_monthly_contribution = remaining_amount_needed / total_months

        else:

            contribution_factor = (
                (1 + monthly_growth_rate) ** total_months - 1
            ) / monthly_growth_rate

            required_monthly_contribution = (
                remaining_amount_needed / contribution_factor
            )

    # Convert monthly calculation into user preference
    if goal_data.contribution_frequency == ContributionFrequency.MONTHLY:
        required_contribution = required_monthly_contribution

    else:
        required_contribution = required_monthly_contribution * 12

    return RetirementGoalResponse(
        target_amount=goal_data.target_amount,
        required_contribution=round(
            required_contribution,
            2,
        ),
        contribution_frequency=(goal_data.contribution_frequency),
        years_to_retirement=years_to_retirement,
        already_reached_goal=already_reached_goal,
    )
