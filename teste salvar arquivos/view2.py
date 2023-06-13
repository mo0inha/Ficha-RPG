class Classe2:
    def __init__(self):
        self.race = ""
        self.subrace = ""
from tkinter import *

class View2:
    def __init__(self, dados_model):
        self.dados_model = dados_model

        self.janela = Tk()
        self.janela.title("View2")
        self.janela.geometry("500x500")

        self.rotulo_idade = Label(self.janela, text="Idade:")
        self.rotulo_idade.pack()
        self.entrada_idade = Entry(self.janela)
        self.entrada_idade.pack()

        self.botao_enviar = Button(self.janela, text="Enviar", command=self.enviar_idade)
        self.botao_enviar.pack()

        self.janela.mainloop()

    def enviar_idade(self):
        self.dados_model.idade = self.entrada_idade.get()
        self.janela.destroy()
