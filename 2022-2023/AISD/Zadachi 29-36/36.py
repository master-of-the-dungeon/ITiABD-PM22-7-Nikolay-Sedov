class Country:
    def __init__(self, name, capital, population, area):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return len(key) % self.size

    def add_country(self, country):
        index = self._hash(country.name)
        self.table[index].append(country)

    def get_country(self, name):
        index = self._hash(name)
        for country in self.table[index]:
            if country.name == name:
                return country
        return None



hash_table = HashTable(10)

hash_table.add_country(Country("Russia", "Moscow", 144500000, 17098242))
hash_table.add_country(Country("USA", "Washington D.C.", 328200000, 9833520))
hash_table.add_country(Country("China", "Beijing", 1393000000, 9596961))
hash_table.add_country(Country("India", "New Delhi", 1353000000, 3287240))

print(hash_table.get_country("Russia").capital)
print(hash_table.get_country("USA").population)
print(hash_table.get_country("China").area)
print(hash_table.get_country("Japan"))
