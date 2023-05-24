import kivy
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from plyer import vibrator
from kivy.graphics import Color, Rectangle

kivy.require('1.11.1')

class History(BoxLayout):
	def __init__(self, **kwargs):
		super(History, self).__init__(**kwargs)
		self.orientation = "vertical"
		self.scrollview = ScrollView()
		self.scrollview.do_scroll_y = True
		self.scrollview.do_scroll_x = False
		self.add_widget(self.scrollview)
		self.item_layout = BoxLayout(orientation = "vertical", size_hint_y = None, padding = "2dp", spacing = "2dp")
		self.item_layout.bind(minimum_height = self.item_layout.setter("height"))
		self.scrollview.add_widget(self.item_layout)
		
	def add(self, item):
		it = TextInput(disabled = True, size_hint_y = None, text = item, font_size = 75, halign = "right", background_color = (0.3, 0.3, 0.3, 0))
		self.item_layout.add_widget(it)
		
	def removeAll(self):
		self.item_layout.clear_widgets()

class Background(BoxLayout):
	def __init__(self, r = 0, g = 0, b = 0, a = 0, **kwargs):
		super(Background, self).__init__(**kwargs)
		self.r = r
		self.g = g
		self.b = b
		self.a = a
		with self.canvas.before:
			Color(self.r, self.g, self.b, self.a)
			self.rect = Rectangle(pos=self.pos, size=self.size)
		self.bind(pos=self.update_canvas)
		self.bind(size=self.update_canvas)
		
	def update_canvas(self, instance, value):
		self.rect.pos = instance.pos
		self.rect.size = instance.size
		
