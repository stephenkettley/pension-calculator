import pytest
from fastapi.testclient import TestClient

from pension_api.main import app
from pension_api.models.requests import (
    ContributionFrequency,
    PensionCalculationRequest,
    RetirementGoalRequest,
)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def default_pension_request():
    return PensionCalculationRequest(
        current_age=30,
        retirement_age=65,
        current_balance=100_000.0,
        contribution_amount=2_000.0,
        contribution_frequency=ContributionFrequency.MONTHLY,
        annual_growth_rate=8.0,
    )


@pytest.fixture
def default_goal_request():
    return RetirementGoalRequest(
        current_age=30,
        retirement_age=65,
        current_balance=100_000.0,
        target_amount=5_000_000.0,
        annual_growth_rate=8.0,
        contribution_frequency=ContributionFrequency.MONTHLY,
    )
