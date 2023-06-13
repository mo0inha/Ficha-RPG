from tkinter import *
from PIL import Image, ImageDraw
import os
from dados_model import DadosModel

def gerar_png(dados_model):
    nome = dados_model.nome
    idade = dados_model.idade

    # Criação da imagem
    imagem = Image.new("RGB", (200, 200), color="white")
    draw = ImageDraw.Draw(imagem)
    texto = f"Nome: {nome}\nIdade: {idade}"
    draw.text((10, 10), texto, fill="black")

    # Verifica se a pasta de destino existe, caso contrário, cria-a
    pasta_destino = "caminho/para/a/pasta"  # Insira o caminho completo para a pasta desejada
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Salvando a imagem como PNG na pasta de destino
    caminho_arquivo = os.path.join(pasta_destino, f"{nome}_{idade}.png")
    imagem.save(caminho_arquivo)
    print("Imagem gerada e salva com sucesso em:", caminho_arquivo)

dados_model = DadosModel()

# Exemplo de uso
# Após a execução das views 1 e 2, chame a função gerar_png passando o dados_model
gerar_png(dados_model)
