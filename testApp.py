import sys
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from functools import partial 

class TestApp(App):
    '''A test app designed to create a pop up with text instructions and to 
    allow for the input of text which will hopefully be bound so it can be executed'''      
    def build(self):
        return Button(on_press=partial(self.popup_display, "Type your code here:"))
        
    def executeText(self, evt=None):
        '''saves user input as a variable to be executed'''
        userInput = self.userInput.text
        try:
            exec(userInput)
        except:
            e = str(sys.exc_info()[0])
            self.showError(e)
           
            
    def showError(self, whatsWrong):
        name = 'Oops, looks like there was an error'
        layout = BoxLayout(orientation = 'vertical', height = 200)
        text = Label(text = whatsWrong)
        layout.add_widget(text)
        error = Popup(content = layout, title = name, size_hint =(None, None), size = (300, 100), auto_dismiss= True)
        error.open()
        
    def popup_display(self, title,  widget):
        btnenter = Button(text = 'try code', size_hint_y = None, size_hint_x = 0.5, height =50)
        btnclose = Button(text='Close', size_hint_y=None, size_hint_x = 0.5, height=50)
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
        
       

if __name__ == '__main__':
    TestApp().run()


#from kivy.app import App
#from kivy.uix.scrollview import ScrollView
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label
#
#class SMApp(App):
#
#    def build(self):
#        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
#        #Make sure the height is such that there is something to scroll.
#        layout.bind(minimum_height=layout.setter('height'))
#        for i in range(30):
#            btn = Label(text=str(i), size_hint_y=None, height=40)
#            layout.add_widget(btn)
#        root = ScrollView(size_hint=(None, None), size=(400, 400),
#            pos_hint={'center_x':.5, 'center_y':.5})
#        root.add_widget(layout)
#        return root
#
#if __name__ == '__main__':
#    SMApp().run()

#    
#class chatApp(App):
#    def build(self):
#        return LoginScreen()

#
#if __name__ == '__main__':
#    chatApp().run()