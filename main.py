from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.textfield import MDTextField

class MainScreen(Screen):
    search_box = ObjectProperty()
    chat_list = ObjectProperty()
	
    def search(self):
        query = self.search_box.text
        user_list_item = MDTextField(text=query, readonly=True, focus=False, mode="rectangle", icon_left="account-circle", multiline=True )
        ai_list_item = MDTextField(text=query, readonly=True, focus=False, mode="rectangle", icon_right="robot-happy" , multiline=True )
        
        self.ids.chat_list.add_widget(user_list_item)
        self.ids.chat_list.add_widget(ai_list_item)

class ChatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Orange"
        return MainScreen()


ChatApp().run()
