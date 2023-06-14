import tkinter as tk
import os

class ModelViewMenu:
    def __init__(self):
        pass
    
    def show_credits(self):
        # Implementa a lógica para exibir os créditos
        window = tk.Toplevel()
        window.title("Créditos")
        window.geometry("200x200")
        
        label = tk.Label(window, text="Desenvolvido por: Mo0inha")
        label.pack()
        
