
import pytest
from freelanceflow.services.pricing import calculate_estimate


def test_calculate_estimate():
    assert calculate_estimate(25, 20) == 500.00


def test_calculate_estimate_with_decimal_rate():
    assert calculate_estimate(25.50, 8) == 204.00


@pytest.mark.parametrize(
    "rate, hours",
    [(0, 10), (-5, 10), (25, 0), (25, -2)],
)
def test_calculate_estimate_rejects_nonpositive_values(rate, hours):
    with pytest.raises(ValueError):
        calculate_estimate(rate, hours)
