import random
import names
from Dict.raças import *
from Dict.classes import *


class Randomizer:
    def __init__(self):
        pass
    
    
    def generate_random_name(self):
        return names.get_first_name()
    
    def generate_random_last_name(self):
        return names.get_last_name()
    
    def generate_random_age(self):
        return str(random.randint(18, 60))
    
    def generate_random_gender(self):
        genders = ["Masculino", "Feminino", "Não binário"]
        return random.choice(genders)
    
    def generate_random_relationship_preference(self):
        preferences = ["Heterossexual", "Homossexual", "Bissexual", "Pansexual"]
        return random.choice(preferences)



    def get_subrace_options(self, race):
        return subraces.get(race, [])
    def generate_random_race(self):
        race = random.choice(races)
        subrace_options = self.get_subrace_options(race)
        
        if subrace_options:
            subrace = random.choice(subrace_options)
        else:
            subrace = ""
        
        return race, subrace
    
    
    
    def get_subclass_options(self, classes):
        return subClass.get(classes, [])
    def generate_random_class(self):
        classe = random.choice(classe)
        subclass_options = self.get_subclass_options(classe)
        
        if subclass_options:
            subclasses = random.choice(subclass_options)
        else:
            subclasses = ""
        
        return classe, subclasses