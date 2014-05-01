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
        dummydict = {"DoorButton":DoorButton(),"LampButton":LampButton(), 
                     "TableButton":TableButton(), "TableButton2":TableButton2(), "ComputerButton": ComputerButton()}
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

class DoorButton(infoPopUp):
    info = 'Camera has detected motion near exit. \nDoor has been closed for your safety.\n\n'
    info += "It looks like you won't be able to exit. \nAs long as the camera can see you, anyway."
    pass

class RoomEnd(infoPopUp):
    info = 'Congratulations! You beat the level!'

class LampButton(textPopUp):
    text = '#Anything that starts with # is a\n#comment (a note) '
    text += 'and will not be run\n'
    text += '#for example: #I am a Light!\n'
    info = "You're trying to leave? Well, \n"
    info += "I don't know how to help you, but I do \n"
    info += "know that the reason I'm on is because my \n"
    info += "'is_on' status is  'True'. If I were set \n"
    info += "to 'False', I'm sure that I would go out.\n\n"
    info += "To set my is_on status, type: \n"
    info += "self.is_on = True or False!\n"
    info += "and if you just want to turn me off,\n"
    info += "you can also type: self.turn_off()\n"
    info += "I hope that helps!\n\n\n\n"
    is_on = True
    
    def turn_off(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True

class TableButton(textPopUp):
    text = '#I am a Normal Table\n'
    text += "#So I don't use code!\n"
    info = "Hey, NaN!\n"
    info += "I haven't seen you in a while. \n"
    info += "Are you trying to escape the room? \n"
    info += "Typing code at my terminal doesn't work, \n"
    info += 'but I can still help you out.\n'
    info += "To escape, turn off the rooms's lights. \n"
    info += 'All of the lights are in a single list! \n'
    info += "It's called room1.light_list \n"
    info += "I'm sure that will help you."
    pass

class TableButton2(textPopUp):
    info = "Hey, NaN!\n"
    info += "A list is a bunch of things put in \n brackets like these []\n"
    info += "Items in lists are separated by commas!\n\n"
    info += "Here's how to make a For Loop:\n"
    info += "You can use For Loops \n to do boring things many times!\n"
    info += "Start a for loop by typing:\n for value in list:\n"
    info += "Remember to use a colon at the end!\n"
    info += "Then, on the next line, type four spaces\n and write code"
    info += "that you want repeated.\n"
    info += "I hope that helps!"
    text = "#Here's an example for loop!\n"
    text += "#Click 'Try Code' to test it out!\n"
    text += 'for number in range(0, 3):\n'
    text += '   print number' 

class ComputerButton(infoPopUp):
    info = "NaN, you're back! I've missed you so much!\n"
    info += "Hmm, you want to leave?\n\n"
    info += "That's easy, if you turn off all \n"
    info += "the lights, the camera won't be able\n"
    info += "to see you. But there are a lot of lights \n"
    info += "in this room! To turn all the lights off you'd need \n"
    info += "to use something powerful... "
    info += "like a For Loop.\n\n"
    info += "A for loop allows you to do something to \n"
    info += "every object in a list, for example if \n"
    info += "you have a list, list = [L1,L2,L3,L4] and want\n"
    info += "to turn on every light you could write:\n\n"
    info += "for light in list:\n"
    info += "    light.turn_on()\n\n"
    info += "But remember For loops have Four spaces!\n"
    info += "Pretty cool right?\n\n"
    info += "Click on the tables for more help if you need it!\n"
    info += "But, if you ever get stuck in a later room, come\n"
    info += "find me."
    pass

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
    def __init__(self,wall, my_pos):
        self.interface = LampButton()
        self.wall = wall
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
        self.light1 = Light(self.front_wall,(100,450))
        self.light2 = Light(self.front_wall,(500,450))
        
        self.light4 = Light(self.left_wall,(300,450))
        self.light5 = Light(self.left_wall,(500,450))
        self.light6 = Light(self.left_wall,(100, 450))
        
        self.light7 = Light(self.right_wall,(300,450))
        self.light8 = Light(self.right_wall,(200, 450))
        self.light9 = Light(self.right_wall,(400, 450))
        
        self.light11 = Light(self.back_wall,(300,450))
        self.light3 = Light(self.back_wall,(200, 450))
        self.light12 = Light(self.back_wall,(400, 450))
        
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
