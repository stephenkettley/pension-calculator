import pytest

from pension_api.models.requests import ContributionFrequency
from pension_api.services.calculator import calculate_pension


def test_calculate_pension_with_monthly_contributions(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)

    result = calculate_pension(request)

    assert result.years_to_retirement == 35
    assert result.projected_balance > 0
    assert result.total_contributions > 0
    assert result.total_growth > 0
    assert len(result.projection) == 35


@pytest.mark.parametrize(
    "frequency, contribution",
    [
        (ContributionFrequency.MONTHLY, 2000),
        (ContributionFrequency.ANNUAL, 24000),
    ],
)
def test_calculate_pension_with_different_contribution_frequencies(
    default_pension_request,
    frequency,
    contribution,
):
    request = default_pension_request.model_copy(deep=True)
    request.contribution_frequency = frequency
    request.contribution_amount = contribution

    result = calculate_pension(request)

    assert result.projected_balance > 0
    assert result.total_contributions > 0


def test_calculate_pension_with_zero_current_balance(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)
    request.current_balance = 0

    result = calculate_pension(request)

    assert result.projected_balance > 0
    assert result.total_growth > 0


def test_calculate_pension_with_zero_contributions(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)
    request.contribution_amount = 0

    result = calculate_pension(request)

    assert result.total_contributions == 0
    assert result.projected_balance > 0


def test_calculate_pension_with_zero_growth_rate(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)
    request.annual_growth_rate = 0

    result = calculate_pension(request)

    assert result.total_growth == 0
    assert result.total_contributions > 0


def test_calculate_pension_one_year_until_retirement(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)
    request.current_age = 64
    request.retirement_age = 65

    result = calculate_pension(request)

    assert result.years_to_retirement == 1
    assert len(result.projection) == 1


def test_projection_contains_one_entry_per_year(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)

    result = calculate_pension(request)

    assert len(result.projection) == result.years_to_retirement


def test_projection_entries_are_ordered_by_age(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)

    result = calculate_pension(request)

    ages = [year.age for year in result.projection]

    assert ages == sorted(ages)
    assert ages[0] == request.current_age + 1
    assert ages[-1] == request.retirement_age


def test_projection_balances_increase_over_time(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)

    result = calculate_pension(request)

    balances = [year.balance for year in result.projection]

    assert balances[-1] == result.projected_balance
    assert balances[0] > request.current_balance


def test_calculate_pension_response_types(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)

    result = calculate_pension(request)

    assert isinstance(result.years_to_retirement, int)
    assert isinstance(result.projected_balance, float)
    assert isinstance(result.total_contributions, float)
    assert isinstance(result.total_growth, float)
    assert isinstance(result.projection, list)


def test_projection_item_types(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)

    result = calculate_pension(request)

    first_year = result.projection[0]

    assert isinstance(first_year.age, int)
    assert isinstance(first_year.balance, float)
    assert isinstance(first_year.contributions, float)
    assert isinstance(first_year.growth, float)


def test_projection_contains_contributions_and_growth(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)

    result = calculate_pension(request)

    first_year = result.projection[0]

    assert first_year.contributions > 0
    assert first_year.growth >= 0


def test_projection_final_year_matches_totals(
    default_pension_request,
):
    request = default_pension_request.model_copy(deep=True)

    result = calculate_pension(request)

    final_year = result.projection[-1]

    assert final_year.balance == result.projected_balance
    assert final_year.contributions <= result.total_contributions
    assert final_year.growth <= result.total_growth
