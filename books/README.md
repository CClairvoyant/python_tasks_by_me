Fail Gitis: `OP/op11_books/books.py`

Siin osas tuleb teha klass, mis hoiab infot raamatu kohta.
OOPi kohta võid lugeda [siit](https://pydoc.pages.taltech.ee/oop/classes.html). Lahendamisel võivad abiks olla ka
[sorted](https://pydoc.pages.taltech.ee/data_structures/list/sorting.html),
[filter](https://pydoc.pages.taltech.ee/function/anon_function/filter.html) ning
[map](https://pydoc.pages.taltech.ee/function/anon_function/map.html) funktsioonid.

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
        return type(other) is self.__class__ and
            self.title == other.title and
            self.author == other.author and
            self.pages == other.pages and
            self.sales == other.sales and
            self.genres == other.genres and
            self.year == other.year

    def __hash__(self) -> int:
        """Allow a Book object to be used as a key in a dictionary. Don't change this method."""
        return hash((self.title, self.author, self.pages, self.sales, tuple(self.genres), self.year))

    def __repr__(self) -> str:
        """Return a string representation of the Book object."""
        return f'"{self.title}" by {self.author}'


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
    Find the author with the most sales.

    If two or more authors have the same amount of sales, it doesn't matter which one is returned.

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
    Find the author with the most sales for each century.

    If two or more authors have the same amount of sales, it doesn't matter which one is returned in the dictionary.

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

    print(most_popular_book(book_list))  # "1984" by George Orwell
    print(most_popular_author(book_list))  # George Orwell
    print(average_author_book_length(book_list, "Harper Lee"))  # 323.3333333333333
    print()

    print(find_best_selling_genre(book_list))  # Fiction
    print(find_books_by_genre_and_year(book_list, "Fiction", 1949))  # ["1984" by George Orwell, "Nineteen Eighty-Four" by George Orwell]
    print(most_popular_author_per_century(book_list))  # {19: 'Jane Austen', 20: 'George Orwell', 21: 'Harper Lee'}
    print()

    print(correct_titles_and_count_books([
        Book("The Great Gatsby", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925),
        Book("The Great Gatsb", "F. Scott Fitzgerald", 218, 100_000, ["Classic", "Fiction"], 1925),
        Book("Tender Is the Night", "F. Scott Fitzgerald", 320, 90_000, ["Classic", "Fiction"], 1934),
        Book("Tender Is the Nigh", "F. Scott Fitzgerald", 321, 90_000, ["Classic", "Fiction"], 1934)
    ]))
    # {
    #     "The Great Gatsby" by F. Scott Fitzgerald: 2,
    #     "Tender Is the Night" by F. Scott Fitzgerald: 1,
    #     "Tender Is the Nigh" by F. Scott Fitzgerald: 1
    # }

```
