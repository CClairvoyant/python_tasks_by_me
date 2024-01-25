"""Cars."""


class Car:
    """Car class."""

    def __init__(self, mark: str, model: str, mileage: int, fuel_tank_size: int, fuel: float, fuel_consumption: float):
        """
        Initializes a new Car instance with the given attributes.

        Args:
            mark (str): The make or brand of the car.
            model (str): The model of the car.
            mileage (int): The number of kilometers the car has been driven.
            fuel_tank_size (int): The size of the car's fuel tank.
            fuel (float): The amount of fuel in the car's tank, in liters.
            fuel_consumption (float): The amount of fuel the car consumes per 100 km. After every 1,000 km
            driven, fuel consumption increases by 0.01.
        """
        self.mark = mark
        self.model = model
        self.mileage = mileage
        self.fuel_tank_size = fuel_tank_size
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> str:
        """
        Drive the specified distance with the car.

        If the car doesn't have enough fuel to drive the whole distance, return
        "The car died after driving {driven_km} kilometers.", if the car doesn't have any fuel, return
        "The car has no fuel.", otherwise return "The car has reached its destination.".
        In any case, drive as much of the distance as possible. Don't forget to reduce the fuel amount
        in the car and increase the fuel consumption if necessary. Also avoid making operations with
        floating point numbers as they often produce unexpected results. Round them to an integer instead
        The only variables, that should ever have float values, are the fuel consumption and fuel attributes.
        Both must be rounded to 2 decimal places after calculations.

        Args:
            distance (int): The distance to drive, in kilometers.

        Returns:
            A string indicating whether the car had enough fuel to complete the trip or not.

        Raises:
            ValueError: If the distance is negative.
        """
        pass

    def refuel(self, liters: int):
        """
        Refuels the car with a given amount of fuel, in liters.

        Args:
            liters (int): The amount of fuel to add to the car's fuel tank.
        """
        pass

    def __repr__(self):
        """
        Returns a string representation of the Car instance.

        Returns:
            str: A string describing the car's make, model, mileage, fuel tank capacity, fuel level,
            and fuel consumption.
        """
        return ("\n{} {} with:\n"
                "    mileage of {},\n"
                "    fuel tank capacity of {}l,\n"
                "    {}l of fuel and\n"
                "    fuel consumption of {}l/100km.")\
            .format(self.mark, self.model, self.mileage, self.fuel_tank_size, self.fuel, self.fuel_consumption)


if __name__ == '__main__':
    car = Car("Audi", "A7", 12459, 50, 12, 8.0)

    print(car.fuel_consumption)
    print(car.fuel_consumption)
    print(car.drive(140))
    print(car.drive(20))
    print(car.drive(1))
    print(car.drive(1))
    print(car.fuel_consumption)

    print(car)
