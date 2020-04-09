from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, StringProperty, BooleanProperty,NumericProperty
from kivy.config import Config 
Config.set('graphics','width',360)
Config.set('graphics','height',720)


class Wm(BoxLayout):
	var ='principal'
	texto = StringProperty("String Property")
	varBol= BooleanProperty(False)
	texVarBol=StringProperty("Falso")
	tamFuen=NumericProperty(15)
	tam=StringProperty("mas")

	def cambiarVar(self):
		if self.texto== "String Property":
			self.texto = "Explicacion String Property,el valor debe ser string"
		else:
			self.texto= 'String Property'

		#print (self.texto)

	def valorBolean(self):
		if self.varBol==False:
			self.varBol = True
			self.texVarBol="Verdadero"
		else:
			self.varBol=False
			self.texVarBol="Falso"

	def numerProAum(self):
		self.tamFuen +=5

	def numerProDis(self):
		self.tamFuen -=5
	
	# def numerPro(self):
		
	# 	if (self.tamFuen <= 80) and (self.tam =="mas"):

	# 		self.tamFuen +=5 
	# 		print(self.tamFuen)
	# 		print(self.tam)
	# 		if self.tamFuen>=80:
	# 			self.tam="mes"
	# 			print(self.tam)

	# 	else:
	# 		self.tamFuen -=5
	# 		print(self.tamFuen)
	# 		if self.tamFuen<=15:
	# 			self.tam="mas"
				



class MyApp(App):
	title="Object Properties"
	def build(self):
		return Wm()


	

if __name__=='__main__':
	MyApp().run()