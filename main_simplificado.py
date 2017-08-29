# -*- coding: cp-1252 -*-

#Programa para tratamiento de datos de circuito de placa solar fotovoltáica

import sublime
import sublime_plugin
import time
import operador

#Definición de parámetros para el amperímetro de la fotoresistencia con la que se pretende conocer las horas de mayor luminosidad
periodo_amp_fotoresist = 86400
espera_amp_fotoresist = 60 #Intervalo entre lecturas de datos
#volt_carga = *Introducir voltaje al que trabaja la carga y dejar de comentar* 

#Estas son las variables proporcionadas por los aparatos de medida y que se actualizan de forma externa a este programa
#voltios_placa
#amperios_placa
#amperios_fotoresist
#amperios_carga

def actualizar (tiempo)
	tiempo = time.time() - inicio

#Introducción de parámetros
periodo = input('Introduce el periodo de estudio de las magnitudas: ')

espera = input('¿Cada cuántos segundos quieres que se recojan los datos? ')

#Placa
volt_placa = voltimetro ('volt_placa', periodo, espera)
amp_placa = amperimetro ('amp_placa', periodo, espera)

#Fotoresistencia
amp_fotoresist = amperimetro ('amp_fotoresist', periodo, espera)

#Carga
amp_carga = amperimetro ('amp_carga', periodo, espera)

#Toma de datos

inicio = time.time()
i = 0 #tiempo transcurrido

while i < periodo

	for j in lista_aparatos

		volt_placa.medir(voltios_placa)
		amp_placa.medir(amperios_placa)
		amp_fotoresist.medir(amperios_fotoresist)
		amp_carga.medir(amperios_carga * volt_carga) # Se obtiene la potencia directamente

		time.sleep(espera)

		actualizar(i) 

