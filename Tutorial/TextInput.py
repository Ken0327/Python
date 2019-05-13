from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class rootwi(BoxLayout):
    textinputtext = StringProperty()

    def __init__(self, **kwargs):
        super(rootwi, self).__init__(**kwargs)
        self.textinputtext = 'palim'

    def print_txt(self):
        print(self.textinputtext)



class rootwiApp(App):
    def build(self):
        return rootwi()

if __name__ == '__main__':
    rootwiApp().run()