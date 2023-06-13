from view_Menu import *
from view_Dados1 import *
from view_Raça import *
from view_Classes import *
from view_Antecedentes import *
from view_Alinhamentos import *
from view_Atributos import *

from controller import Controller


controller = Controller()

view_menu = view_Menu(controller)
view_Dados1 = view_Dados1(controller)
view_Raça = view_Raça(controller)
view_Classes = view_Classes(controller)
view_Antecedentes = view_Antecedentes(controller)
view_Alinhamentos = view_Alinhamentos(controller)
view_Atributos = view_Atributos(controller)

controller.set(view_menu)


view_menu.run()  