#Classe responsavel por selecionar a (raça)

import sys
import tkinter as tk

class view_Dados1():
    def __init__(self):
        pass

        self.root = tk.Tk()
        self.root.geometry("700x700")


        self.topFrame = tk.Frame(relief=tk.RAISED, borderwidth=1, bg="red")
        self.topFrame.pack(fill=tk.BOTH, expand=True)

        self.bottomFrame = tk.Frame(
            relief=tk.RAISED, borderwidth=1, bg="green")
        self.bottomFrame.pack()

        button = tk.Button(self.bottomFrame, text="<")
        button.grid(row=1, column=0)
        button = tk.Button(self.bottomFrame, text=">")
        button.grid(row=1, column=2)

        #NomePrincipal

        Titulo = tk.Label(self.root, text="Insira seu nome: \n RPG",
            bg="black", fg="white", font=("Arial", 20)).place(x=260, y=150)

        self.root.mainloop()

view_Dados1()