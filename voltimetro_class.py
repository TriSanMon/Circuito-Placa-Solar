import sublime
import sublime_plugin

class voltimetro:
	def __init__(self, identif, periodo, espera):
		self.identif = identif
		self.periodo = periodo
		self.espera = espera
		self.tabla_volt = []
		
	def medir(volt) #variable introducida por el voltímetro
		self.tabla_volt.append(volt)
