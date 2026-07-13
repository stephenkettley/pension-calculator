import pytest

from pension_api.models.responses import YearProjection
from pension_api.services.goal_calculator import (
    calculate_required_contribution,
)


def test_calculate_required_contribution(default_goal_request):
    request = default_goal_request.model_copy(deep=True)

    result = calculate_required_contribution(request)

    assert result.years_to_retirement == 35
    assert result.required_contribution > 0
    assert result.total_contributions > 0
    assert result.total_growth > 0
    assert len(result.projection) == 35


def test_goal_already_reached(default_goal_request):
    request = default_goal_request.model_copy(deep=True)
    request.current_balance = 6_000_000
    request.target_amount = 5_000_000

    result = calculate_required_contribution(request)

    assert result.required_contribution == 0
    assert result.total_contributions == 0

    assert all(
        year.contributions == 0
        for year in result.projection
    )


def test_calculate_required_contribution_with_zero_balance(
    default_goal_request,
):
    request = default_goal_request.model_copy(deep=True)
    request.current_balance = 0

    result = calculate_required_contribution(request)

    assert result.required_contribution > 0


def test_calculate_required_contribution_with_zero_growth(
    default_goal_request,
):
    request = default_goal_request.model_copy(deep=True)
    request.annual_growth_rate = 0

    result = calculate_required_contribution(request)

    assert result.required_contribution > 0


def test_calculate_required_contribution_one_year_until_retirement(
    default_goal_request,
):
    request = default_goal_request.model_copy(deep=True)
    request.current_age = 64
    request.retirement_age = 65

    result = calculate_required_contribution(request)

    assert result.years_to_retirement == 1
    assert len(result.projection) == 1


def test_projection_contains_one_entry_per_year(
    default_goal_request,
):
    request = default_goal_request.model_copy(deep=True)

    result = calculate_required_contribution(request)

    assert (
        len(result.projection)
        == result.years_to_retirement
    )

    first = result.projection[0]

    assert isinstance(first, YearProjection)
    assert first.age == request.current_age + 1


def test_goal_response_types(default_goal_request):
    request = default_goal_request.model_copy(deep=True)

    result = calculate_required_contribution(request)

    assert isinstance(
        result.required_contribution,
        float,
    )

    assert isinstance(
        result.total_contributions,
        float,
    )

    assert isinstance(
        result.total_growth,
        float,
    )

    assert isinstance(
        result.years_to_retirement,
        int,
    )

    assert isinstance(
        result.projection,
        list,
    )

    assert all(
        isinstance(item, YearProjection)
        for item in result.projection
    )