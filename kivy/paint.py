from kivy import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Eclipse, Line


class PaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            Eclipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

    def on_touch_move(self, touch):
    	touch.ud(['line'].points += [touch.x, touch.y]


class PaintApp(Widget):

	def build(self):
		parent = Widget()
		self.painter = MyPaintWidget()
		clear_button = Button(text='clear')
		clear_button.bind(on_release=self.clear_canvas)
		parent.add_widget(self.painter)
		parent.add_widget(clear_button)
		return parent

	def clear_canvas(self, obj):
		self.painter.canvas.clear()

if __name__ == "__main__":
	PaintApp.run()