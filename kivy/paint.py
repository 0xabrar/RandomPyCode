from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Rectangle, Triangle


class PaintWidget(Widget):

    shaped_Rectangle = 1


    # shuffle between: circle, triangle, rectangle
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            if PaintWidget.shaped_Rectangle == 1:
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                PaintWidget.shaped_Rectangle = 2
            elif PaintWidget.shaped_Rectangle == 2:
                coords = [touch.x - d / 2, touch.y - d / 2, touch.x,
                        touch.y + d / 2, touch.x + d / 2, touch.y - d / 2]
                Triangle(points=coords)
                PaintWidget.shaped_Rectangle = 3
            else:
                Rectangle(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                PaintWidget.shaped_Rectangle = 1

            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PaintApp(App):

    def build(self):
        parent = Widget()
        self.painter = PaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    PaintApp().run()
