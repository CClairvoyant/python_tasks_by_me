# EX11 - OOP

## Ülesanded

Kaust Gitis: `EX/ex11_oop`

---
<details>
<summary><strong>Kohustuslik osa - Cars</strong></summary>


Fail Gitis: `EX/ex11_oop/cars.py`

Ülesande eesmärgiks on tutvustada objektorienteeritud programmeerimist. Siin osas tuleb teha klass, mis hoiab infot auto
kohta.
OOPi kohta võid lugeda [siit](https://pydoc.pages.taltech.ee/oop/classes.html).

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
lugeda [PyDoci](https://pydoc.pages.taltech.ee/oop/oop_special_methods.html)
või [rszalski.github.io](https://rszalski.github.io/magicmethods/) lehelt.
Inglise keeles on neil järgmised nimetused: magic methods, dunder methods, double underscore methods.

## Funktsioonid

* `sort_cars_by_make(cars: list[Car]) -> list[Car]`

Tagasta autode list, mis on sorteeritud autode markide järgi (tähestiku järjekorras).
Kui mitmel autol on sama mark, siis sorteeri need mudeli järgi (tähestiku järjekorras).

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
        return type(other) == self.__class__ and \
            self.make == other.make and \
            self.model == other.model and \
            self.fuel_consumption == other.fuel_consumption and \
            self.features == other.features

    def __hash__(self) -> int:
        """Allow this object to be used as a key in a dictionary. Don't change this method."""
        return super().__hash__()

    def __repr__(self) -> str:
        """Return a string representation of the Car object. It is not necessary to change this method."""
        return f'{self.make} {self.model}'


def sort_cars_by_make(cars: list[Car]) -> list[Car]:
    """
    Sort the given list of cars by make alphabetically. If multiple cars have the same make, sort them by model alphabetically.
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
    Find all cars that have the given feature. Sort the resulting list of cars by make alphabetically. If multiple
    cars have the same make, sort them by model alphabetically. If those cars also have the same model, then the order
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
    Calculate the average fuel consumption of the given cars. The average fuel consumption is the sum of the fuel
    consumption of all the cars divided by the number of cars.

    :param cars: The list of cars to calculate the average fuel consumption for.
    :return: The average fuel consumption of the given cars.
    """
    pass


def most_popular_feature(cars: list[Car]) -> str:
    """
    Find the most popular feature among the given cars. The most popular feature is the feature that occurs the most
    times among all the cars. If multiple features occur the same number of times, return any of them.

    :param cars: The list of cars to search through.
    :return: The most popular feature among the given cars.
    """
    pass


def write_cars_to_file(cars: list[Car], file_name: str):
    """
    Write the given list of cars to the given file in JSON format. The cars should be written as a list of dictionaries
    where each dictionary represents a car. The keys of the dictionaries should be the attributes of the car and the
    values should be the values of the attributes. The order of the cars in the list should stay the same.

    :param cars: The list of cars to write to the file.
    :param file_name: The name of the file to write the cars to.
    """
    pass


def read_cars_from_file(file_name: str) -> list[Car]:
    """
    Read a list of cars from the given file in JSON format. The file should contain a list of dictionaries where each
    dictionary represents a car. The keys of the dictionaries should be the attributes of the car and the values should
    be the values of the attributes. The order of the cars in the list should stay the same.

    :param file_name: The name of the file to read the cars from.
    :return: The list of cars read from the file.
    """
    pass


if __name__ == '__main__':
    cars = [Car('BMW', 'X5', 12.3, ['leather', 'heated seats', 'GPS']),
            Car('BMW', 'X6', 7.2, ['leather', 'heated seats', 'panorama', 'GPS']),
            Car('Audi', 'A6', 9.93, ['leather', 'heated seats', 'panorama', 'GPS']),
            Car('Audi', 'A7', 15.21, ['leather', 'heated seats', 'panorama', 'sport package']),
            Car('Mercedes', 'S500', 10.6, ['leather', 'heated seats', 'panorama', 'sport package',
                                           'premium sound system'])]

    print(cars)  # [BMW X5, BMW X6, Audi A6, Audi A7, Mercedes S500]
    print(sort_cars_by_make(cars))  # [Audi A6, Audi A7, BMW X5, BMW X6, Mercedes S500]
    print()

    print(find_cars_by_make_and_model(cars, 'BMW', 'X6'))  # [BMW X6]
    print(find_cars_by_feature(cars, 'panorama'))  # [Audi A6, Audi A7, BMW X6, Mercedes S500]
    print()

    print(fuel_needed(cars[0], 150))  # 18.45; might be a little different due to floating point arithmetic errors
    print(calculate_average_fuel_consumption(cars))  # 11.048
    print()

    print(most_popular_feature(cars))  # leather
    write_cars_to_file(cars, 'cars.json')
    print(read_cars_from_file('cars.json'))  # [BMW X5, BMW X6, Audi A6, Audi A7, Mercedes S500]

```

</details>

---

<details>
<summary><strong>Vabatahtlik osa - Books</strong></summary>

Fail Gitis: `EX/ex11_oop/books.py`

Siin osas tuleb teha klass, mis hoiab infot raamatu kohta.
OOPi kohta võid lugeda [siit](https://pydoc.pages.taltech.ee/oop/classes.html).

## Klass `Book`

* `__init__(self, title: str, author: str, pages: int, sales: int, genres: list[str], publication_year: int)`

Konstruktor, mis loob raamatu objekti antud parameetritega.
Igal raamatul on pealkiri, autor, lehekülgede arv, müüdud eksemplaride arv, žanrid ning ilmumisaasta.
Siit midagi eemaldada ei tohi, kuid soovi korral juurde võib panna.

* `__eq__(self, other) -> bool`

See meetod aitab objektide võrdlemisega. Ära seda muuda.

* `__hash__(self) -> int`

See meetod võimaldab objekti panna hulka ning sõnastikku (võtmena). Ära seda muuda.

* `__repr__(self) -> str`

See meetod võimaldab objekti kuvada loetaval kujul (näiteks kasutades `print()`). Seda pole vaja muuta.

## Funktsioonid

* `author_book_count(library: list[Book], author: str) -> int`

Leia, mitu raamatut on antud autor kirjutanud.

* `author_page_count(library: list[Book], author: str) -> int`

Leia, mitu lehekülge on antud autor kirjutanud.

* `most_popular_book(library: list[Book]) -> Book`

Leia raamat, mis on kõige populaarsem (kõige suurem müüdud eksemplaride arv).

* `most_popular_author(library: list[Book]) -> str`

Leia autor, kelle raamatuid on kõige rohkem müüdud. Kui mitmel autoril on sama palju müüdud raamatuid,
siis pole oluline, millise neist tagastad.

* `average_author_book_length(library: list[Book], author: str) -> float`

Leia autori keskmine raamatu pikkus (lehekülgede arv).

* `find_best_selling_genre(library: list[Book]) -> str`

Leia kõige populaarsem žanr. Kui mitu žanrit on sama populaarsed, siis pole oluline, millise neist tagastad.

* `find_books_by_genre_and_year(library: list[Book], genre: str, year: int) -> list[Book]`

Leia raamatud, mis on antud žanrist ja ilmusid antud aastal. Tagasta need raamatud listis, mis on sorteeritud
müüdud eksemplaride arvu järgi (kahanevalt) ning kui mitmel raamatul on sama palju müüdud eksemplare, siis
sorteeri need pealkirja järgi (tähestiku järjekorras).

* `most_popular_author_per_century(library: list[Book]) -> dict[int, str]`

Leia iga sajandi populaarseim autor ehk autor, kes on müünud kõige rohkem vastaval sajandil avaldatud raamatuid.
Tagasta tulemus sõnastikuna, kus võtmeteks on sajandite numbrid ja väärtusteks on autorite nimed.
Kui mitmel autoril on sama palju müüke, siis pole vahet, milline sõnastikku satub.

Sõnastik peaks välja nägema umbes selline:

```python
{
    19: "Jane Austen",
    20: "Stephen King",
    21: "J. K. Rowling"
}
```

* `correct_titles_and_count_books(library: list[Book]) -> dict[Book, int]`

Süsteemivea tõttu on mõne raamatu pealkirjast üks täht ära kadunud. Sinu ülesanne on leida kõik sellised raamatud
ning parandada nende pealkirjad. Tagasta sõnastik, kus võtmeteks on parandatud pealkirjadega raamatud
ja väärtusteks on nende raamatute arv selles listis.

Pealkirja tuleks parandada siis, kui listis leidub teine raamat, millel on täpselt samad omadused (autor, lehekülgede
arv, müüdud eksemplaride arv, žanrid, ilmumisaasta), kuid pealkirjas on täpselt üks täht lisaks.

Näiteks kui list on järgmine:

```python
library = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925),
    Book("The Great Gatsb", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925),
    Book("Tender Is the Night", "F. Scott Fitzgerald", 320, 90_000, ["Classic", "Fiction"], 1934),
    Book("Tender Is the Nigh", "F. Scott Fitzgerald", 321, 90_000, ["Classic", "Fiction"], 1934)
]
```

siis tuleks parandada raamatute "The Great Gatsb" pealkiri "The Great Gatsby"-ks, kuid "Tender Is the Nigh" pealkirja
ei tohiks muuta, sest teist raamatut, millel on samad omadused (peale pealkirja), ei leidu.

Tagastatav sõnastik peaks välja nägema selline:

```python
result = {
    Book("The Great Gatsby", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925): 2,
    Book("Tender Is the Night", "F. Scott Fitzgerald", 320, 90_000, ["Classic", "Fiction"], 1934): 1,
    Book("Tender Is the Nigh", "F. Scott Fitzgerald", 321, 90_000, ["Classic", "Fiction"], 1934): 1
}
```

Lisaks, collections teegi Counter klass tuleks siin ülesandes kasuks, kuid sellest hoolimata pole selle kasutamine
kahjuks lubatud.

## Mall

```python
"""Books."""


class Book:
    """Book class."""

    def __init__(self, title: str, author: str, pages: int, sales: int, genres: list[str], publication_year: int):
        """
        Initialize a Book object.

        :param title: The title of the book.
        :param author: The author of the book.
        :param pages: The amount of pages in the book.
        :param sales: The amount of times the book has been sold.
        :param genres: The genres of the book.
        :param publication_year: The year the book was published.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.sales = sales
        self.genres = genres
        self.year = publication_year

    def __eq__(self, other) -> bool:
        """Return True if the Book objects are equal."""
        return type(other) == self.__class__ and \
            self.title == other.title and \
            self.author == other.author and \
            self.pages == other.pages and \
            self.sales == other.sales and \
            self.genres == other.genres and \
            self.year == other.year

    def __hash__(self) -> int:
        """Allow a Book object to be used as a key in a dictionary. Don't change this method."""
        return hash((self.title, self.author, self.pages, self.sales, tuple(self.genres), self.year))

    def __repr__(self) -> str:
        """Return a string representation of the Book object."""
        return f"{self.title} by {self.author}"


def author_book_count(library: list[Book], author: str) -> int:
    """
    Find the number of books written by the given author.

    :param library: The list of books to search through.
    :param author: The given author.
    :return: The amount of books written by the author.
    """
    pass


def author_page_count(library: list[Book], author: str) -> int:
    """
    Find the total number of pages written by the given author.

    :param library: The list of books to search through.
    :param author: The given author.
    :return: The total number of pages written by the author.
    """
    pass


def most_popular_book(library: list[Book]) -> Book:
    """
    Find the book with the most sales.

    :param library: The list of books.
    :return: The Book object with the most sales.
    """
    pass


def most_popular_author(library: list[Book]) -> str:
    """
    Find the author with the most sales. If two or more authors have the same amount of sales,
    it doesn't matter which one is returned.

    :param library: The list of books.
    :return: The author with the most sales.
    """
    pass


def average_author_book_length(library: list[Book], author: str) -> float:
    """
    Find the average length of a book (amount of pages), that is written by the given author.

    :param library: The list of books.
    :param author: The given author.
    :return: The average length of the author's books.
    """
    pass


def find_best_selling_genre(library: list[Book]) -> str:
    """
    Find the genre, that has the most sales. If two or more genres have the same amount of sales, return either one.

    :param library: The list of books.
    :return: The genre with the most total sales.
    """
    pass


def find_books_by_genre_and_year(library: list[Book], genre: str, year: int) -> list[Book]:
    """
    Find all books in the given list, that match the given year and genre.

    For the genre, you should check if the given genre is contained in the list of genres of the book.
    The result should be sorted by sales (descending) and if two or more books have the same sales,
    then sort them by title (alphabetically).

    :param library: The list of books to search from.
    :param genre: The genre to search for.
    :param year: The year to search for.
    :return: A list of books, that match the given genre and year, sorted by sales (descending) and title (alphabetically).
    """
    pass


def most_popular_author_per_century(library: list[Book]) -> dict[int, str]:
    """
    Find the author with the most sales for each century. If two or more authors have the same amount of sales,
    it doesn't matter which one is returned in the dictionary.

    :param library: The list of books.
    :return: A dictionary, where the keys are the centuries and the values are the authors with the most sales in that
    century.
    """
    pass


def correct_titles_and_count_books(library: list[Book]) -> dict[Book, int]:
    """
    Due to an unknown error, some of the titles in the given list of books have a letter missing.

    Your task is to correct the titles of the Book objects in the list and return a dictionary,
    where the Book objects are the keys and their occurrences in the list are the values.
    You should correct the book's title, if there is another book in the list,
    that has the exact same attributes, except for the title, which has a missing letter.

    For example, if the list of books has the following books:
    Book("The Great Gatsby", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925)
    Book("The Great Gatsb", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925)
    Book("Tender Is the Night", "F. Scott Fitzgerald", 320, 90_000, ["Classic", "Fiction"], 1934)
    Book("Tender Is the Nigh", "F. Scott Fitzgerald", 321, 90_000, ["Classic", "Fiction"], 1934)

    Then the second book's title should be corrected to "The Great Gatsby", while the fourth book's title should
    remain the same, because "Tender Is the Night" has a different amount of pages.

    :param library: The list of books.
    :return: The amount of books in the list.
    """
    pass


if __name__ == '__main__':
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925)
    book2 = Book("Tender Is the Night", "F. Scott Fitzgerald", 320, 90_000, ["Classic", "Fiction"], 1934)
    book3 = Book("The Beautiful and Damned", "F. Scott Fitzgerald", 348, 120_000, ["Classic", "Fiction"], 1922)
    book4 = Book("To Kill a Mockingbird", "Harper Lee", 324, 80_000, ["Fiction"], 1960)
    book5 = Book("Go Set a Watchman", "Harper Lee", 278, 70_000, ["Fiction"], 2015)
    book6 = Book("In Cold Blood", "Harper Lee", 368, 110_000, ["True Crime"], 1966)
    book7 = Book("1984", "George Orwell", 328, 200_000, ["Dystopian", "Fiction"], 1949)
    book8 = Book("Animal Farm", "George Orwell", 144, 70_000, ["Satire", "Fiction"], 1945)
    book9 = Book("Nineteen Eighty-Four", "George Orwell", 328, 95_000, ["Dystopian", "Fiction"], 1949)
    book10 = Book("Pride and Prejudice", "Jane Austen", 432, 85_000, ["Classic", "Romance"], 1813)

    book_list: list[Book] = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

    print(author_book_count(book_list, "Harper Lee"))  # 3
    print(author_page_count(book_list, "Harper Lee"))  # 970
    print(author_book_count(book_list, "Willy Wonka"))  # 0
    print(author_page_count(book_list, "Walter White"))  # 0
    print()

    print(most_popular_book(book_list))  # 1984 by George Orwell
    print(most_popular_author(book_list))  # George Orwell
    print(average_author_book_length(book_list, "Harper Lee"))  # 323.3333333333333
    print()

    print(find_best_selling_genre(book_list))  # Fiction
    print(find_books_by_genre_and_year(book_list, "Fiction",
                                       1949))  # [1984 by George Orwell, Nineteen Eighty-Four by George Orwell]
    print(most_popular_author_per_century(book_list))  # {19: 'Jane Austen', 20: 'George Orwell', 21: 'Harper Lee'}

```

</details>

---
