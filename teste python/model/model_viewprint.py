class ModelViewPrint:
    def __init__(self, dados):
        self.dados = dados

    def save_as_txt(self):
        self.dados.salvar_dados()

    def get_data_from_views(self):
        data = {
            "Nome": self.dados.nome.get(),
            "Sobrenome": self.dados.sobrenome.get(),
            "Idade": self.dados.idade.get(),
            "Sexo": self.dados.sexo.get(),
            "Preferência de Relacionamento": self.dados.preferencia_relacionamento.get(),
            "Raça": self.dados.raca.get(),
            "Subraça": self.dados.subraca.get()
        }
        return data

    def save_as_png(self):
        data = self.get_data_from_views()  # Obtém os dados dos views anteriores