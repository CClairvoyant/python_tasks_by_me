class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def sort_people_dictionary_by_last_name(people: dict[str, str]):
    return dict(sorted(people.items(), key=lambda item: item[1]))


def sort_people_dictionary_2_by_last_name(people: dict[int, tuple[str, str]]):
    return dict(sorted(people.items(), key=lambda item: item[1][1]))


def sort_people_objects_by_last_name(people: list[Person]):
    return sorted(people, key=lambda person: person.last_name)


if __name__ == '__main__':
    people_dict = {
        'John': 'Doe',
        'John': 'Smith',  # Dictionary keys must be unique, so this will overwrite the previous entry!
        'Jane': 'Smith',
        'Adam': 'Fisher',
        'Eve': 'Fisher',
        'Oliver': 'Jones'
    }

    # This fixes the problem of duplicate keys, but the structure is not ideal for sorting.
    people_dict_2 = {
        1: ('John', 'Doe'),
        2: ('John', 'Smith'),
        3: ('Jane', 'Smith'),
        4: ('Adam', 'Fisher'),
        5: ('Eve', 'Fisher'),
        6: ('Oliver', 'Jones')
    }

    # Person objects don't have these problems.
    people_objects = [
        Person('John', 'Doe'),
        Person('John', 'Smith'),
        Person('Jane', 'Smith'),
        Person('Adam', 'Fisher'),
        Person('Eve', 'Fisher'),
        Person('Oliver', 'Jones')
    ]

    print(sort_people_dictionary_by_last_name(people_dict))  # John Doe is missing, because it was overwritten.
    print(sort_people_dictionary_2_by_last_name(people_dict_2))
    print(sort_people_objects_by_last_name(people_objects))
