from fastapi import status

from pension_api.models.requests import ContributionFrequency


def test_calculate_pension_success(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 100000,
        "contribution_amount": 2000,
        "contribution_frequency": ContributionFrequency.MONTHLY.value,
        "annual_growth_rate": 8,
    }

    response = client.post(
        "/pension/calculate_pension",
        json=payload,
    )

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert "years_to_retirement" in body
    assert "projected_balance" in body
    assert "total_contributions" in body
    assert "total_growth" in body
    assert "projection" in body


def test_goal_calculation_success(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 100000,
        "target_amount": 5000000,
        "annual_growth_rate": 8,
        "contribution_frequency": ContributionFrequency.MONTHLY.value,
    }

    response = client.post(
        "/pension/goal",
        json=payload,
    )

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert "target_amount" in body
    assert "required_contribution" in body
    assert "contribution_frequency" in body
    assert "years_to_retirement" in body
    assert "already_reached_goal" in body


def test_calculate_pension_invalid_retirement_age(client):
    payload = {
        "current_age": 65,
        "retirement_age": 64,
        "current_balance": 100000,
        "contribution_amount": 2000,
        "contribution_frequency": ContributionFrequency.MONTHLY.value,
        "annual_growth_rate": 8,
    }

    response = client.post(
        "/pension/calculate_pension",
        json=payload,
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_goal_invalid_retirement_age(client):
    payload = {
        "current_age": 65,
        "retirement_age": 64,
        "current_balance": 100000,
        "target_amount": 5000000,
        "annual_growth_rate": 8,
        "contribution_frequency": ContributionFrequency.MONTHLY.value,
    }

    response = client.post(
        "/pension/goal",
        json=payload,
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_calculate_pension_missing_required_field(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
    }

    response = client.post(
        "/pension/calculate_pension",
        json=payload,
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_goal_missing_required_field(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
    }

    response = client.post(
        "/pension/goal",
        json=payload,
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_invalid_contribution_frequency(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 100000,
        "contribution_amount": 2000,
        "contribution_frequency": "weekly",
        "annual_growth_rate": 8,
    }

    response = client.post(
        "/pension/calculate_pension",
        json=payload,
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_negative_current_balance(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": -100,
        "contribution_amount": 2000,
        "contribution_frequency": ContributionFrequency.MONTHLY.value,
        "annual_growth_rate": 8,
    }

    response = client.post(
        "/pension/calculate_pension",
        json=payload,
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_negative_target_amount(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 100000,
        "target_amount": -5000,
        "annual_growth_rate": 8,
        "contribution_frequency": ContributionFrequency.MONTHLY.value,
    }

    response = client.post(
        "/pension/goal",
        json=payload,
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_goal_already_reached(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 6000000,
        "target_amount": 5000000,
        "annual_growth_rate": 8,
        "contribution_frequency": ContributionFrequency.MONTHLY.value,
    }

    response = client.post(
        "/pension/goal",
        json=payload,
    )

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert body["already_reached_goal"] is True
    assert body["required_contribution"] == 0


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")

    assert response.status_code == status.HTTP_404_NOT_FOUND