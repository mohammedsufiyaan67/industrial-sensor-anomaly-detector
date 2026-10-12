
%%writefile test_sensor_detector.py

from sensor_detector import classify_temperature

def test_normal_reading():
    assert classify_temperature(65) == "Normal"

def test_high_temperature():
    assert classify_temperature(105) == "WARNING"

def test_negative_reading():
    assert classify_temperature(-999) == "INVALID"

def test_reading_above_range():
    assert classify_temperature(160) == "INVALID"

def test_missing_reading():
    assert classify_temperature(None) == "INVALID"

def test_custom_safety_limit():
    assert classify_temperature(85, safe_limit=80) == "WARNING"

def test_reading_at_threshold():
    assert classify_temperature(90) == "Normal"

if __name__ == "__main__":
    test_normal_reading()
    test_high_temperature()
    test_negative_reading()
    test_reading_above_range()
    test_missing_reading()
    test_custom_safety_limit()
    test_reading_at_threshold()

    print("SUCCESS: All 7 project tests passed!")
