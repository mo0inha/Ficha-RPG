class Dados:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = ""
        self.gender = ""
        self.relationship_preference = ""
        self.race = ""
        self.subrace = ""

    def set_first_name(self, name):
        self.first_name = name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_relationship_preference(self, relationship_preference):
        self.relationship_preference = relationship_preference

    def set_race(self, race):
        self.race = race

    def set_subrace(self, subrace):
        self.subrace = subrace

    def salvar_dados(self):
        with open("dados.txt", "w") as file:
            file.write(f"First Name: {self.first_name}\n")
            file.write(f"Last Name: {self.last_name}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"Gender: {self.gender}\n")
            file.write(f"Relationship Preference: {self.relationship_preference}\n")
            file.write(f"Race: {self.race}\n")
            file.write(f"Subrace: {self.subrace}\n")

        print("Dados salvos com sucesso.")
