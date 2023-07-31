import tkinter as tk
from controller import ViewMerge

root = tk.Tk()
root.title("Ficha de RPG")

ViewMerge = ViewMerge(root)
ViewMerge.switch_view(0)

root.mainloop()
