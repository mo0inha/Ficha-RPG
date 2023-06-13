#Classe responsavel por pegar os primeiros dados (Nome, Idade)
import sys
import tkinter as tk

class view_Alinhamentos():
    def __init__ (self):

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

        Titulo = tk.Label(self.root, text="Criador e Ficha de \n RPG",
            bg="black", fg="white", font=("Arial", 20)).place(x=260, y=150)

        self.root.mainloop()

view_Alinhamentos()