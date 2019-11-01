from kivy.app import App 
from kivy.uix.widget import Widget 

class HelloWidget(Widget): 
    pass

class MyApp(App):
    def build(self):
        return HelloWidget()

if __name__ == '__main__': 
    MyApp().run() 
