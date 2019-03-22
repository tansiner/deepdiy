import os
from kivy.uix.treeview import TreeView,TreeViewLabel
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.properties import DictProperty
from kivy.core.window import Window


class ResourceTree(TreeView):
    data = DictProperty()
    def __init__(self, **kwargs):
        super(ResourceTree, self).__init__(**kwargs)
        self.bind(data=self.update_tree_view)
        self.size_hint = 1, None
        self.bind(minimum_height = self.setter('height'))


    def update_ids(self,*arg):
        if self.data['file_list']==[]:
            return
        resource_ids={}
        for file_path in self.data['file_list']:
            resource_ids.update({file_path.split(os.sep)[-1]:[]})
        # for dict in self.resource_data:
        #     if dict ==None:
        #         return
        #     for key in dict:
        #         resource_ids[key].append(dict[key])
        self.resource_ids={'All data':[resource_ids]}

    def populate_tree_view(self, parent, node):
        for key in list(node.keys()):
            tree_node = self.add_node(TreeViewLabel(text=key,is_open=True), parent)
        for child_node in node[key]:
            self.populate_tree_view(tree_node, child_node)

    def depopulate(self,*arg):
        for node in self.iterate_all_nodes():
            self.remove_node(node)

    def update_tree_view(self,*arg):
        if not hasattr(self.data, 'file_list'):
            return
        print(self.data)
        self.update_ids()
        self.depopulate()
        self.populate_tree_view(None, self.resource_ids)


class TestApp(App):
    def __init__(self):
        super(TestApp, self).__init__()

        self.resource_tree=ResourceTree()
        self.resource_tree.resource_ids={'1': [
                    {'1.1': [
                        {'1.1.1': [
                            {'1.1.1.1': []}]},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.2': []},
                        {'1.1.3': []}]},
                      {'1.2': []}]}

    def build(self):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button
        root=BoxLayout()
        window=ScrollView(scroll_type=["bars"],  bar_width=20)
        root.add_widget(window)
        window.add_widget(self.resource_tree)
        root.add_widget(Button(text='Clear',on_press=self.resource_tree.depopulate))
        root.add_widget(Button(text='Update',on_press=self.resource_tree.update_tree_view))
        return root


if __name__ == '__main__':
    TestApp().run()
