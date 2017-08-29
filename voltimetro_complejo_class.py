import sublime
import sublime_plugin

class voltimetro:
	def __init__(self, identif, periodo, espera, medida):
		self.identif = identif
		self.periodo = periodo
		self.espera = espera
		self.tabla_volt = []
		self.medida = medida

	def actualizar_medida (medida) #Esta variable iría cambiando de forma externa a este código según lo que lee el aparato de medida del circuito
		self.medida = medida		
		
	def medir(self.medida)
		self.tabla_volt.append(self.medida)
