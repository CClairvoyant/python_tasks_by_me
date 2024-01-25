Fail Gitis: `EX/ex11_cars/cars.py`

Ülesande eesmärgiks on tutvustada objektorienteeritud programmeerimist. Siin osas tuleb teha klass, mis hoiab infot auto
kohta.
OOPi kohta võid lugeda [siit](https://pydoc.pages.taltech.ee/oop/classes.html). Lahendamisel võivad abiks olla ka
[filter](https://pydoc.pages.taltech.ee/function/anon_function/filter.html) ning
[map](https://pydoc.pages.taltech.ee/function/anon_function/map.html) funktsioonid.


## Klass `Car`

* `__init__(self, make: str, model: str, fuel_consumption: float, features: list[str])`

Konstruktor, mis loob auto objekti antud parameetritega.
Igal autol on mark, mudel, kütusekulu (mitu liitrit kütust kulub 100km läbimiseks) ning lisafunktsioonid.
Siit midagi eemaldada ei tohi, kuid soovi korral juurde võib panna.
Konstruktori kohta võid lugeda näiteks [PyDoci](https://pydoc.pages.taltech.ee/oop/classes.html)
ja [GeeksForGeeks](https://www.geeksforgeeks.org/__init__-in-python/) lehelt.

* `__eq__(self, other)`

See meetod aitab objektide võrdlemisega. Ära seda muuda.

* `__hash__(self) -> int`

See meetod võimaldab objekti panna hulka ning sõnastikku (võtmena). Ära seda muuda.

* `__repr__(self) -> str`

See meetod võimaldab objekti kuvada loetaval kujul (näiteks kasutades `print()`). Seda pole vaja muuta.

<br>

Soovi korral võid spetsiaalsete meetodite kohta
lugeda [PyDoci](https://pydoc.pages.taltech.ee/oop/oop-special-methods.html)
või [rszalski.github.io](https://rszalski.github.io/magicmethods/) lehelt.
Inglise keeles on neil järgmised nimetused: magic methods, dunder methods, double underscore methods.

## Funktsioonid

* `sort_cars_by_make(cars: list[Car]) -> list[Car]`

Tagasta autode list, mis on sorteeritud autode markide järgi (tähestiku järjekorras).
Kui mitmel autol on sama mark, siis sorteeri need mudeli järgi (tähestiku järjekorras).
Sorteerimise kohta võid lugeda [siit](https://pydoc.pages.taltech.ee/data_structures/list/sorting.html).

* `find_cars_by_make_and_model(cars: list[Car], make: str, model: str) -> list[Car]`

Leia autod, millel on antud mark ja mudel. Tagasta need autod listis. Järjekord ei ole oluline.

* `find_cars_by_feature(cars: list[Car], feature: str) -> list[Car]`

Leia autod, millel on antud lisafunktsioon. Tagasta need autod listis. Sorteeri autod markide järgi (tähestiku
järjekorras).
Kui mitmel autol on sama mark, siis sorteeri need mudeli järgi (tähestiku järjekorras).

* `fuel_needed(car: Car, distance: int) -> float`

Arvuta auto keskmise kütusekulu põhjal, kui palju kütust kulub sellel autol antud vahemaa läbimiseks. Tagasta tulemus.

* `calculate_average_fuel_consumption(cars: list[Car]) -> float`

Arvuta antud autode kütusekulude keskmine suurus. Tagasta tulemus.

* `most_popular_feature(cars: list[Car]) -> str`

Leia kõige populaarsem lisafunktsioon. Kui mitu lisafunktsiooni on sama populaarsed, siis pole oluline, millise neist
tagastad.

* `write_cars_to_file(cars: list[Car], file_name: str)`

Kirjuta Car objektid faili JSON formaadis. Selleks tee sõnastik nende objektide attribuutidest ning seejärel
kasuta `json` teeki,
et see sõnastik JSON faili kirjutada.
Näited selle teegi kasutamisest võid
leida [stack overflowist](https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file).

Näiteks kui `cars` on järgmine list:

```python
cars = [
    Car("Toyota", "Corolla", 5.5, ["ABS", "Airbag", "Air conditioning"]),
    Car("Toyota", "Yaris", 4.5, ["ABS", "Airbag", "Air conditioning"])
]
```

siis peaks faili sisu tulema selline:

```json
[
  {
    "make": "Toyota",
    "model": "Corolla",
    "fuel_consumption": 5.5,
    "features": [
      "ABS",
      "Airbag",
      "Air conditioning"
    ]
  },
  {
    "make": "Toyota",
    "model": "Yaris",
    "fuel_consumption": 4.5,
    "features": [
      "ABS",
      "Airbag",
      "Air conditioning"
    ]
  }
]
```
Vastava taande saavutamiseks peaks kasutama argumenti `indent=2` `json.dump` funktsiooni välja kutsumisel.

* `read_cars_from_file(file_name: str) -> list[Car]`

Siin funktsioonis tuleb saavutada täpselt vastupidine funktsionaalsus võrreldes eelmise funktsiooniga. See tähendab,
et on tarvis JSON failist lugeda Car objektide info sõnastikku, sellest luua Car objektid antud väärtustega, panna need
listi ning tagastada see list.
Näiteid JSON failist lugemisest võid leida
samuti [stack overflowist](https://stackoverflow.com/questions/20199126/reading-json-from-a-file).

## Mall

```python
"""Cars."""

import json


class Car:
    """Car class."""

    def __init__(self, make: str, model: str, fuel_consumption: float, features: list[str]):
        """
        Initialize a Car object.

        :param make: The make of the car.
        :param model: The model of the car.
        :param fuel_consumption: The fuel consumption of the car in liters per 100 kilometers.
        :param features: The features of the car.
        """
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.features = features

    def __eq__(self, other):
        """Check if two cars are equal. Don't change this method."""
        return type(other) is self.__class__ and \
            self.make == other.make and \
            self.model == other.model and \
            self.fuel_consumption == other.fuel_consumption and \
            self.features == other.features

    def __hash__(self) -> int:
        """Allow a Car object to be used as a key in a dictionary. Don't change this method."""
        return hash((self.make, self.model, self.fuel_consumption, tuple(self.features)))

    def __repr__(self) -> str:
        """Return a string representation of the Car object. It is not necessary to change this method."""
        return f'{self.make} {self.model}'


def sort_cars_by_make(cars: list[Car]) -> list[Car]:
    """
    Sort the given list of cars by make alphabetically.

    If multiple cars have the same make, sort them by model alphabetically.
    If those cars also have the same model, then the order of those cars doesn't matter.

    :param cars: The list of cars to sort.
    :return: The sorted list of cars.
    """
    pass


def find_cars_by_make_and_model(cars: list[Car], make: str, model: str) -> list[Car]:
    """
    Find all cars with the given make and model. The order of the cars in the returned list does not matter.

    :param cars: The list of cars to search through.
    :param make: The given make.
    :param model: The given model.
    :return: The list of cars with the given make and model.
    """
    pass


def find_cars_by_feature(cars: list[Car], feature: str) -> list[Car]:
    """
    Find all cars that have the given feature.

    Sort the resulting list of cars by make alphabetically. If multiple cars have the same make,
    sort them by model alphabetically. If those cars also have the same model, then the order
    of those cars doesn't matter.

    :param cars: The list of cars to search through.
    :param feature: The given feature.
    :return: The list of cars that have the specified feature.
    """
    pass


def fuel_needed(car: Car, distance: int) -> float:
    """
    Calculate the amount of fuel needed for a given distance based on the car's fuel consumption.

    :param car: The car object representing the vehicle.
    :param distance: The distance in kilometers for which the fuel amount is calculated.
    :return: The amount of fuel needed in liters.
    """
    pass


def calculate_average_fuel_consumption(cars: list[Car]) -> float:
    """
    Calculate the average fuel consumption of the given cars.

    The average fuel consumption is the sum of the fuel consumption of all the cars divided by the number of cars.

    :param cars: The list of cars to calculate the average fuel consumption for.
    :return: The average fuel consumption of the given cars.
    """
    pass


def most_popular_feature(cars: list[Car]) -> str:
    """
    Find the most popular feature among the given cars.

    The most popular feature is the feature that occurs the most times among all the cars.
    If multiple features occur the same number of times, return any of them.

    :param cars: The list of cars to search through.
    :return: The most popular feature among the given cars.
    """
    pass


def write_cars_to_file(cars: list[Car], file_name: str):
    """
    Write the given list of cars to the given file in JSON format.

    The cars should be written as a list of dictionaries, where each dictionary represents a car.
    The keys of the dictionaries should be the attributes of the car and the values should be
    the values of the attributes. The order of the cars in the list should stay the same.

    :param cars: The list of cars to write to the file.
    :param file_name: The name of the file to write the cars to.
    """
    pass


def read_cars_from_file(file_name: str) -> list[Car]:
    """
    Read a list of cars from the given file in JSON format.

    The file should contain a list of dictionaries where each dictionary represents a car.
    The keys of the dictionaries should be the attributes of the car and the values should be
    the values of the attributes. The order of the cars in the list should stay the same.

    :param file_name: The name of the file to read the cars from.
    :return: The list of cars read from the file.
    """
    pass


if __name__ == '__main__':
    list_of_cars = [Car('BMW', 'X5', 12.3, ['leather', 'heated seats', 'GPS']),
                    Car('BMW', 'X6', 7.2, ['leather', 'heated seats', 'panorama', 'GPS']),
                    Car('Audi', 'A6', 9.93, ['leather', 'heated seats', 'panorama', 'GPS']),
                    Car('Audi', 'A7', 15.21, ['leather', 'heated seats', 'panorama', 'sport package']),
                    Car('Mercedes', 'S500', 10.6, ['leather', 'panorama', 'sport package',
                                                   'premium sound system'])]

    print(list_of_cars)  # [BMW X5, BMW X6, Audi A6, Audi A7, Mercedes S500]
    print(sort_cars_by_make(list_of_cars))  # [Audi A6, Audi A7, BMW X5, BMW X6, Mercedes S500]
    print()

    print(find_cars_by_make_and_model(list_of_cars, 'BMW', 'X6'))  # [BMW X6]
    print(find_cars_by_feature(list_of_cars, 'panorama'))  # [Audi A6, Audi A7, BMW X6, Mercedes S500]
    print()

    print(fuel_needed(list_of_cars[0], 150))  # 18.45; might be a little different due to floating point arithmetic errors
    print(calculate_average_fuel_consumption(list_of_cars))  # 11.048
    print()

    print(most_popular_feature(list_of_cars))  # leather
    write_cars_to_file(list_of_cars, 'cars.json')
    print(read_cars_from_file('cars.json'))  # [BMW X5, BMW X6, Audi A6, Audi A7, Mercedes S500]

```