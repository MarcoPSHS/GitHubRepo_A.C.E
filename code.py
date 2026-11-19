from abc import ABC , abstractmethod
from datetime import date, time, datetime
import math
import random
from enum import Enum

authors = ["Alve, Gabriel", "Chavero, Zach", "Evano, Marco"]

print("This is OUR program!")
print("Made by:")
for author in authors:
    print(" - ", author)

class Country:
    def __init__(self, continent, population, size, language, laws: list = []):
        self.continent = continent
        self.population = population
        self.size = size
        self.language = language
        self.laws = laws

    def conquer(self, country_obj):
        pass

        
    def corruption(self):
        pass

    def pass_law(self, new_law):
        self.laws.append(new_law)