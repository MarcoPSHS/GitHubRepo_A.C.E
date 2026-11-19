# code.py
# This code file is for practicing how to use git, so there is no
# specific code to be implemented that is required by CS3.

# from future __import__ braces  <-- This was never an option.
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

    # ========== Getter Methods ==========
    # Attributes are already public, but these getter methods 
    # are in case if their access level would be changed later on. 
    # This is also for being able to make setter methods.

    @property
    def continent(self):
        return self.continent
    
    @property
    def population(self):
        return self.population
    
    @property
    def size(self):
        return self.size
    
    @property
    def language(self):
        return self.language
    
    @property
    def laws(self):
        return self.laws
    # ====================================
    
    # ========== Setter/Validator-ish Methods ==========
    # Validator rules to be added/changed...
    @continent.setter
    def continent(self, updated_continent):
        pass
    
    @population.setter
    def population(self, updated_population):

        # Note for updates:
        # Consider the fact that there could be 8 billion people in 1
        # country but the country's size is just 1 km^2.
        
        if not isinstance(updated_population, int):
            print("Error: Updated population needs to be a number.")
            return
        if updated_population < 0:
            print ("Error: Updated population cannot be negative.")
            return

        self.population = updated_population

    @size.setter
    def size(self, updated_size):
        pass

    @language.setter
    def language(self, updated_language):
        pass
    
    # do not know if a laws list setter is needed

    # ==================================================
    
    def conquer(self, country_obj):
        pass

        
    def corruption(self):
        pass

    def pass_law(self, new_law):

        self.laws.append(new_law)