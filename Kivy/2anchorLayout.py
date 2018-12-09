from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.anchorlayout import AnchorLayout

class AnchorApp(App):
  def build(self):
    al = AnchorLayout(anchor_x = 'left', anchor_y = 'top') #left,center,right/top,centr,bottom


    al.add_widget( Button(text='Button', size_hint = [.5, .5]))



    return al

if __name__ == "__main__":
  AnchorApp().run()
