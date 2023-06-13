from view1 import View1
from view2 import View2
from view3 import View3

class ViewController:
    def __init__(self, master):
        self.master = master
        
        self.views = []
        self.current_view_index = None
        
        self.add_view(View1)
        self.add_view(View2)
        self.add_view(View3)
        
    def add_view(self, view_class):
        view = view_class(self)
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
