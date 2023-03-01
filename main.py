from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class MainScreen(Screen):
    search_box = ObjectProperty()
	
    def search(self):
        query = self.search_box.text
        print(f"{query}")

class ChatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Orange"
        return MainScreen()

ChatApp().run()
