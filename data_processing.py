import os
import csv

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TableDB:
    def __init__(self):
        self.cities_database = []
        self.countries_database = []

    def insert_countries(self, table):
        self.countries_database.append(table)

    def insert_cities(self, table):
        self.cities_database.append(table)

    def search_countries(self, table_name):
        for item in self.countries_database:
            if item == table_name:
                return item
            return None

    def search_cities(self, table_name):
        for item in self.cities_database:
            if item == table_name:
                return item
            return None

    def __str__(self):
        return f"Current Countries: {self.countries_database}\
        \nCurrent Cities: {self.cities_database}"


class Table:
    def __init__(self, DB):
        self.cities_table = DB.cities_database
        self.countries_table = DB.countries_database

    def filter(self, condition, choice):
        filtered_list = []
        if choice.lower() == "cities":
            for item in self.cities_table:
                if condition(item):
                    filtered_list.append(item)
            return filtered_list
        if choice.lower() == "countries":
            for item in self.countries_table:
                if condition(item):
                    filtered_list.append(item)
            return filtered_list
        return None

    def aggregate(self, aggregation_key, aggregation_function, choice):
        values = []
        if choice.lower() == "cities":
            for item in self.cities_table:
                values.append(float(item[aggregation_key]))
            return aggregation_function(values)
        if choice.lower() == "countries":
            for item in self.countries_table:
                values.append(float(item[aggregation_key]))
            return aggregation_function(values)
        return None


# MAIN
italy_table = Table(TableDB())
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        italy_table.cities_table.append(dict(r))

with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        italy_table.countries_table.append(dict(r))

x = italy_table.filter(lambda x: float(x['latitude']) >= 60.0, "cities")
for stuff in x:
    print(stuff)