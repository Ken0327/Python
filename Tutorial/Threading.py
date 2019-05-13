import threading
import time   
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class Thread(BoxLayout):
    counter = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Thread, self).__init__(**kwargs)
        threading.Thread(target = self.while_thread).start()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def Counter_function(self):
        self.counter += 1
        self.ids.lbl.text = "{}".format(self.counter)

    def start_thread(self):
        threading.Thread(target = self.while_thread).start()
        #self.counter += 1
        self.ids.lbl.text = "{}".format(self.counter)

    def while_thread(self):
        while True:
            self.counter += 1
            self.ids.lbl.text = "{}".format(self.counter)
            time.sleep(1)

class MyApp(App):
    def build(self):
        self.load_kv('thread.kv')
        return Thread() 

if __name__ == "__main__":
    app = MyApp()
    app.run()