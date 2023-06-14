import random
import names
from raças import races, subraces

class Randomizer:
    def __init__(self):
        pass
    
    # Lógica para o view 2
    def generate_random_name(self):
        return names.get_first_name() # Usa a biblioteca names para gerar um nome aleatório
    
    def generate_random_last_name(self):
        return names.get_last_name() # Usa a biblioteca names para gerar um sobrenome aleatório
    
    def generate_random_age(self):
        return str(random.randint(18, 60)) # Gera uma idade aleatória entre 18 e 60 anos
    
    def generate_random_gender(self):
        genders = ["Masculino", "Feminino", "Não binário"]
        return random.choice(genders) # Escolhe um sexo aleatório da lista
    
    def generate_random_relationship_preference(self):
        preferences = ["Heterossexual", "Homossexual", "Bissexual", "Pansexual"]
        return random.choice(preferences) # Escolhe uma preferência de relacionamento aleatória da lista

    # Lógica para o view 3
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