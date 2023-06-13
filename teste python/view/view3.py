import tkinter as tk
import tkinter.ttk as ttk
from randomizer import Randomizer
from raças import races

class View3(tk.Frame):
    def __init__(self, view_controller):
        tk.Frame.__init__(self, view_controller.master, width=300, height=300)
        
        self.race = tk.StringVar()
        self.subrace = tk.StringVar()
        
        self.label_race = tk.Label(self, text="Raça:")
        self.label_race.pack(pady=10)
        
        self.combobox_race = ttk.Combobox(self, textvariable=self.race, values=races, state="readonly")
        self.combobox_race.bind("<<ComboboxSelected>>", self.update_subrace_options)
        self.combobox_race.pack()
        
        self.label_subrace = tk.Label(self, text="Sub-raça:")
        self.label_subrace.pack(pady=10)
        
        self.combobox_subrace = ttk.Combobox(self, textvariable=self.subrace, state="disabled")
        self.combobox_subrace.pack()
        
        # Cria um botão para gerar dados aleatórios
        self.button_generate_random = tk.Button(self, text="Aleatório", command=self.generate_random_data)
        self.button_generate_random.pack(pady=10)
        
        # Cria um botão para limpar os campos
        self.button_clear = tk.Button(self, text="Limpar", command=self.clear_race_subrace)
        self.button_clear.pack(pady=10)

        # Cria um botão para voltar para a tela anterior
        self.button_back = tk.Button(self, text="Voltar",
                                command=lambda: view_controller.switch_view(view_controller.current_view_index - 1))
        self.button_back.pack(pady=10)

        # Cria um botão para ir para a próxima tela
        self.button_next = tk.Button(self, text="Próxima",
                                command=lambda: view_controller.switch_view(view_controller.current_view_index + 1))
        self.button_next.pack()
        
    def update_subrace_options(self, event):
        # Chama o método do randomizer para obter as opções de sub-raça
        randomizer = Randomizer()
        race = self.race.get()
        
        if race:
            subrace_options = randomizer.get_subrace_options(race)
            self.combobox_subrace['values'] = subrace_options
            
            if subrace_options:
                self.combobox_subrace.configure(state="readonly")
            else:
                self.combobox_subrace.configure(state="disabled")
    
    def generate_random_data(self):
        # Chama o método do randomizer para gerar uma raça e uma sub-raça aleatórias
        randomizer = Randomizer()
        race, subrace = randomizer.generate_random_race()
        
         # Atualiza os campos de texto com os dados gerados
        self.race.set(race)
        self.subrace.set(subrace)
        
    def clear_race_subrace(self):
       # Limpa os campos de texto
       self.race.set("")
       self.subrace.set("")
    