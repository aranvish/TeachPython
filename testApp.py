#from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.popup import PopUp

#
#class LoginScreen(GridLayout):
#
#    def __init__(self, **kwargs):
#        super(LoginScreen, self).__init__(**kwargs)
#        self.cols = 2
#        self.add_widget(Label(text='User Name'))
#        self.username = TextInput(multiline=False)
#        self.add_widget(self.username)
#        self.add_widget(Label(text='password'))
#        self.password = TextInput(password=True, multiline=False)
#        self.add_widget(self.password)
#        


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
        message = 'Have you ever wanted to do the same thing more than once?  \n\n'
        message2 = 'Like a lot of times? \n\n'
        message3 = 'Did you know if you use a for loop, you can do the same thing as many times as you want without re-typing the same code? \n\n'
        message4 = 'Pretty cool, huh\n\n\n'
        return Button(on_press=partial(self.popup_display, "Did you know...?", message+message2+message3+message4))
        
    def executeText(self, evt=None):
        '''saves user input as a variable to be executed'''
        userInput = self.userInput.text
        exec(userInput)
        
    def popup_display(self, title, message,  widget):
        btnenter = Button(text = 'enter', size_hint_y = None, height =50)
        btnclose = Button(text='Close me', size_hint_y=None, height=50)
        self.userInput = TextInput(size_hint = (1,1))

        layout = BoxLayout(orientation='horizontal', height = 300)
        layout.add_widget(Label(text = message, size_hint = (1, 1)))
        layout.add_widget(self.userInput)
        layout.add_widget(btnclose)
        layout.add_widget(btnenter)
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