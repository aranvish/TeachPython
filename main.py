# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 18:25:41 2014

@author: gabrielle
"""
import sys
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
   
    def dispPop(self):
        name = textPopUp()
        name.open()


class textPopUp(Popup):
    '''creates a popup object takes in text input and will execute it as a string and display
    any errors that occur'''   
    def textBind(self, userInput):
        self.userInput = str(userInput)
        try:
            exec(self.userInput)
        except:
            e = str(sys.exc_info()[0])
            self.showError(e)
    def showError(self, whatsWrong):
        '''creates a popup which displays any errors that occur'''
        name = 'Oops, looks like there was an error'
        layout = BoxLayout(orientation = 'vertical', height = 200)
        text = Label(text = whatsWrong)
        layout.add_widget(text)
        error = Popup(content = layout, title = name, size_hint =(None, None), size = (300, 100), auto_dismiss= True)
        error.open()


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