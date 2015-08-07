from kivy.app import App
from kivy.config import Config
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

from kivy.base import EventLoop


class CanvasWidget(Widget):

    def on_touch_down(self, touch):
    	if Widget.on_touch_down(self, touch):
    		return
        with self.canvas:
            Color(*get_color_from_hex("0080FF80"))
            Line(circle=(touch.x, touch.y, 25), width=4)

    def clear_canvas(self):
    	saved = self.children[:]
    	self.clear_widgets()
    	self.canvas.clear()
    	for widget in saved:
    		self.add_widget(widget)

class PaintApp(App):

    def build(self):
        return CanvasWidget()

if __name__ == "__main__":
	Config.set("graphics", "width", "960")
	Config.set("graphics", "height", "540")  # 16:9
	Config.set("graphics", "resizable", "0")
	Config.set("input", "mouse", "mouse, disabled_multitouch")

	from kivy.core.window import Window
	Window.clearcolor = get_color_from_hex("FFFFFF")

	PaintApp().run()
