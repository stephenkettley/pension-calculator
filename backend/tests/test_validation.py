import pytest
from pydantic import ValidationError

from pension_api.models.requests import (
    ContributionFrequency,
    PensionCalculationRequest,
    RetirementGoalRequest,
)


def test_valid_pension_request():
    request = PensionCalculationRequest(
        current_age=30,
        retirement_age=65,
        current_balance=100000,
        contribution_amount=2000,
        contribution_frequency=ContributionFrequency.MONTHLY,
        annual_growth_rate=8,
    )

    assert request.current_age == 30
    assert request.retirement_age == 65


def test_valid_goal_request():
    request = RetirementGoalRequest(
        current_age=30,
        retirement_age=65,
        current_balance=100000,
        target_amount=5000000,
        annual_growth_rate=8,
        contribution_frequency=ContributionFrequency.MONTHLY,
    )

    assert request.target_amount == 5000000


@pytest.mark.parametrize(
    "field,value",
    [
        ("current_age", 17),
        ("retirement_age", 101),
        ("current_balance", -1),
        ("contribution_amount", -100),
        ("annual_growth_rate", -5),
        ("annual_growth_rate", 101),
    ],
)
def test_invalid_pension_fields(field, value):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 100000,
        "contribution_amount": 2000,
        "contribution_frequency": ContributionFrequency.MONTHLY,
        "annual_growth_rate": 8,
    }

    payload[field] = value

    with pytest.raises(ValidationError):
        PensionCalculationRequest(**payload)


@pytest.mark.parametrize(
    "field,value",
    [
        ("current_age", 17),
        ("retirement_age", 101),
        ("current_balance", -1),
        ("target_amount", -1000),
        ("annual_growth_rate", -1),
        ("annual_growth_rate", 101),
    ],
)
def test_invalid_goal_fields(field, value):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 100000,
        "target_amount": 5000000,
        "annual_growth_rate": 8,
        "contribution_frequency": ContributionFrequency.MONTHLY,
    }

    payload[field] = value

    with pytest.raises(ValidationError):
        RetirementGoalRequest(**payload)


def test_invalid_contribution_frequency_for_pension():
    with pytest.raises(ValidationError):
        PensionCalculationRequest(
            current_age=30,
            retirement_age=65,
            current_balance=100000,
            contribution_amount=2000,
            contribution_frequency="weekly",
            annual_growth_rate=8,
        )


def test_invalid_contribution_frequency_for_goal():
    with pytest.raises(ValidationError):
        RetirementGoalRequest(
            current_age=30,
            retirement_age=65,
            current_balance=100000,
            target_amount=5000000,
            annual_growth_rate=8,
            contribution_frequency="weekly",
        )


def test_missing_required_field_for_pension():
    with pytest.raises(ValidationError):
        PensionCalculationRequest(
            retirement_age=65,
            current_balance=100000,
            contribution_amount=2000,
            contribution_frequency=ContributionFrequency.MONTHLY,
            annual_growth_rate=8,
        )


def test_missing_required_field_for_goal():
    with pytest.raises(ValidationError):
        RetirementGoalRequest(
            retirement_age=65,
            current_balance=100000,
            target_amount=5000000,
            annual_growth_rate=8,
            contribution_frequency=ContributionFrequency.MONTHLY,
        )