class BoxLayout_App(App):
	def __init__(self):
		super(BoxLayout_App, self).__init__()
		self.txtbox = TextInput(disabled = True, padding = "5dp", halign = "right", font_size = 75, background_color = (0.3, 0.3, 0.3, 0))
		self.opcount = 0
		self.history = History()
		
	def build(self):
		
		superBox = BoxLayout(orientation ="horizontal")
		
		s1 = BoxLayout(orientation = "vertical", padding = (10, 10, 5, 10), spacing = (10))

		bl1 = BoxLayout(orientation = "horizontal", spacing = (10))
		bl1.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "1", on_release=self.input, font_size = 120))
		bl1.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "2", on_release=self.input, font_size = 120))
		bl1.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "3", on_release=self.input, font_size = 120))
		
		bl2 = BoxLayout(orientation = "horizontal", spacing = (10))
		bl2.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "4", on_release=self.input, font_size = 120))
		bl2.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "5", on_release=self.input, font_size = 120))
		bl2.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "6", on_release=self.input, font_size = 120))
		
		bl3 = BoxLayout(orientation = "horizontal", spacing = (10))
		bl3.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "7", on_release=self.input, font_size = 120))
		bl3.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "8", on_release=self.input, font_size = 120))
		bl3.add_widget(Button(background_color = (1, 1, 1, 0.1), text = "9", on_release=self.input, font_size = 120))

		s1.add_widget(bl1)
		s1.add_widget(bl2)
		s1.add_widget(bl3)
		s1.add_widget(Button(text = "0", background_color = (1, 1, 1, 0.1), on_release=self.input, font_size = 120))
		
		s2 = BoxLayout(orientation = "vertical")
		
		bl4 = BoxLayout(orientation = "vertical", spacing = (10))
		bl4.add_widget(Button(background_color = (0.5, 0.5, 0.5, 0.1), text = "-", on_release=self.input, font_size = 120))
		bl4.add_widget(Button(background_color = (0.5, 0.5, 0.5, 0.1), text = "+", on_release=self.input, font_size = 120))
		bl4.add_widget(Button(background_color = (0.5, 0.5, 0.5, 0.1), text = "×", on_release=self.input, font_size = 120))
		bl4.add_widget(Button(background_color = (0.5, 0.5, 0.5, 0.1), text = "÷", on_release=self.input, font_size = 120))
		
		s2.add_widget(bl4)
		
		s3 = BoxLayout(orientation = "vertical")
		
		bl5 = BoxLayout(orientation = "vertical", spacing = (10))
		bl5.add_widget(Button(background_color = (0.5, 0.5, 0.5, 0.1), text = "del", on_release=self.input, font_size = 120))
		bl5.add_widget(Button(background_color = (1, 1, 1, 0), text = " ", disabled = True))
		bl5.add_widget(Button(background_color = (1, 1, 1, 0), text = " ", disabled = True))
		bl5.add_widget(Button(background_color = (0.5, 0.5, 0.5, 0.1), text = "=", on_release=self.input, font_size = 120))
		
		s3.add_widget(bl5)
		
		opbox = Background(r = 0.2, g = 0.2, b = 0.2, a = 1, orientation = "horizontal", padding = (5, 10, 10, 10), spacing = (10))
		
		opbox.add_widget(s2)
		opbox.add_widget(s3)
		
		superBox.add_widget(s1)
		superBox.add_widget(opbox)
		
		con = Background(r = 0.3, g = 0.3, b = 0.3, a = 1, orientation = "vertical")
		
		to = BoxLayout(orientation = "vertical")
		to.add_widget(self.history)
		to.add_widget(self.txtbox)
		
		
		b1 = Background(r = 0.5, g = 0.8, b = 1, a = 1)
		b1.add_widget(Button(background_color = (0.5, 0.8, 1, 0.1), text = "Clear History", on_release=self.clear, font_size = 50))
		
		t_1 = Background(r = 0.5, g = 0.8, b = 1, a = 0, orientation = "vertical")
		t_1.add_widget(b1)
		t_2 = Background(r = 0.48, g = 0.78, b = 1, a = 0, orientation = "vertical")
		
		t_3 = Background(r = 0.5, g = 0.5, b =0.5, a = 1, orientation = "vertical")
		t_3.add_widget(t_1)
		t_3.add_widget(t_2)
		t_4 = Background(r = 0.5, g = 0.5, b = 0.5, a = 1, orientation = "vertical")
		
		t_5 = Background(r = 0.5, g = 0.5, b = 0.5, a = 1, orientation = "vertical")
		t_5.add_widget(t_3)
		t_5.add_widget(t_4)
		
		blank = Background(r = 0.5, g = 0.8, b = 1, a = 1, orientation = "vertical", padding = (10), spacing = (10, 0))
		blank.add_widget(t_5)
		blank.add_widget(Background(r = 0.5, g = 0.5, b = 0.5, a = 1))
		
		con.add_widget(to)
		con.add_widget(blank)
		con.add_widget(superBox)
		
		return con
		
		
	def clear(self, instance):
		self.history.item_layout.clear_widgets()
		
	def input(self, instance):
		vibrator.vibrate(0.01)
		
		txt = self.txtbox.text
		ins = instance.text
		
		if (ins == "+" or ins == "×" or ins == "÷"):
			if len(txt) == 0:
				return
			if len(txt) == 1 and txt == "-":
				return
				
		
		
		if instance.text == "+":
			if txt[len(txt) - 1:] == "+":
				return
			elif txt[len(txt) - 1:] == "-" or txt[len(txt) - 1:] == "*" or txt[len(txt) - 1:] == "/":
				t = txt[:-1]
				t += instance.text
				self.txtbox.text = t
				return

		if instance.text == "-":
			if txt[len(txt) - 1:] == "-":
				return
			elif txt[len(txt) - 1:] == "+":
				t = txt[:-1]
				t += instance.text
				self.txtbox.text = t
				return
		
		if instance.text == "×":
			if txt[len(txt) - 1:] == "*":
				return
			elif txt[len(txt) - 1:] == "+" or txt[len(txt) - 1:] == "-" or txt[len(txt) - 1:] == "/":
				t = txt[:-1]
				t += "*"
				self.txtbox.text = t
				return
				
		if instance.text == "÷":
			if txt[len(txt) - 1:] == "/":
				return
			elif txt[len(txt) - 1:] == "+" or txt[len(txt) - 1:] == "-" or txt[len(txt) - 1:] == "*":
				t = txt[:-1]
				t += "/"
				self.txtbox.text = t
				return
				
		if instance.text == "del":
			t = self.txtbox.text[:-1]
			self.txtbox.text = t
			return
		
		if ins == "+" or ins == "×" or ins == "÷":
			self.opcount = self.opcount + 1
		if ins == "-" and len(txt) > 0:
			self.opcount = self.opcount + 1
			
		if instance.text == "=":
			if self.opcount < 1:
				return
			res = 0
			
			parsed = txt.replace("÷", "/")
			parsed = parsed.replace("×", "*")
			try:
				res = eval(parsed)
				self.opcount = 0
				self.history.add(txt)
			except:
				return
				
			self.txtbox.text = str(res)
			return
		self.txtbox.text += instance.text
		
root = BoxLayout_App()
root.run()
