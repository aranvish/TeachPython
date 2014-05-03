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
from kivy.uix.tabbedpanel import TabbedPanel

from functools import partial 

import pdb
import sys


class ImgBtn(ButtonBehavior, Image):
   
    def dispPop(self, which_widget):
#        d = DoorButton()
        dummydict = {"DoorButton":DoorButton(),"LampButton":LampButton(), 
                     "TableButton":TableButton(), "TableButton2":TableButton2(), "ComputerPanel":ComputerPanel()}
        name =dummydict[which_widget]
        name.open()


class textPopUp(Popup):
    '''creates a popup object takes in text input and will execute it as a string and display
    any errors that occur'''  
    
    def textBind(self, userInput):
        '''takes the user input from the kivy input terminal and binds it as
        a string. Tries string to catch all errors, if none occur, runs the 
        string. Also checks to see if any light values have been changed'''
        self.userInput = str(userInput)
        try:
            exec(self.userInput)
            old = room1.room_light
            for i in range(len(room1.light_list)):
                room1.light_list[i].check_is_on()
                room1.updatelight()  
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
        
        
class infoPopUp(Popup):
    '''Just has a label which pops up on press'''
    pass

class ComputerPanel(Popup):
    '''Special info popup with tabbed panels for navigating on the computer'''
    pass

class DoorButton(infoPopUp):
    info = 'Camera has detected motion near exit. \nDoor has been closed for your safety.\n\n'
    info += "It looks like you won't be able to exit [b]as long as the camera can see you.[/b]"
    pass

class RoomEnd(infoPopUp):
    info = 'Congratulations! You beat the level!'

class LampButton(textPopUp):
    text = ""
    info = "You want to turn me off? Well, that's not too hard! \n\n"
    info += "To set my is_on status, type: \n\n"
    info += "self.is_on = True or self.is_on = False!\n\n"
    info += "When you type self, you choose me\n"
    info += "instead of some other light and when you\n"
    info += "type .is_on it means you want to know\n"
    info += "my is_on state instead of someone else's!\n\n"
    info += "OH! And if you just want to turn me off,\n"
    info += "you can also type:\n\nself.turn_off()\n\n"
    info += "I hope that helps!\n\n"
    is_on = True
    
    def turn_off(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        
    def changetext(self, text):
        self.text = text

class TableButton(infoPopUp):
    info = "Hey, NaN! I haven't seen you in a while.\n\n"
    info += "Are you trying to escape the room? \n"
    info += "I can't write any code myself, \n"
    info += 'but I can still help you out.\n'
    info += "To escape, [b]turn off the rooms's lights.[/b] \n"
    pass

class TableButton2(infoPopUp):
    info = "Hey, NaN!\nI am but a lowly table, I can't do much But I know\nthe name of the list all of the lights are in!\n\nIt's [b]room1.light_list[/b]\n\nI hope that helps!"

class StartScreen(Screen):
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
    bk_img = ObjectProperty()

class Light:
    def __init__(self,wall, my_pos, list_index):
        self.interface = LampButton()
        self.wall = wall
        self.interface.changetext('N0')
        self.my_pos = my_pos
        self.is_on = self.interface.is_on
        self.widg = ImgBtn(source = 'Assets_HangingLamp_on.png', size_hint = (.25,.25), pos = self.my_pos, on_press = self.interface.open)
        wall.add_widget(self.widg)

        
    def check_is_on(self):
        '''changes the light image depending on whether the light is on or 
        off'''
        if self.interface.is_on == False:
            self.wall.remove_widget(self.widg)
            self.widg = ImgBtn(source = 'Assets_HangingLamp_off.png', size_hint = (.25,.25), pos = self.my_pos, on_press = self.interface.open)
            self.wall.add_widget(self.widg)
        else:
            self.wall.remove_widget(self.widg)
            self.widg = ImgBtn(source = 'Assets_HangingLamp_on.png', size_hint = (.25,.25), pos = self.my_pos, on_press = self.interface.open)
            self.wall.add_widget(self.widg)
        if room1.room_light == 0:
            self.wall.clear_widgets()
            win = Label(text = 'Congratulations! You escaped the Room')
            self.wall.add_widget(win)
            
            
    def turn_off(self):
        self.interface.is_on = False
        
    def turn_on(self):
        self.interface.is_on = True
        
        
class Door:
    def __init__(self,wall):
        self.interface = DoorButton()
        self.win = RoomEnd()
        self.wall = wall
        self.my_pos = 300, 140
        self.widg = ImgBtn(source = 'Assets_Door2.png', size_hint = (.2,.5), pos = self.my_pos, on_press = self.checklight(room1.room_light).open)
        wall.add_widget(self.widg)
        
    def checklight(self, roomlight):
        '''Tries to change the popup depending on the amount of light in the 
        room'''
        print roomlight
        if roomlight == 0:
            return self.win
        return self.interface
        
class RoomEscapeApp(App):

    def build(self):
        self.start_screen = StartScreen(name = 'start')
        self.front_wall = FrontScreen(name = 'front')
        self.left_wall = LeftScreen(name = 'left')
        self.right_wall = RightScreen(name = 'right')
        self.back_wall = BackScreen(name = 'back')
        self.room_light = 11

        
        self.light_list = []
        self.makedoor()
        self.makelights()
        
        sm = BackgroundScreenManager()
        sm.add_widget(self.start_screen)
        sm.add_widget(self.left_wall)
        sm.add_widget(self.front_wall)
        sm.add_widget(self.right_wall)
        sm.add_widget(self.back_wall)
        sm.add_widget(StartScreen(name = 'start'))
        sm.add_widget(LeftScreen(name = 'left'))
        sm.add_widget(FrontScreen(name = 'front'))
        sm.add_widget(RightScreen(name = 'right'))
        sm.add_widget(BackScreen(name = 'back'))
        return sm
   
    def makelights(self):
        '''initializes all lights, adding them to the wall'''
        self.light1 = Light(self.front_wall,(100,450), 1)
        self.light2 = Light(self.front_wall,(500,450), 1)
        
        self.light4 = Light(self.left_wall,(300,450), 3)
        self.light5 = Light(self.left_wall,(500,450), 4)
        self.light6 = Light(self.left_wall,(100, 450), 5)
        
        self.light7 = Light(self.right_wall,(300,450), 6)
        self.light8 = Light(self.right_wall,(200, 450),7)
        self.light9 = Light(self.right_wall,(400, 450), 8)
        
        self.light11 = Light(self.back_wall,(300,450), 9)
        self.light3 = Light(self.back_wall,(200, 450), 10)
        self.light12 = Light(self.back_wall,(400, 450), 11)
        
        self.light_list = [self.light1, self.light2, self.light3, self.light4, self.light5, self.light6, self.light7, self.light8, self.light9, self.light11, self.light12]
        
    def makedoor(self):
        '''creates a door and adds to wall'''
        self.door = Door(self.front_wall)        
        
    def updatelight(self):
        '''updates the amount of light in the room'''
        self.room_light = 11
        for light in self.light_list:
            if light.interface.is_on == False:
                self.room_light -=1
        
room1 = RoomEscapeApp()
room1.build()
#initialize widgets related to conditionals for the door
room1.run()
