
def calculate_estimate(hourly_rate: float, estimated_hours: float) -> float:
    if hourly_rate <= 0:
        raise ValueError("Hourly rate must be positive.")

    if estimated_hours <= 0:
        raise ValueError("Estimated hours must be positive.")

    return round(hourly_rate * estimated_hours, 2)
