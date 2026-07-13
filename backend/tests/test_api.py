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
        "contribution_frequency": ContributionFrequency.ANNUAL.value,
    }

    response = client.post(
        "/pension/calculate_contribution",
        json=payload,
    )

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    assert "years_to_retirement" in body
    assert "required_contribution" in body
    assert "total_contributions" in body
    assert "total_growth" in body
    assert "projection" in body

    first_projection = body["projection"][0]

    assert "age" in first_projection
    assert "balance" in first_projection
    assert "contributions" in first_projection
    assert "growth" in first_projection


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
        "contribution_frequency": ContributionFrequency.ANNUAL.value,
    }

    response = client.post(
        "/pension/calculate_contribution",
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
        "/pension/calculate_contribution",
        json=payload,
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_invalid_contribution_frequency(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 100000,
        "target_amount": 5000000,
        "contribution_frequency": "weekly",
        "annual_growth_rate": 8,
    }

    response = client.post(
        "/pension/calculate_contribution",
        json=payload,
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_negative_current_balance(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": -100,
        "target_amount": 5000000,
        "annual_growth_rate": 8,
        "contribution_frequency": ContributionFrequency.ANNUAL.value,
    }

    response = client.post(
        "/pension/calculate_contribution",
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
        "contribution_frequency": ContributionFrequency.ANNUAL.value,
    }

    response = client.post(
        "/pension/calculate_contribution",
        json=payload,
    )

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_goal_projection_contains_required_fields(client):
    payload = {
        "current_age": 30,
        "retirement_age": 65,
        "current_balance": 100000,
        "target_amount": 5000000,
        "annual_growth_rate": 8,
        "contribution_frequency": ContributionFrequency.ANNUAL.value,
    }

    response = client.post(
        "/pension/calculate_contribution",
        json=payload,
    )

    assert response.status_code == status.HTTP_200_OK

    body = response.json()

    for year in body["projection"]:
        assert "age" in year
        assert "balance" in year
        assert "contributions" in year
        assert "growth" in year

        assert year["balance"] >= 0
        assert year["contributions"] >= 0
        assert year["growth"] >= 0


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")

    assert response.status_code == status.HTTP_404_NOT_FOUND