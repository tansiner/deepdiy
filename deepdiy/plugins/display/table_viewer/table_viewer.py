import os,rootpath
rootpath.append(pattern='main.py') # add the directory of main.py to PATH
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty,DictProperty,ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class Cell(TextInput):
    pass

class NoCell(ToggleButton):
    def pressed(self,n):
        print(n)

    def released(self,m):
        print(m)

class TableViewer(BoxLayout):
    """docstring for TableViewer."""

    data=DictProperty()
    bundle_dir = rootpath.detect(pattern='main.py') # Obtain the dir of main.py
    Builder.load_file(bundle_dir +os.sep+'ui'+os.sep+'table_viewer.kv')

    def __init__(self):
        super(TableViewer, self).__init__()
        self.is_selected_=False
        self.bind(data=self.populate)


    def populate(self,*args):
        data =self.data['content']
        if len(data)==0:
            pass
        else:
            self.ids.grid.cols=len(data[0])+1
            self.rows=len(data)
            for i in range(len(data)):
                for j in range(len(data[0])+1):
                    cell=Cell()
                    no=NoCell()
                    if j==0:
                    	no.text=str(i+1)
                    	self.ids.grid.add_widget(no)
                    else:
                    	cell.text=str(data[i][j-1])
                    	self.ids.grid.add_widget(cell)


class Test(App):
    """docstring for Test."""

    data=ObjectProperty()
    plugins=DictProperty()

    def __init__(self):
        super(Test, self).__init__()

    def build(self):
        x=[]
        for i in range(20):
            y=[]
            for j in range(6):
                t='text'+str(j+1)
                y.append(t)
            x.append(y)
            del y

        '''Populate the table'''
        demo=TableViewer()
        demo.data={'content':x}
        return demo

if __name__ == '__main__':
    Test().run()