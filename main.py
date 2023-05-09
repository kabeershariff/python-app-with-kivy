from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.clock import mainthread
import openai
import my_key
import threading


openai.api_key = my_key.my_api_key
Window.softinput_mode = 'below_target'


class MainScreen(Screen):
    search_box = ObjectProperty()
    chat_list = ObjectProperty()
    spinner = ObjectProperty()
    icon_button = ObjectProperty()
    
    def search(self):
        global query
        query = self.search_box.text
        print(query)
        self.spinner.active = True
        self.search_box.disabled = True
        self.icon_button.disabled = True
        background_thread = threading.Thread(target = self.fetch).start()
    
    
    def fetch(self):
        global ai_message
        ai_message = Model.result(query)
        print(ai_message)
        self.update()
    
    @mainthread
    def update(self):
        #query = self.search_box.text
        self.search_box.text = ""
        self.spinner.active = False
        self.search_box.disabled = False
        self.icon_button.disabled = False
        user_list_item = MDTextField(text=query, readonly=True, focus=False, mode="rectangle", icon_left="account-circle", multiline=True )
        ai_list_item = MDTextField(text=ai_message, readonly=True, focus=False, mode="rectangle", icon_right="robot-happy" , multiline=True )
        
        self.ids.chat_list.add_widget(user_list_item)
        self.ids.chat_list.add_widget(ai_list_item)

class ChatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Red"
        return MainScreen()
        
class Model():
    def result(question):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.6,
            max_tokens=150,
         )
        return (response.choices[0].text.strip())
        


ChatApp().run()
