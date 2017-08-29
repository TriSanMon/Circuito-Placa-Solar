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

def ordenar (lista_aparatos)
	sorted(lista_aparatos, key = operator.attrgetter("espera"))

def actualizar (tiempo)
	tiempo = time.time() - inicio

#Introducción de parámetros
periodo_volt_placa = input('Introduce el periodo de estudio del voltaje en la placa: ')

espera_volt_placa = input('¿Cada cuántos segundos quieres que se recojan los datos de voltaje en la placa? ')

periodo_amp_placa = input('Introduce el periodo de estudio de la intensidad proporcionada por la placa: ')

espera_amp_placa  = input('¿Cada cuántos segundos quieres que se recojan los datos de la intensidad proporcionada por la placa? ')

periodo_amp_carga = input('Introduce el periodo de estudio de la potencia consumida por la carga: ')

espera_amp_carga  = input('¿Cada cuántos segundos quieres que se recojan los datos de la potencia consumida por la carga? ')

#Placa
volt_placa = voltimetro ('volt_placa', periodo_volt_placa, espera_volt_placa)
amp_placa = amperimetro ('amp_placa', periodo_amp_placa, espera_amp_placa)

#Fotoresistencia
amp_fotoresist = amperimetro ('amp_fotoresist', periodo_amp_fotoresist, espera_amp_fotoresist)

#Carga
amp_carga = amperimetro ('amp_carga', periodo_amp_carga, espera_amp_carga)

#Toma de datos
lista_aparatos = [volt_placa, amp_placa, amp_carga, amp_fotoresist]
ordenar(lista_aparatos)

inicio = time.time()
i = 0 #tiempo transcurrido
j = 0 
actualizar(i) 

while i < lista_aparatos[3].espera:

	if i < lista_aparatos[0].espera:
		lista_aparatos[0].actualizar_medida(self.medida)
		lista_aparatos[0].medir(lista_aparatos[0].medida)
		time.sleep(lista_aparatos[0].espera)
		j += lista_aparatos[0].espera

	actualizar(i) 

	if i < lista_aparatos[1].espera:
		lista_aparatos[1].actualizar_medida(self.medida)
	    lista_aparatos[1].medir(lista_aparatos[1].medida)
		time.sleep(lista_aparatos[1].espera - j)
		j += lista_aparatos[1].espera

	actualizar(i) 

	if i < lista_aparatos[2].espera:
		lista_aparatos[2].actualizar_medida(self.medida)
	    lista_aparatos[2].medir(lista_aparatos[2].medida)
		time.sleep(lista_aparatos[2].espera - j)
		j += lista_aparatos[2].espera

	actualizar(i) 

	if i < lista_aparatos[3].espera:
		lista_aparatos[3].actualizar_medida(self.medida)
	    lista_aparatos[3].medir(lista_aparatos[3].medida)
		time.sleep(lista_aparatos[3].espera - j)
		j = 0

	actualizar(i) 
