from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivymd.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivymd.uix.boxlayout import BoxLayout


class MyApp(MDApp):
    def build(self):
        self.formula = ''
        bl = BoxLayout(orientation = 'vertical')
        gl = GridLayout(cols = 4)

        self.lbl = MDLabel(text = '0', halign = 'right', font_style = 'H3')

        bl.add_widget(self.lbl)

        button1 = Button(text = '1', on_press = self.add_number)
        button2 = Button(text = '2', on_press = self.add_number)
        button3 = Button(text = '3', on_press = self.add_number)
        button4 = Button(text = '+', on_press = self.add_oper)
        button5 = Button(text = '4', on_press = self.add_number)
        button6 = Button(text = '5', on_press = self.add_number)
        button7 = Button(text = '6', on_press = self.add_number)
        button8 = Button(text = '-', on_press = self.add_oper)
        button9 = Button(text = '7', on_press = self.add_number)
        button10 = Button(text = '8', on_press = self.add_number)
        button11 = Button(text = '9', on_press = self.add_number)
        button12 = Button(text = '*', on_press = self.add_oper)
        button13 = Button(text = 'C', on_press = self.add_clear)
        button14 = Button(text = '0', on_press = self.add_number)
        button15 = Button(text = '=', on_press = self.add_res)
        button16 = Button(text = '/', on_press = self.add_oper)
        gl.add_widget(button1)
        gl.add_widget(button2)
        gl.add_widget(button3)
        gl.add_widget(button4)
        gl.add_widget(button5)
        gl.add_widget(button6)
        gl.add_widget(button7)
        gl.add_widget(button8)
        gl.add_widget(button9)
        gl.add_widget(button10)
        gl.add_widget(button11)
        gl.add_widget(button12)
        gl.add_widget(button13)
        gl.add_widget(button14)
        gl.add_widget(button15)
        gl.add_widget(button16)
        bl.add_widget(gl)
        return bl

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        self.formula +=str(instance.text)
        self.update_label()

    def add_oper(self, instance):
        self.formula +=str(instance.text)
        self.update_label()

    def add_clear(self, instance):
        self.formula = '0'
        self.update_label()
        self.formula = ''

    def add_res(self, instance):
        self.lbl.text = str(eval(self.lbl.text))



if __name__ == '__main__':
    MyApp().run()