from dados_model import DadosModel
from view1 import View1
from view2 import View2
from gerador_png import gerar_png

dados_model = DadosModel()

# Abre a View1 para obter o nome
view1 = View1(dados_model)

# Abre a View2 para obter a idade
view2 = View2(dados_model)

# Gera o arquivo PNG com os dados obtidos
gerar_png(dados_model)
