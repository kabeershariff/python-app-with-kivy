from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineIconListItem

class MainScreen(Screen):
    search_box = ObjectProperty()
    chat_list = ObjectProperty()
	
    def search(self):
        query = self.search_box.text
        list_item = OneLineIconListItem(text=query )
        self.ids.chat_list.add_widget(list_item)

class ChatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Orange"
        return MainScreen()


ChatApp().run()
