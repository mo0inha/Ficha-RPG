import tkinter as tk
import tkinter.ttk as ttk
from randomizer import Randomizer

class View2(tk.Frame):
    def __init__(self, view_controller):
        tk.Frame.__init__(self, view_controller.master, width=500, height=500)
        
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.age = tk.StringVar()
        self.gender = tk.StringVar()
        self.relationship_preference = tk.StringVar()
        
        # Resto do código...

        
        self.label_first_name = tk.Label(self, text="Nome:")
        self.label_first_name.pack(pady=10)
        
        self.entry_first_name = tk.Entry(self, textvariable=self.first_name)
        self.entry_first_name.pack(pady=5)
        
        self.label_last_name = tk.Label(self, text="Sobrenome:")
        self.label_last_name.pack(pady=10)
        
        self.entry_last_name = tk.Entry(self, textvariable=self.last_name)
        self.entry_last_name.pack(pady=5)
        
        self.label_age = tk.Label(self, text="Idade:")
        self.label_age.pack(pady=10)
        
        self.entry_age = tk.Entry(self, textvariable=self.age)
        self.entry_age.pack(pady=5)
        
        self.label_gender = tk.Label(self, text="Sexo:")
        self.label_gender.pack(pady=10)
        
        self.entry_gender = tk.Entry(self, textvariable=self.gender)
        self.entry_gender.pack(pady=5)
        
        self.label_relationship_preference = tk.Label(self, text="Preferência de relacionamento:")
        self.label_relationship_preference.pack(pady=10)
        
        self.entry_relationship_preference = tk.Entry(self, textvariable=self.relationship_preference)
        self.entry_relationship_preference.pack(pady=5)
        
         # Cria um botão para limpar todos os campos
        self.button_clear = tk.Button(self, text="Limpar Campos", command=self.clear_fields)
        self.button_clear.pack(pady=10)

         # Cria um botão para gerar dados aleatórios
        self.button_generate = tk.Button(self, text="Gerar Aleatoriamente", command=self.generate_random_data)
        self.button_generate.pack(pady=10)

         # Cria um botão para ir para a próxima tela
        self.button_next = tk.Button(self, text="Próxima", command=lambda: view_controller.switch_view(view_controller.current_view_index + 1))
        self.button_next.pack(side=tk.RIGHT)

         # Cria um botão para voltar para a tela anterior
        self.button_prev = tk.Button(self, text="Anterior", command=lambda: view_controller.switch_view(view_controller.current_view_index - 1))
        self.button_prev.pack(side=tk.RIGHT, padx=10)

    def generate_random_data(self):
         # Chama o método do randomizer para gerar os dados aleatórios
         randomizer = Randomizer()
         name = randomizer.generate_random_name()
         last_name = randomizer.generate_random_last_name()
         age = randomizer.generate_random_age()
         gender = randomizer.generate_random_gender()
         relationship_preference = randomizer.generate_random_relationship_preference()
        
         # Atualiza os campos de texto com os dados gerados
         self.first_name.set(name)
         self.last_name.set(last_name)
         self.age.set(age)
         self.gender.set(gender)
         self.relationship_preference.set(relationship_preference)

    def clear_fields(self):
       # Limpa os campos de texto
       self.first_name.set("")
       self.last_name.set("")
       self.age.set("")
       self.gender.set("")
       self.relationship_preference.set("")
       