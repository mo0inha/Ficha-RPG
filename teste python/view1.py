import tkinter as tk

class View1(tk.Frame):
    def __init__(self, view_controller):
        tk.Frame.__init__(self, view_controller.master, width=500, height=500)
        
        self.pack_propagate(0)  # Impede que o frame se ajuste automaticamente ao conteúdo
        
        label = tk.Label(self, text="Criador de Ficha de RPG", font=("Helvetica", 20))
        label.pack(pady=20)
        
        next_button = tk.Button(self, text="Próxima",
                                command=lambda: view_controller.switch_view(view_controller.current_view_index + 1))
        next_button.pack()
        
        credits_button = tk.Button(self, text="Créditos", command=self.show_credits)
        credits_button.pack(pady=10)
        
        other_sheets_button = tk.Button(self, text="Outras Fichas", command=self.show_other_sheets)
        other_sheets_button.pack()
        
    def show_credits(self):
        print("Créditos")  # Implemente aqui a lógica para exibir os créditos
    
    def show_other_sheets(self):
        print("Outras Fichas")  # Implemente aqui a lógica para exibir outras fichas
