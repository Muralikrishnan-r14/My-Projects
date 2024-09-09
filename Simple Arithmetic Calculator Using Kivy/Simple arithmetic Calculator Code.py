from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorLayout(GridLayout):

    def __init__(self, **kwargs):
        super(CalculatorLayout, self).__init__(**kwargs)
        self.cols = 4

        # Define placeholders for the first row
        for _ in range(4):
            self.add_widget(Label(text=''))

        # Keep a reference to the label here
        self.display_label = Label(text='0', size_hint_y=None, height=100, font_size=30)
        self.add_widget(self.display_label)

        # Extend the grid to include the display label
        for _ in range(3):
            self.add_widget(Label(text=''))

        buttons = [
            'C', '0', '=', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+'
        ]
        for button in buttons:
            self.add_widget(Button(text=button, on_press=self.on_button_press))

    def on_button_press(self, instance):
        if instance.text == 'C':
            self.display_label.text = '0'
        elif instance.text == '=':
            try:
                self.display_label.text = str(eval(self.display_label.text))
            except Exception:
                self.display_label.text = 'Error'
        else:
            if self.display_label.text == '0':
                self.display_label.text = ''
            self.display_label.text += instance.text


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()
