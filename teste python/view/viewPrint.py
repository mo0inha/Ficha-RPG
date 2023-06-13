import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageTk as ImageTk
import os
from model.model_viewprint import ModelViewPrint

class ViewPrint(tk.Frame):
    def __init__(self, view_controller, dados):
        tk.Frame.__init__(self, view_controller.master, width=500, height=500)
        
        # Cria um objeto da classe ModelViewPrint passando o objeto dados
        self.model = ModelViewPrint(dados)
        self.view_controller = view_controller
        
        # Cria um label com o título da tela
        label = tk.Label(self, text="Imprimir Ficha", font=("Helvetica", 20))
        label.pack(pady=20)
        
        # Cria um botão para salvar a ficha como txt
        save_txt_button = tk.Button(self, text="Salvar como TXT", command=self.save_as_txt)
        save_txt_button.pack(pady=10)
        
        # Cria um botão para salvar a ficha como png
        save_png_button = tk.Button(self, text="Salvar como PNG", command=self.save_as_png)
        save_png_button.pack(pady=10)

        # Cria um botão para voltar para a tela anterior
        back_button = tk.Button(self, text="Voltar",
                                command=lambda: view_controller.switch_view(view_controller.current_view_index - 1))
        back_button.pack(pady=10)

        # Cria um botão para voltar ao início
        home_button = tk.Button(self, text="Início",
                                command=lambda: view_controller.switch_view(0))
        home_button.pack()
        
    def save_as_txt(self):
        # Chama o método do model para salvar a ficha como txt
        self.model.save_as_txt()
    
    def save_as_png(self):
        # Chama o método do model para salvar a ficha como png
        data = self.model.get_data_from_views()  # Obtém os dados dos views anteriores

        # Cria uma imagem em branco com o tamanho desejado
        image = Image.new("RGB", (500, 500), (255, 255, 255))

        # Cria um objeto para desenhar na imagem
        draw = ImageDraw.Draw(image)

        # Define uma fonte para escrever na imagem
        font = ImageFont.truetype("arial.ttf", 20)

        # Define as coordenadas iniciais para escrever na imagem
        x = 10
        y = 10

        # Escreve os dados da ficha na imagem
        for key, value in data.items():
            draw.text((x, y), f"{key}: {value}", fill=(0, 0, 0), font=font)
            y += 30  # Incrementa a coordenada y para a próxima linha

        # Cria um arquivo png com o nome da ficha
        file_name = f"{data['Nome']}_{data['Sobrenome']}.png"

        # Salva a imagem como png
        image.save(file_name)

        print(f"Ficha salva como {file_name}")