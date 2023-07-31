import tkinter as tk
import tkinter.ttk as ttk
from randomizer import Randomizer
from Dict.classes import *


class ViewClass(tk.Frame):
    def __init__(self, view_controller):
        tk.Frame.__init__(self, view_controller.master, width=500, height=500)
        self.pack_propagate(0)

        self.class_name = tk.StringVar()
        self.subclass = tk.StringVar()

        self.label_class = tk.Label(self, text="Classe:")
        self.label_class.pack(pady=10)

        self.combobox_class = ttk.Combobox(self, textvariable=self.class_name, values=classe, state="readonly")
        self.combobox_class.bind("<<ComboboxSelected>>", self.update_subclass_options)
        self.combobox_class.pack()

        self.label_subclass = tk.Label(self, text="Subclasse:")
        self.label_subclass.pack(pady=10)

        self.combobox_subclass = ttk.Combobox(self, textvariable=self.subclass, state="disabled")
        self.combobox_subclass.pack()

        self.button_generate_random = tk.Button(self, text="Aleatório", command=self.generate_random_data)
        self.button_generate_random.pack(pady=10)

        self.button_clear = tk.Button(self, text="Limpar", command=self.clear_class_subclass)
        self.button_clear.pack(pady=10)

        self.button_next = tk.Button(self, text="Próxima", command=lambda: view_controller.switch_view(view_controller.current_view_index + 1))
        self.button_next.pack(side=tk.RIGHT)

        self.button_prev = tk.Button(self, text="Anterior", command=lambda: view_controller.switch_view(view_controller.current_view_index - 1))
        self.button_prev.pack(side=tk.RIGHT, padx=10)

    def update_subclass_options(self):
        randomizer = Randomizer()
        class_name = self.class_name.get()

        if class_name:
            subclass_options = randomizer.get_subclass_options(class_name)
            self.combobox_subclass['values'] = subclass_options

            if subclass_options:
                self.combobox_subclass.configure(state="readonly")
            else:
                self.combobox_subclass.configure(state="disabled")

    def generate_random_data(self):
        randomizer = Randomizer()
        class_name, subclass = randomizer.generate_random_class()

        self.class_name.set(class_name)
        self.subclass.set(subclass)

    def clear_class_subclass(self):
        self.class_name.set("")
        self.subclass.set("")