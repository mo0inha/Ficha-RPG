from view.view_Home import ViewMenu
from view.view_Name import ViewName
from view.view_Race import ViewRace
from view.view_Class import ViewClass

class ViewMerge:
    def __init__(self, master):
        self.master = master
        
        self.views = []
        self.current_view_index = None
        
        self.add_view(ViewMenu)
        self.add_view(ViewName)
        self.add_view(ViewRace)
        self.add_view(ViewClass)
        
    def add_view(self, view_class, *args):
        view = view_class(self, *args)
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