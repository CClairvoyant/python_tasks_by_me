Fail Gitis: `XP/xp04_decorators/decorators.py`

### Kasulikud lingid:
* [Dekoraatorid](https://www.programiz.com/python-programming/decorator)
* [*args ja **kwargs](https://www.geeksforgeeks.org/args-kwargs-python/)
* [inspect.Signature viimase dekoraatori jaoks](https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object)

## Sissejuhatus
Dekoraatorid on funktsioonid, mis võtavad argumendiks funktsiooni ja tagastavad funktsiooni.
Dekoraatorid on kasulikud, kui soovime funktsiooni käitumist muuta, kuid ei soovi/saa funktsiooni ennast muuta.

Näide dekoraatorist:
```python
def decorator(func):
  def wrapper(*args, **kwargs):
    # siia saab kirjutada koodi, mis käivitub enne funktsiooni
    result = func(*args, **kwargs)  # siin käivitatakse dekoreeritav funktsioon
    # siia saab kirjutada koodi, mis käivitub pärast funktsiooni
    return result
  return wrapper
```

Sisemise funktsiooni `wrapper` parameetrid peavad olema samad, mis dekoreeritaval funktsioonil,
kuid kui me ei tea, milliseid argumente dekoreeritav funktsioon võtab või kui tahame, et oleks võimalik
dekoreerida funktsioone, mis võtavad ükskõik kui palju ning ükskõik milliseid argumente,
siis saame kasutada `*args` ja `**kwargs` parameetreid.

Näiteks on tänu `*args` ja `**kwargs` parameetritele võimalik ülevalolevat dekoraatorit kasutada nii:
```python
@decorator
def my_func(n: int):
  return n * 2

my_func(2)
```
kui ka nii:
```python
@decorator
def my_func(s: str, *, l: list[str]):
  return s + "".join(l)

my_func("Hello", l=["a", "b", "c"])
```

## Ülesanne
Siin ülesandes tuleb valmis kirjutada 6 dekoraatorit. Dekoraatorid on järjest keerulisemad, seega on soovitatav
neid lahendada järjest.

### 1. `@double`
Loo dekoraator `double`, mis korrutab mingi funktsiooni tulemuse kahega.


### 2. `@stopwatch`
Loo dekoraator `stopwatch`, mis mõõdab ja prindib välja, kui kaua mingi funktsioon töötab.
Prinditud väljund peaks olema selline: ```"It took [time] seconds for [function_name] to run"```,
kus `[time]` on aeg sekundites ja `[function_name]` on funktsiooni nimi.


### 3. `@memoize`
Memoiseerimine on tehnika, kus ajaliselt kuluka funktsiooni tulemusi salvestatakse, et neid hiljem uuesti kasutada ja
mitte funktsiooni korduvalt välja kutsuda.

Loo dekoraator `memoize`, mis salvestab funktsiooni tulemusi ning kui funktsioonile antakse samad argumendid,
mida on juba varem kasutatud, siis funktsiooni välja kutsumise asemel tagastab salvestatud tulemuse.


### 4. `@read_data`
Loo dekoraator `read_data`, mis loeb faili "data.txt" sisu järjendisse (iga element järjendis olgu üks rida failist)
ja annab selle dekoreeritavale funktsioonile esimese argumendina, enne teisi argumente.


### 5. `@catch`
Loo dekoraator `catch`, mis püüab kinni dekoreeritava funktsiooni käivitamisel tekkivad erindid.

`catch` peab toetama järgmiseid kasutusviise:
* Dekoraatorit kasutatakse ilma argumentideta, nt. `@catch`. Sellisel juhul püütakse kinni kõik erindid.
* Dekoraatorit kasutatakse ühe erindi klassiga, nt. `@catch(TypeError)`. Sellisel juhul püütakse kinni ainult
  `TypeError` erindid.
* Dekoraatorit kasutatakse mitme erindi klassiga, nt. `@catch(KeyError, ValueError)`. Sellisel juhul püütakse kinni
  nii `KeyError` kui ka `ValueError` erindid.


### 6. `@enforce_types`
Loo dekoraator `enforce_types`, mis kontrollib, et dekoreeritav funktsioon saaks õiget tüüpi argumente
ning tagastaks õiget tüüpi väärtuse. Õige tüübi alla peaks lugema kõik märgitud tüübi alamklassid (ning muidugi ka see klass ise).

Kui dekoreeritav funktsioon saab valet tüüpi argumendi, siis tõstata `TypeError` erind sõnumiga
`"Argument '[argument_name]' must be of type [expected_type], but was [value] of type [actual_type]"`, kus
`[argument_name]` on valet tüüpi argumendi nimi, `[expected_type]` on oodatav tüüp, `[value]` on argumendi väärtuse
esitus, mis on saadud `repr` funktsiooni abil ja `[actual_type]` on argumendi tegelik tüüp.

Kui dekoreeritav funktsioon tagastab valet tüüpi väärtuse, siis tõstata `TypeError` erind sõnumiga
`"Returned value must be of type [expected_type], but was [value] of type [actual_type]"`, kus
`[expected_type]` on oodatav tüüp, `[value]` on tagastusväärtuse esitus, mis on saadud `repr` funktsiooni abil
ja `[actual_type]` on tagastusväärtuse tegelik tüüp.

Kui mingil parameetril või tagastusel on mitu lubatud tüüpi, siis peab veasõnumis olema loetletud kõik võimalikud tüübid.
Näiteks kui parameetri tüüp on `int | float | str | bool`, siis peab veasõnum olema
`"Argument '[argument_name]' must be of type int, float, str or bool, but was [value] of type [actual_type]"`.
Mitme võimaliku tagastusväärtuse tüübi korral peab veasõnum muutuma sama loogikaga.

Kui mingil parameetril või tagastusväärtusel ei ole tüüpi määratud, siis see võib olla ükskõik millist tüüpi.

Erindid, mis tekivad dekoreeritava funktsiooni käivitamisel, peavad ikka tekkima, kui argumentide tüübid on õiged.

Selle lahendamisel on soovituslik kasutada `inspect` moodulit, et saada dekoreeritava funktsiooni parameetrite
ja tagastusväärtuse tüübid.


## Mall

```py
"""XP - decorators."""

import time


def double(func):
    """
    Double the return value of a function.

    :param func: The decorated function.
    :return: Inner function.
    """
    pass


def stopwatch(func):
    """
    Print the runtime of a function.

    It should be printed out like: "It took [time] seconds for [function_name] to run",
    where [time] is the number of seconds (with the precision of at least 5 decimal places)
    it took for the function to run and [function_name] is the name of the function.
    The function's return value should not be affected.
    :param func: The decorated function.
    :return: Inner function.
    """
    pass


def memoize(func):
    """
    Cache the return value of a function.

    Memoization is an optimisation technique used primarily to speed up computer programs
    by storing the results of expensive function calls and returning the cached result
    when the same inputs occur again.
    For efficiency purposes, you can assume, that the function only takes one argument,
    and that the argument is an integer.
    :param func: The decorated function.
    :return: Inner function.
    """
    pass


def read_data(func):
    """
    Read the data from the file "data.txt" and pass it to the function.

    The data must be passed as a list of strings, where each string is a line from the file.
    It also must be passed as the first argument to the function, followed by any other given arguments.
    :param func: The decorated function.
    :return: Inner function.
    """
    pass


def catch(*error_classes):
    """
    Catch the specified exceptions.

    If the function raises one of the specified exceptions, return a tuple of (1, exception_class),
    where exception_class is the type of the exception that was raised. Otherwise, return a tuple of (0, result),
    where result is the result of the function.

    This decorator must be able to handle the following cases:
    1. The decorator is used with no arguments, e.g. @catch. Such usage should catch all exceptions.
    2. The decorator is used with one argument, e.g. @catch(ValueError).
    3. The decorator is used with multiple arguments, e.g. @catch(KeyError, TypeError).
    :param error_classes: The exceptions to catch.
    :return: Inner function.
    """
    pass


def enforce_types(func):
    """
    Enforce the types of the function's parameters and return value.
  
    If the function is called with an argument of the wrong type, raise a TypeError with the message:
    "Argument '[argument_name]' must be of type [expected_type], but was [value] of type [actual_type]".
    If the function returns a value of the wrong type, raise a TypeError with the message:
    "Returned value must be of type [expected_type], but was [value] of type [actual_type]".
    Values should be represented as strings using the repr() function.
  
    If an argument or the return value can be of multiple types, then the [expected_type]
    in the error message should be "[type_1], [type_2], ..., [type_(n-1)] or [type_n]".
    For example if the type annotation for an argument is int | float | str | bool, then the error message should be
    "Argument '[argument_name]' must be of type int, float, str or bool, but was [value] of type [actual_type]".
  
    If there's no type annotation for a parameter or the return value, then it can be of any type.
  
    Using the inspect module to get the function's signature and annotations is recommended.
  
    Exceptions, that happen during the execution of the function, should still occur normally,
    if the argument types are correct.
    :param func: The decorated function.
    :return: Inner function.
    """
    pass


#  Everything below is just for testing purposes, tester does not care what you do with them.
#    |           |           |           |           |           |           |           |
#    V           V           V           V           V           V           V           V


@double
def double_me(element):
    """Test function for @double."""
    return element


@stopwatch
def measure_me():
    """Test function for @stopwatch."""
    time.sleep(0.21)
    return 5


@memoize
def fibonacci(n: int):
    """Test function for @memoize."""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@catch(KeyError, ZeroDivisionError)
def error_func(iterable):
    """Test function for @catch."""
    return iterable[2]


@read_data
def process_file_contents(data: list, prefix: str = ""):
    """Test function for @read_data."""
    return [prefix + line for line in data]


@enforce_types
def no_more_duck_typing(num: int | float, g: None) -> str:
    """Test function for @enforce_types."""
    return str(num)


if __name__ == '__main__':
    print(double_me(5))  # 10
    print(double_me("Hello"))  # HelloHello
    print()
  
    print(measure_me())  # It took 0.21... seconds for measure_me to run
    # 5
    print()
  
    print(fibonacci(35))  # 9227465
    # Probably takes about 2 seconds without memoization and under 50 microseconds with memoization
    print()
  
    print(error_func("Hello"))  # (0, 'l')
    print(error_func([5, 6, 7]))  # (0, 7)
    print(error_func({}))  # (1, <class 'KeyError'>)
  
    try:
        print(error_func([]))
        print("IndexError should not be caught at this situation.")
    except IndexError:
        print("IndexError was thrown (as it should).")
  
    print()
  
    print(process_file_contents("hi"))  # This assumes you have a file "data.txt". It should print out the file
    # contents in a list with "hi" in front of each line like ["hiLine 1", "hiLine 2", ...].
    print(process_file_contents())  # This should just print out the file contents in a list.
    print()
  
    print(no_more_duck_typing(5, None))  # 5
  
    try:
        print(no_more_duck_typing("5", None))
        print("TypeError should be thrown, but wasn't.")
    except TypeError as e:
        print(e)  # Argument 'num' must be of type int or float, but was '5' of type str
  
    try:
        print(no_more_duck_typing(5.0, 2))
        print("TypeError should be thrown, but wasn't.")
    except TypeError as e:
        print(e)  # Argument 'g' must be of type NoneType, but was 2 of type int

```
