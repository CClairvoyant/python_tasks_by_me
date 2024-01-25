import pytest

from cars import Car


car = Car("Toyota", "Corolla", 0, 50, 25.0, 6.5)


@pytest.mark.timeout(1.0)
def test_drive_not_enough_fuel():
    """Test drive method with not enough fuel."""
    assert car.drive(1000) == "The car died after driving 384 kilometers."
    assert car.mileage == 384
    assert car.fuel == 0.0
    assert car.fuel_consumption == 6.5


@pytest.mark.timeout(1.0)
def test_drive_enough_fuel():
    """Test drive method with enough fuel."""
    car.fuel = 50
    assert car.drive(500) == "The car has reached its destination."
    assert car.mileage == 884
    assert car.fuel == 17.5
    assert car.fuel_consumption == 6.5


@pytest.mark.timeout(1.0)
def test_drive_fuel_consumption_increased_after_1000_km():
    """Test if fuel consumption is increased after mileage passed 1000 km mark."""
    assert car.drive(250) == "The car has reached its destination."
    assert car.mileage == 1134
    assert car.fuel == 1.25
    assert car.fuel_consumption == 6.51
    car.mileage = 1998
    car.drive(4)
    assert car.fuel_consumption == 6.52


@pytest.mark.timeout(1.0)
def test_drive_no_fuel():
    """Test drive method with zero fuel"""
    car.fuel = 0
    assert car.drive(100) == "The car has no fuel."
    assert car.drive(0) == "The car has no fuel."


@pytest.mark.timeout(1.0)
def test_drive_negative_distance():
    """Test drive method with negative distance"""
    try:
        car.drive(-100)
        assert False, "Negative distance should raise a ValueError."
    except ValueError:
        assert True


@pytest.mark.timeout(1.0)
def test_refuel_positive_liters():
    """Test refuel method with positive liters."""
    car.fuel = 7.39
    car.refuel(10)
    assert car.fuel == 17.39


@pytest.mark.timeout(1.0)
def test_refuel_negative_liters():
    """Test refuel method with negative liters."""
    car.refuel(-5)
    assert car.fuel == 17.39


@pytest.mark.timeout(1.0)
def test_refuel_zero_liters():
    """Test refuel method with zero liters."""
    car.refuel(0)
    assert car.fuel == 17.39


@pytest.mark.timeout(1.0)
def test_refuel_over_tank_capacity():
    """Test refuel method with liters that exceed the tank size."""
    car.refuel(40)
    assert car.fuel == 50
