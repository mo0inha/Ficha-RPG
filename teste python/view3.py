import tkinter as tk
from tkinter import ttk
import random
from raças import races, subraces

class View3(tk.Frame):
    def __init__(self, view_controller):
        tk.Frame.__init__(self, view_controller.master, width=300, height=300)
        
        self.pack_propagate(0)  # Impede que o frame se ajuste automaticamente ao conteúdo
        
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
        
        self.button_generate_random = tk.Button(self, text="Aleatório", command=self.generate_random_race)
        self.button_generate_random.pack(pady=10)
        
        self.button_clear = tk.Button(self, text="Limpar", command=self.clear_race_subrace)
        self.button_clear.pack(pady=10)
        
        self.update_subrace_options(None)
    
    def get_subrace_options(self, race):
        return subraces.get(race, [])
        
    def update_subrace_options(self, event):
        race = self.race.get()
        
        if race:
            subrace_options = self.get_subrace_options(race)
            self.combobox_subrace['values'] = subrace_options
            
            if subrace_options:
                self.combobox_subrace.configure(state="readonly")
            else:
                self.combobox_subrace.configure(state="disabled")
    
    def generate_random_race(self):
        race = random.choice(races)
        self.race.set(race)
        self.update_subrace_options(None)  # Atualiza as opções da sub-raça
        
        subrace_options = self.get_subrace_options(race)
        
        if subrace_options:
            subrace = random.choice(subrace_options)
            self.subrace.set(subrace)
        else:
            self.subrace.set("")
        
        print(f"Raça: {race}\nSub-raça: {self.subrace.get() or 'N/A'}")
        
    def clear_race_subrace(self):
        self.race.set("")
        self.subrace.set("")
