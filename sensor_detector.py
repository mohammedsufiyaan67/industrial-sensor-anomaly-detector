
import math


def classify_temperature(
    temp, safe_limit=90, minimum=0, maximum=150
):
    """Classify a temperature reading using configured limits."""

    if (
        not isinstance(temp, (int, float))
        or isinstance(temp, bool)
        or not math.isfinite(temp)
    ):
        return "INVALID"

    if minimum > maximum:
        raise ValueError("Minimum cannot exceed maximum.")

    if safe_limit < minimum or safe_limit > maximum:
        raise ValueError("Safety limit must be within the valid range.")

    if temp < minimum or temp > maximum:
        return "INVALID"

    if temp > safe_limit:
        return "WARNING"

    return "Normal"


if __name__ == "__main__":
    readings = [65, 85, 105, -999, 160, None]

    print("INDUSTRIAL SENSOR REPORT")
    print("-" * 30)

    for reading in readings:
        status = classify_temperature(reading)
        print(f"Temperature: {reading} -> {status}")

