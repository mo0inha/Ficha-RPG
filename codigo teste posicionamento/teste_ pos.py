import tkinter as tk

root = tk.Tk()

# Criando widgets
button1 = tk.Button(root, text="Botão 1")
button2 = tk.Button(root, text="Botão 2")
image = tk.PhotoImage(file="imagem.png")

# Colocando os widgets na tela
button1.pack()
button2.pack()
label = tk.Label(root, image=image)
label.pack()

# Alterando a ordem de sobreposição
button1.lift()  # Move o botão 1 para cima
label.lower()  # Move a imagem para baixo

root.mainloop()