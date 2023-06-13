import tkinter as tk
from view_controller import ViewController

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.view_controller = ViewController(self)
        
        self.switch_view(0)
        
    def switch_view(self, view_index):
        self.view_controller.switch_view(view_index)


app = App()
app.mainloop()
