from tkinter import *

class View1:
    def __init__(self, dados_model):
        self.dados_model = dados_model

        self.janela = Tk()
        self.janela.title("View1")
        self.janela.geometry("500x500")

        self.rotulo_nome = Label(self.janela, text="Nome:")
        self.rotulo_nome.pack()
        self.entrada_nome = Entry(self.janela)
        self.entrada_nome.pack()

        self.botao_enviar = Button(self.janela, text="Enviar", command=self.enviar_nome)
        self.botao_enviar.pack()

        self.janela.mainloop()

    def enviar_nome(self):
        self.dados_model.nome = self.entrada_nome.get()
        self.janela.destroy()
