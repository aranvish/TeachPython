# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 19:35:39 2014

@author: koenigin
"""

import sys
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App
from functools import partial 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class textPopUp(Popup):
    '''creates a popup object takes in text input and will execute it as a string and display
    any errors that occur'''
    
    def showError(self, whatsWrong):
        '''creates a popup which displays any errors that occur'''
        name = 'Oops, looks like there was an error'
        layout = BoxLayout(orientation = 'vertical', height = 200)
        text = Label(text = whatsWrong)
        layout.add_widget(text)
        error = Popup(content = layout, title = name, size_hint =(None, None), size = (300, 100), auto_dismiss= True)
        error.open()    
        
    def textBind(self, userInput):
        self.userInput = str(userInput)
        try:
            exec(self.userInput)
        except:
            e = str(sys.exc_info()[0])
            self.showError(e)
            

            
class errorDisplay(Popup):
    '''creates a popup object that takes in an error and displays it to the user'''
    def labelError(self, e):
        return e
           
class textApp(App):
    def build(self):
        pop = textPopUp()
        return Button(on_press=pop.open)
        
textApp().run()
            


            
