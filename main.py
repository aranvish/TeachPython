# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 18:25:41 2014

@author: gabrielle
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.image import  Image 
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from functools import partial 




class ImgBtn(ButtonBehavior, Image):
    def executeText(self, evt=None):
        '''saves user input as a variable to be executed'''
        userInput = self.userInput.text
        exec(userInput)
        
    def popup_display(self, title):
        btnenter = Button(text = 'enter', size_hint_y = None, size_hint_x = 0.5, height =50)
        btnclose = Button(text='Close me', size_hint_y=None, size_hint_x = 0.5, height=50)
        self.userInput = TextInput(size_hint = (1,1))

        layout = BoxLayout(orientation='vertical', height = 300)
#        layout.add_widget(Label(text = message, size_hint = (1, 1)))
        layout.add_widget(self.userInput)
        layout.add_widget(btnenter)
        layout.add_widget(btnclose)
        sv = ScrollView(size_hint=(None, None), size=(300, 300),
                        pos_hint={'center_x':0.5, 'center_y':.5})
        sv.add_widget(layout)
        popup = Popup(content=sv, title=title, size_hint=(None, None), size=(325, 350), auto_dismiss=True)
        btnclose.bind(on_release=popup.dismiss)
        btnenter.bind(on_release=self.executeText)
        popup.open()
        pass

class FrontScreen(Screen):
    pass

class LeftScreen(Screen):
    print("oh hey. front.")
    pass    
    
class RightScreen(Screen):
    pass

class BackScreen(Screen):
    pass    

class BackgroundScreenManager(ScreenManager):#creating a new screen manager so we can have lovely background images!
    bk_img = ObjectProperty(
    Image(source = 'elephant.gif')
    )

class RoomEscapeApp(App):
    def build(self):
        sm = BackgroundScreenManager()
        sm.add_widget(FrontScreen(name = 'front'))
        sm.add_widget(LeftScreen(name = 'left'))
        sm.add_widget(RightScreen(name = 'right'))
        sm.add_widget(BackScreen(name = 'back'))
        return sm
        

        

RoomEscapeApp().run()