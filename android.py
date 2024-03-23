from kivy.app import App
from kivy.uix.codeinput import CodeInput
from kivy.uix.button import Button
from pygments.lexers import HtmlLexer
from kivy.config import Config


def hello():
    print('Hello')


class MyApp(App):
    def build(self):
        # return CodeInput(lexer=HtmlLexer())
        return Button(text='Hello World')


if __name__ == '__main__':
    MyApp().run()
