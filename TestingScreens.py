# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 16:26:18 2014

@author: ddiggins
"""

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import WipeTransition

class StartScreen(Screen):
    pass

class BackgroundScreen(Screen):
    pass

class BackgroundScreenManager(ScreenManager):
    pass

class TestScreens(App):
    def build(self):
        sm = BackgroundScreenManager()
        sm.add_widget(BackgroundScreen(name = 'background'))
        sm.add_widget(StartScreen(name = 'start'))
        return sm

Orkiv().run()