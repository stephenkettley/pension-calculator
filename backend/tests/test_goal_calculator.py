import pytest

from pension_api.models.requests import ContributionFrequency
from pension_api.services.goal_calculator import calculate_required_contribution


def test_calculate_required_monthly_contribution(default_goal_request):
    # Arrange
    request = default_goal_request.model_copy(deep=True)

    # Act
    result = calculate_required_contribution(request)

    # Assert
    assert result.target_amount == request.target_amount
    assert result.years_to_retirement == 35
    assert result.required_contribution > 0
    assert result.contribution_frequency == ContributionFrequency.MONTHLY
    assert result.already_reached_goal is False


@pytest.mark.parametrize(
    "frequency",
    [
        ContributionFrequency.MONTHLY,
        ContributionFrequency.ANNUAL,
    ],
)
def test_calculate_required_contribution_for_each_frequency(
    default_goal_request,
    frequency,
):
    # Arrange
    request = default_goal_request.model_copy(deep=True)
    request.contribution_frequency = frequency

    # Act
    result = calculate_required_contribution(request)

    # Assert
    assert result.contribution_frequency == frequency
    assert result.required_contribution >= 0


def test_goal_already_reached(default_goal_request):
    # Arrange
    request = default_goal_request.model_copy(deep=True)
    request.current_balance = 6_000_000
    request.target_amount = 5_000_000

    # Act
    result = calculate_required_contribution(request)

    # Assert
    assert result.already_reached_goal is True
    assert result.required_contribution == 0


def test_calculate_required_contribution_with_zero_balance(
    default_goal_request,
):
    # Arrange
    request = default_goal_request.model_copy(deep=True)
    request.current_balance = 0

    # Act
    result = calculate_required_contribution(request)

    # Assert
    assert result.required_contribution > 0


def test_calculate_required_contribution_with_zero_growth(
    default_goal_request,
):
    # Arrange
    request = default_goal_request.model_copy(deep=True)
    request.annual_growth_rate = 0

    # Act
    result = calculate_required_contribution(request)

    # Assert
    assert result.required_contribution > 0


def test_calculate_required_contribution_one_year_until_retirement(
    default_goal_request,
):
    # Arrange
    request = default_goal_request.model_copy(deep=True)
    request.current_age = 64
    request.retirement_age = 65

    # Act
    result = calculate_required_contribution(request)

    # Assert
    assert result.years_to_retirement == 1


def test_goal_response_types(default_goal_request):
    # Arrange
    request = default_goal_request.model_copy(deep=True)

    # Act
    result = calculate_required_contribution(request)

    # Assert
    assert isinstance(result.target_amount, float)
    assert isinstance(result.required_contribution, float)
    assert isinstance(result.years_to_retirement, int)
    assert isinstance(result.already_reached_goal, bool)
    assert isinstance(
        result.contribution_frequency,
        ContributionFrequency,
    )