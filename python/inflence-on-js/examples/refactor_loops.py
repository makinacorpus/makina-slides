def initials(person):
    return person["given_name"][0] + person["family_name"][1]


def some_random_function(a, b, records):
    data = a + b
    transformed_records = []
    for record in records:
        transformed_record = dict(record)
        transformed_record["initials"] = initials(transformed_record)
        transformed_records.append(transformed_record)
    do_something_with(data, transformed_records)


def do_something_with(data, records):
    pass


records = [
    {"family_name": "Van Rossum", "given_name": "Guido"},
    {"family_name": "Lovelace", "given_name": "Ada"},
    {"family_name": "Knuth", "given_name": "Donald"},
]


some_random_function(1, 2, records)
