from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

class BoxApp(App):
  def build(self):
    bl = BoxLayout(orientation='horizontal', spacing=20, padding=[5, 30, 50, 70]) #vertical

    bl.add_widget( Button(text='Knopka 1'))
    bl.add_widget( Button(text='Knopka 2'))
    bl.add_widget( Button(text='Knopka 3'))

    return bl

if __name__ == "__main__":
  BoxApp().run()
