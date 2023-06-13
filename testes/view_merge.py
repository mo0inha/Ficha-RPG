from view.view1 import View1
from view.view2 import View2
from view.view3 import View3
from view.viewPrint import ViewPrint
from dados import Dados

class ViewMerge:
    def __init__(self, master):
        self.master = master
        
        self.views = []
        self.current_view_index = None
        
        self.dados = Dados()  # Instancia o objeto dados
        
        self.add_view(View1)
        self.add_view(View2)
        self.add_view(View3)
        self.add_view(ViewPrint, self.dados)  # Passa o objeto dados para ViewPrint
        
    def add_view(self, view_class, *args):
        view = view_class(self, *args)  # Passa os argumentos adicionais para a classe de visualização
        self.views.append(view)
        
        if len(self.views) == 1:
            self.switch_view(0)
        
    def switch_view(self, view_index):
        if view_index < 0 or view_index >= len(self.views):
            return
        
        if self.current_view_index is not None:
            self.views[self.current_view_index].pack_forget()
        
        self.current_view_index = view_index
        self.views[self.current_view_index].pack()