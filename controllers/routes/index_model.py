from typing import Union, Any
from atri_react.Flex import Flex
from atri_react.Button import Button
from atri_react.TextBox import TextBox
from atri_react.Image import Image


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.hero_section_white = state["hero_section_white"] if "hero_section_white" in state else None
		self.work_section_white = state["work_section_white"] if "work_section_white" in state else None
		self.hero_section_content = state["hero_section_content"] if "hero_section_content" in state else None
		self.work_section_content = state["work_section_content"] if "work_section_content" in state else None
		self.about_section_content = state["about_section_content"] if "about_section_content" in state else None
		self.about_section_white = state["about_section_white"] if "about_section_white" in state else None
		self.navbar = state["navbar"] if "navbar" in state else None
		self.main = state["main"] if "main" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.Button1 = state["Button1"] if "Button1" in state else None
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.Button2 = state["Button2"] if "Button2" in state else None
		self.Button3 = state["Button3"] if "Button3" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.waveflow_logo = state["waveflow_logo"] if "waveflow_logo" in state else None
		self.Button4 = state["Button4"] if "Button4" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.about_top = state["about_top"] if "about_top" in state else None
		self.about_stats = state["about_stats"] if "about_stats" in state else None
		self.about_top_left = state["about_top_left"] if "about_top_left" in state else None
		self.about_top_right = state["about_top_right"] if "about_top_right" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}
  
	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		if hasattr(self, self.event_alias):
			comp = getattr(self, self.event_alias)
			setattr(comp, callback_name, True)
		self.event_repeating = event["repeating"]
  
	
	@property
	def hero_section_white(self):
		self._getter_access_tracker["hero_section_white"] = {}
		return self._hero_section_white
	@hero_section_white.setter
	def hero_section_white(self, new_state):
		self._setter_access_tracker["hero_section_white"] = {}
		self._hero_section_white = Flex(new_state)

	@property
	def work_section_white(self):
		self._getter_access_tracker["work_section_white"] = {}
		return self._work_section_white
	@work_section_white.setter
	def work_section_white(self, new_state):
		self._setter_access_tracker["work_section_white"] = {}
		self._work_section_white = Flex(new_state)

	@property
	def hero_section_content(self):
		self._getter_access_tracker["hero_section_content"] = {}
		return self._hero_section_content
	@hero_section_content.setter
	def hero_section_content(self, new_state):
		self._setter_access_tracker["hero_section_content"] = {}
		self._hero_section_content = Flex(new_state)

	@property
	def work_section_content(self):
		self._getter_access_tracker["work_section_content"] = {}
		return self._work_section_content
	@work_section_content.setter
	def work_section_content(self, new_state):
		self._setter_access_tracker["work_section_content"] = {}
		self._work_section_content = Flex(new_state)

	@property
	def about_section_content(self):
		self._getter_access_tracker["about_section_content"] = {}
		return self._about_section_content
	@about_section_content.setter
	def about_section_content(self, new_state):
		self._setter_access_tracker["about_section_content"] = {}
		self._about_section_content = Flex(new_state)

	@property
	def about_section_white(self):
		self._getter_access_tracker["about_section_white"] = {}
		return self._about_section_white
	@about_section_white.setter
	def about_section_white(self, new_state):
		self._setter_access_tracker["about_section_white"] = {}
		self._about_section_white = Flex(new_state)

	@property
	def navbar(self):
		self._getter_access_tracker["navbar"] = {}
		return self._navbar
	@navbar.setter
	def navbar(self, new_state):
		self._setter_access_tracker["navbar"] = {}
		self._navbar = Flex(new_state)

	@property
	def main(self):
		self._getter_access_tracker["main"] = {}
		return self._main
	@main.setter
	def main(self, new_state):
		self._setter_access_tracker["main"] = {}
		self._main = Flex(new_state)

	@property
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def Button1(self):
		self._getter_access_tracker["Button1"] = {}
		return self._Button1
	@Button1.setter
	def Button1(self, new_state):
		self._setter_access_tracker["Button1"] = {}
		self._Button1 = Button(new_state)

	@property
	def TextBox1(self):
		self._getter_access_tracker["TextBox1"] = {}
		return self._TextBox1
	@TextBox1.setter
	def TextBox1(self, new_state):
		self._setter_access_tracker["TextBox1"] = {}
		self._TextBox1 = TextBox(new_state)

	@property
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def Button2(self):
		self._getter_access_tracker["Button2"] = {}
		return self._Button2
	@Button2.setter
	def Button2(self, new_state):
		self._setter_access_tracker["Button2"] = {}
		self._Button2 = Button(new_state)

	@property
	def Button3(self):
		self._getter_access_tracker["Button3"] = {}
		return self._Button3
	@Button3.setter
	def Button3(self, new_state):
		self._setter_access_tracker["Button3"] = {}
		self._Button3 = Button(new_state)

	@property
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def waveflow_logo(self):
		self._getter_access_tracker["waveflow_logo"] = {}
		return self._waveflow_logo
	@waveflow_logo.setter
	def waveflow_logo(self, new_state):
		self._setter_access_tracker["waveflow_logo"] = {}
		self._waveflow_logo = Image(new_state)

	@property
	def Button4(self):
		self._getter_access_tracker["Button4"] = {}
		return self._Button4
	@Button4.setter
	def Button4(self, new_state):
		self._setter_access_tracker["Button4"] = {}
		self._Button4 = Button(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def TextBox3(self):
		self._getter_access_tracker["TextBox3"] = {}
		return self._TextBox3
	@TextBox3.setter
	def TextBox3(self, new_state):
		self._setter_access_tracker["TextBox3"] = {}
		self._TextBox3 = TextBox(new_state)

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		self._TextBox6 = TextBox(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def Flex13(self):
		self._getter_access_tracker["Flex13"] = {}
		return self._Flex13
	@Flex13.setter
	def Flex13(self, new_state):
		self._setter_access_tracker["Flex13"] = {}
		self._Flex13 = Flex(new_state)

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		self._TextBox7 = TextBox(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def Flex14(self):
		self._getter_access_tracker["Flex14"] = {}
		return self._Flex14
	@Flex14.setter
	def Flex14(self, new_state):
		self._setter_access_tracker["Flex14"] = {}
		self._Flex14 = Flex(new_state)

	@property
	def about_top(self):
		self._getter_access_tracker["about_top"] = {}
		return self._about_top
	@about_top.setter
	def about_top(self, new_state):
		self._setter_access_tracker["about_top"] = {}
		self._about_top = Flex(new_state)

	@property
	def about_stats(self):
		self._getter_access_tracker["about_stats"] = {}
		return self._about_stats
	@about_stats.setter
	def about_stats(self, new_state):
		self._setter_access_tracker["about_stats"] = {}
		self._about_stats = Flex(new_state)

	@property
	def about_top_left(self):
		self._getter_access_tracker["about_top_left"] = {}
		return self._about_top_left
	@about_top_left.setter
	def about_top_left(self, new_state):
		self._setter_access_tracker["about_top_left"] = {}
		self._about_top_left = Flex(new_state)

	@property
	def about_top_right(self):
		self._getter_access_tracker["about_top_right"] = {}
		return self._about_top_right
	@about_top_right.setter
	def about_top_right(self, new_state):
		self._setter_access_tracker["about_top_right"] = {}
		self._about_top_right = Flex(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def TextBox9(self):
		self._getter_access_tracker["TextBox9"] = {}
		return self._TextBox9
	@TextBox9.setter
	def TextBox9(self, new_state):
		self._setter_access_tracker["TextBox9"] = {}
		self._TextBox9 = TextBox(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

	@property
	def Flex21(self):
		self._getter_access_tracker["Flex21"] = {}
		return self._Flex21
	@Flex21.setter
	def Flex21(self, new_state):
		self._setter_access_tracker["Flex21"] = {}
		self._Flex21 = Flex(new_state)

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		self._TextBox12 = TextBox(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		self._Flex22 = Flex(new_state)

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		self._Flex23 = Flex(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def Flex24(self):
		self._getter_access_tracker["Flex24"] = {}
		return self._Flex24
	@Flex24.setter
	def Flex24(self, new_state):
		self._setter_access_tracker["Flex24"] = {}
		self._Flex24 = Flex(new_state)
  
	def _to_json_fields(self):
		return {
			"hero_section_white": self._hero_section_white,
			"work_section_white": self._work_section_white,
			"hero_section_content": self._hero_section_content,
			"work_section_content": self._work_section_content,
			"about_section_content": self._about_section_content,
			"about_section_white": self._about_section_white,
			"navbar": self._navbar,
			"main": self._main,
			"Flex11": self._Flex11,
			"Button1": self._Button1,
			"TextBox1": self._TextBox1,
			"TextBox2": self._TextBox2,
			"Button2": self._Button2,
			"Button3": self._Button3,
			"Flex10": self._Flex10,
			"waveflow_logo": self._waveflow_logo,
			"Button4": self._Button4,
			"Flex12": self._Flex12,
			"Image2": self._Image2,
			"TextBox3": self._TextBox3,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"TextBox6": self._TextBox6,
			"Image3": self._Image3,
			"Flex13": self._Flex13,
			"TextBox7": self._TextBox7,
			"TextBox8": self._TextBox8,
			"Image4": self._Image4,
			"Flex14": self._Flex14,
			"about_top": self._about_top,
			"about_stats": self._about_stats,
			"about_top_left": self._about_top_left,
			"about_top_right": self._about_top_right,
			"Image5": self._Image5,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"Flex19": self._Flex19,
			"Image6": self._Image6,
			"Flex20": self._Flex20,
			"TextBox11": self._TextBox11,
			"Flex21": self._Flex21,
			"TextBox12": self._TextBox12,
			"Image7": self._Image7,
			"Flex22": self._Flex22,
			"TextBox13": self._TextBox13,
			"TextBox14": self._TextBox14,
			"TextBox15": self._TextBox15,
			"TextBox16": self._TextBox16,
			"Flex23": self._Flex23,
			"TextBox17": self._TextBox17,
			"TextBox18": self._TextBox18,
			"Flex24": self._Flex24
			}
  