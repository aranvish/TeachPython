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

import pdb
import sys


class ImgBtn(ButtonBehavior, Image):
   
    def dispPop(self, which_widget):
#        d = DoorButton()
        dummydict = {"DoorButton":DoorButton(),"LampButton":LampButton(), "TableButton":TableButton()}
        name =dummydict[which_widget]
        name.open()
#        l = getattr(sys.modules[__name__],which_widget)
#        pdb.set_trace()
#        name.open()
#        l.open()
#        getattr(open, which_widget)
#        name = which_widget()
#        name.open()

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

class DoorButton(textPopUp):
    text='#I am a doorl'
    info = 'Camera has detected motion near exit. \n Door has been closed for your safety.'
    pass

class LampButton(textPopUp):
    text = '#I am a lamp'
    line1 = "You want to know about me? \n" 
    line2 = "Why should I tell you any-\n\n"
    line3 = "Wait, is that really you NaN?\n\n"
    line4 = "You're trying to leave? Well, \n"
    line5 = "I don't know how to help you, but I do \n"
    line6 = "know that the reason I'm on is because my \n"
    line7 = "light value is equal to 1, if I were set \n"
    line8 = "equal to 0, I'm sure that I would turn off.\n\n"
    line9 = "I hope that helps!"
    info = line1+line2+line3+line4+line5+line6+line7+line8+line9
    pass

class TableButton(textPopUp):
    text = '#I am a Table\n'
    line1 = "Here's a secret:\n"
    line2 = 'If you want, I can be blue!\n\n'
    line3 = "Try typing: 'object.makeblue()\n"
    line4 = "into your command line!\n\n"
    line5 = "If you want to turn all of us blue,\n"
    line6 = "try typing:\n"
    line7 = "'for object in object_list:\n"
    line8 = "    object.makeblue()'\n"    
    info = line1 + line2 + line3 + line4 + line5 + line6 + line7 +line8
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