# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Str, Int
from enthought.traits.ui.api import View, Group, Item, Controller

g1 = [Item('department', label="部门"),
      Item('name', label="姓名")]
g2 = [Item('salary', label="工资"),
      Item('bonus', label="奖金")]

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int
    
view1 = View(
    Group(*g1, label = '个人信息', show_border = True),
    Group(*g2, label = '收入', show_border = True),
    title = "外部视图",
)
           
zhang = Employee(name="Zhang")
c = Controller(zhang)
c.edit_traits(view=view1)