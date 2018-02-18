'''
Universidade de Brasilia, UnB
Faculdade de Comunicacao Social, FAC
Departamento de Jornalismo

Produto de Trabalho de Conclusao de Curso, TCC
Título: "JORNALISMO E COMPUTAÇAO: Automacao do lide"

Aluna: Marilia Nestor Santos
Matricula: 11/0132254
Orientadora: Marcia Marques

Brasilia, 07 de fevereiro de 2017

**** Informacoes necessarias:
--- Este programa foi escrito para automatizar um lide de clima e tempo

--- Especificações tecnicas
    Programa escrito em python3.5
    Para rodar, foi utilizado o editor de texto Text Wrangler e o terminal do computador
    O computador e um MacBook Pro mid 2012, que utiliza macOS Sierra 10.12.3
    
-- Variaveis utilizadas com exemplos:
nome_cidade = "Brasilia"
quando = "hoje"
Quando = "Hoje"
temp_min = "14"
temp_max = "28"
umidade_min = "55"
umidade_max = "70"
texto_manha = "Parcialmente nublado"
texto_tarde = "Parcialmente nublado a nublado com possibilidade de chuva em areas isoladas
texto_noite = "Parcialmente nublado a nublado com possibilidade de chuva em areas isoladas
'''

import string
import datetime
import random
import doctest
import requests
import urllib
import urllib.request
import string
from bs4 import BeautifulSoup
from random import randint

def Grupo_1_1_IniciarLide (nome_cidade, quando, Quando):
		aleatorio = (randint(0,4))
		if aleatorio == 0:
				print ("Em "+nome_cidade+" "+quando+" ", end = "")
		elif aleatorio == 1:
				print ("A previsao de "+quando+" para "+nome_cidade+" ", end = "")
		elif aleatorio == 2:
				print (Quando+" em "+nome_cidade+", ", end = "")
		elif aleatorio == 3:
				print (Quando+" "+nome_cidade+" tem expectativa de ", end = "")
		elif aleatorio == 4:
				print (Quando+" "+nome_cidade+" espera ", end = "")

def Grupo_1_2_no_fim_da_frase (nome_cidade, quando, Quando):
		aleatorio = (randint(0,2))
		if aleatorio == 0:
				print ("em "+nome_cidade+" "+quando+". ", end = "")
		elif aleatorio == 1:
				print ("de "+nome_cidade+" "+quando+". ", end = "")
		elif aleatorio == 2:
				print (quando+" em "+nome_cidade +". ", end = "")

def Grupo_2_1_frase_completa (temp_min, temp_max):
		aleatorio = (randint(0,4))
		if aleatorio == 0:
				print ("Temperatura minima prevista de "+temp_min+"°C e maxima de "+temp_max+"°C. ", end = "")
		elif aleatorio == 1:
				print ("Temperatura maxima de "+temp_max+"°C e temperatura minima de "+temp_min+"°C. ", end = "")
		elif aleatorio == 2:
				print ("Temperatura variando entre "+temp_min+"°C e "+temp_max+"°C. ", end = "")
		elif aleatorio == 3:
				print ("Maxima prevista de "+temp_max+"°C e minima de "+temp_min+"°C. ", end = "")
		elif aleatorio == 4:
				print ("Minima prevista de "+temp_min+"°C e maxima de "+temp_max+"°C. ", end = "")

def Grupo_2_2_inicio_frase (temp_min, temp_max):
		aleatorio = (randint(0,4))
		if aleatorio == 0:
				print ("Temperatura minima prevista de "+temp_min+"°C e maxima de "+temp_max+"°C, ", end = "")
		elif aleatorio == 1:
				print ("Temperatura maxima de "+temp_max+"°C e temperatura minima de "+temp_min+"°C, ", end = "")
		elif aleatorio == 2:
				print ("Temperatura variando entre "+temp_min+"°C e "+temp_max+"°C, ", end = "")
		elif aleatorio == 3:
				print ("Maxima prevista de "+temp_max+"°C e minima de "+temp_min+"°C, ", end = "")
		elif aleatorio == 4:
				print ("Minima prevista de "+temp_min+"°C e maxima de "+temp_max+"°C, ", end = "")

def Grupo_2_3_no_fim_de_frase ( temp_min, temp_max):
		aleatorio = (randint(0,4))
		if aleatorio == 0:
				print ("temperatura minima de "+temp_min+"°C e maxima de "+temp_max+"°C. ", end = "")
		elif aleatorio == 1:
				print ("temperatura maxima de "+temp_max+"°C e temperatura minima de "+temp_min+"°C. ", end = "")
		elif aleatorio == 2:
				print ("temperatura variando entre "+temp_min+"°C e "+temp_max+"°C. ", end = "")
		elif aleatorio == 3:
				print ("maxima de "+temp_max+"°C e minima de "+temp_min+"°C. ", end = "")
		elif aleatorio == 4:
				print ("minima de "+temp_min+"°C e maxima de "+temp_max+"°C. ", end = "")

def Grupo_3_1_frase_completa ( umidade_min, umidade_max):
		aleatorio = (randint(0,4))
		if aleatorio == 0:
				print ("Umidade variando entre "+umidade_min+" e "+umidade_max+". ", end = "")
		elif aleatorio == 1:
				print ("Umidade minima prevista de "+umidade_min+" e maxima de "+umidade_max+". ", end = "")
		elif aleatorio == 2:
				print ("Umidade maxima de "+umidade_max+" e minima de "+umidade_min+". ", end = "")
		elif aleatorio == 3:
				print ("Umidade prevista de "+umidade_max+" e "+umidade_min+". ", end = "")
		elif aleatorio == 4:
				print ("Umidade prevista entre "+umidade_min+" e "+umidade_max+". ", end = "")

def Grupo_3_2_no_inicio_de_frase ( umidade_min, umidade_max):
		aleatorio = (randint(0,4))
		if aleatorio == 0:
				print ("Umidade variando entre "+umidade_min+" e "+umidade_max+" e ", end = "")
		elif aleatorio == 1:
				print ("Umidade minima prevista de "+umidade_min+" e maxima de "+umidade_max+" e ", end = "")
		elif aleatorio == 2:
				print ("Umidade maxima de "+umidade_max+" e minima de "+umidade_min+" e ", end = "")
		elif aleatorio == 3:
				print ("Umidade prevista de "+umidade_max+" e "+umidade_min+" e ", end = "")
		elif aleatorio == 4:
				print ("Umidade prevista entre "+umidade_min+" e "+umidade_max+" e ", end = "")

def Grupo_3_3_no_fim_de_frase ( umidade_min, umidade_max):
		aleatorio = (randint(0,4))
		if aleatorio == 0:
				print ("com umidade variando entre "+umidade_min+" e "+umidade_max+". ", end = "")
		elif aleatorio == 1:
				print ("com umidade minima prevista de "+umidade_min+" e maxima de "+umidade_max+". ", end = "")
		elif aleatorio == 2:
				print ("com umidade maxima de "+umidade_max+" e minima de "+umidade_min+". ", end = "")
		elif aleatorio == 3:
				print ("com umidade prevista de "+umidade_max+" e "+umidade_min+". ", end = "")
		elif aleatorio == 4:
				print ("com umidade prevista entre "+umidade_min+" e "+umidade_max+". ", end = "")

def Grupo_4_1_frase_completa ( texto_manha,  texto_tarde,  texto_noite):
		if ( (texto_manha==texto_tarde) and (texto_manha==texto_noite)):
				aleatorio = (randint(0,3))
				if aleatorio == 0:
						print (texto_manha+"pela manha e permanece assim ao longo do dia e da noite. ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower()#umidade_minima.replace("<b>","")
						print ("Ceu "+texto_manha+" permanece assim durante todo dia e noite. ", end = "")
				elif aleatorio == 2:
						print (texto_manha+" durante todo dia e noite. ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower()
						print ("De manha, a tarde e a noite, ceu se mantém "+texto_manha+". ", end = "")

		elif ( (texto_manha==texto_tarde) and (texto_manha!=texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu amanhece "+texto_manha+" e permanece assim ao longo do dia, mas fica "+texto_noite+" da noite. ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" permanece assim durante todo dia. a noite, ceu "+texto_noite+". ", end = "")
				elif aleatorio == 2:
						texto_noite = texto_noite.lower()
						print (texto_manha+" durante todo o dia. A noite, ceu "+texto_noite+". ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("De manha e a tarde, ceu se mantém "+texto_manha+", mas fica "+texto_noite+" durante a noite. ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("De manha e a tarde, ceu se mantém "+texto_manha+", mas fica "+texto_noite+" durante a noite. ", end = "")

		elif ((texto_manha!=texto_tarde) and (texto_tarde==texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu amanhece "+texto_manha+", mas fica "+texto_noite+" durante a tarde e permanece assim ao longo da noite. ")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("De manha, ceu "+texto_manha+". Durante a tarde, ceu "+texto_noite+" que permanece assim a noite. ")
				elif aleatorio == 2:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante toda manha. A tarde e a noite, ceu "+texto_noite+". ")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("De manha, ceu se mantem "+texto_manha+", mas fica "+texto_noite+" durante a tarde e a noite. ")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("De manha e a tarde, ceu se mantem "+texto_manha+", mas acaba "+texto_noite+" no resto do dia. ")

		elif ((texto_manha!=texto_tarde) and (texto_manha==texto_noite)):
				aleatorio = (randint(0,3))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("ceu amanhece "+texto_manha+", se torna "+texto_tarde+" ao longo do dia e volta a ficar "+texto_noite+" a noite. ")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("ceu amanhece "+texto_manha+", mas fica "+texto_tarde+" assim durante todo dia. a noite, ceu "+texto_noite+". ")
				elif aleatorio == 2:
						texto_tarde = texto_tarde.lower()
						print (texto_manha+" durante todo o dia e noite, mas ceu fica "+texto_tarde+" na parte da tarde. ")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("De manha, ceu se mantem "+texto_manha+", mas deve ficar "+texto_tarde+" na parte da tarde e voltar a ficar "+texto_noite+" durante a noite. ")

		elif ((texto_manha!=texto_tarde) and (texto_manha!=texto_noite) and (texto_tarde!=texto_noite)):
				aleatorio = (randint(0,3))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("ceu amanhece "+texto_manha+", se torna "+texto_tarde+" ao longo do dia e fica "+texto_noite+" a noite. ")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("ceu amanhece "+texto_manha+", mas fica "+texto_tarde+" assim durante todo dia. A noite, ceu "+texto_noite+". ")
				elif aleatorio == 2:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("ceu amanhece "+texto_manha+", se torna "+texto_tarde+" ao longo do dia e fica "+texto_noite+" a noite. ")
				elif aleatorio == 3:
						texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print (texto_manha+" durante toda a manha, mas ceu fica "+texto_tarde+" na parte da tarde. "+texto_noite+" a noite. ")

def Grupo_4_2_inicio_de_lide ( texto_manha,  texto_tarde,  texto_noite):
		if ( (texto_manha==texto_tarde) and (texto_manha==texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower()
						print ("Amanhece o dia "+texto_manha+" e permanece assim ate a noite, ", end = "")
				elif aleatorio == 1:
						print (texto_manha+" durante todo dia e noite ", end = "")
				elif aleatorio == 2:
						print (texto_manha+" eh o ceu durante todo o dia ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower()
						print ("De manha, ceu "+texto_manha+", permanece assim ao longo do dia ", end = "")
				elif aleatorio == 4:
						print (texto_manha+" durante todo dia e noite ", end = "")

		elif ( (texto_manha==texto_tarde) and (texto_manha!=texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Amanhece com ceu "+texto_manha+" e permanece assim ao longo do dia, mas fica "+texto_noite+" a noite ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante todo dia e noite "+texto_noite+" ", end = "")
				elif aleatorio == 2:
						texto_noite = texto_noite.lower()
						print (texto_manha+" eh o ceu durante todo o dia, enquanto a noite ele fica "+texto_noite+" ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante todo dia e noite "+texto_noite+" ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Amanhece com ceu "+texto_manha+" e permanece assim ao longo do dia, mas fica "+texto_noite+" a noite ", end = "")

		elif ( (texto_manha!=texto_tarde) and (texto_manha==texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("Amanhece com ceu "+texto_manha+", mas fica "+texto_tarde+" ao longo do dia e volta a ficar "+texto_noite+" a noite ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante de manha, "+texto_tarde+" a tarde e noite "+texto_noite+" ", end = "")
				elif aleatorio == 2:
						texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print (texto_manha+" eh o ceu durante toda manha e noite, mas ao longo da tarde ele fica "+texto_tarde+" ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante toda a manha, tarde com ceu "+texto_tarde+" e noite volta ao "+texto_noite+" ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante todo dia e noite "+texto_noite+" ")

		elif ((texto_manha!=texto_tarde) and (texto_tarde==texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Amanhece com ceu "+texto_manha+", mas fica "+texto_noite+" durante tarde e noite. ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante a manha e "+texto_noite+" no resto do dia ", end = "")
				elif aleatorio == 2:
						texto_noite = texto_noite.lower()
						print (texto_manha+" eh o ceu durante a manha, enquanto ele fica "+texto_noite+" e permanece assim ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante toda a manha, mas fica "+texto_noite+" ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante a manha e "+texto_noite+" no resto do dia ", end = "")

		elif ((texto_manha!=texto_tarde) and (texto_tarde!=texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("Amanhece com ceu "+texto_manha+", mas fica "+texto_tarde+" ao longo do dia e "+texto_noite+" a noite ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante a manha, a tarde fica "+texto_tarde+" e noite "+texto_noite+" ", end = "")
				elif aleatorio == 2:
						texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print (texto_manha+" eh o ceu durante toda manha, mas ao longo da tarde ele fica "+texto_tarde+" e a noite permanece "+texto_noite+" ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("Ceu "+texto_manha+" durante toda a manha, tarde com ceu "+texto_tarde+" e noite no "+texto_noite+" ", end = "")
				elif aleatorio == 4:
						texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print (texto_manha+" eh o ceu durante toda manha, mas ao longo da tarde ele fica "+texto_tarde+" e a noite permanece "+texto_noite+" ", end = "")

def Grupo_4_3_fim_da_frase ( texto_manha,  texto_tarde,  texto_noite):
		if ( (texto_manha==texto_tarde) and (texto_manha==texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower()
						print ("amanhece o dia "+texto_manha+" e permanece assim ate a noite. ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower()
						print ("permanece "+texto_manha+" durante todo dia e noite. ", end = "")
				elif aleatorio == 2:
						texto_manha = texto_manha.lower()
						print ("tem ceu "+texto_manha+" de manha, a tarde e a noite. ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower()
						print ("permanece durante dia e noite com ceu "+texto_manha+". ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower()
						print ("permanece durante dia e noite com ceu "+texto_manha+". ", end = "")

		elif ( (texto_manha==texto_tarde) and (texto_manha!=texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("amanhece com ceu "+texto_manha+" e permanece assim ao longo do dia, mas fica "+texto_noite+" a noite. ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("permanece "+texto_manha+" durante todo dia, mas a noite fica "+texto_noite+". ",end = "")
				elif aleatorio == 2:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("tem ceu "+texto_manha+" de manha e a tarde , mas noite termina com ceu "+texto_noite+". ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("amanhece o ceu "+texto_manha+" e permanece assim ao longo do dia, mas fica "+texto_noite+" a noite. ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("permanece durante todo o dia com ceu "+texto_manha+". a noite, ceu fica "+texto_noite+". ", end = "")

		elif ( (texto_manha!=texto_tarde) and (texto_manha==texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("amanhece com ceu "+texto_manha+", mas fica "+texto_tarde+" ao longo do dia e volta a ficar "+texto_noite+" a noite. ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("permanece "+texto_manha+" durante manha e noite, mas tarde pode ser "+texto_tarde+". ", end = "")
				elif aleatorio == 2:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("tem ceu "+texto_manha+" de manha, mas fica "+texto_tarde+" e volta a ficar "+texto_noite+" a noite. ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("amanhece o ceu "+texto_manha+", mas se torna "+texto_tarde+" e volta a ficar "+texto_noite+" a noite. ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("amanhece o ceu "+texto_manha+", que vai ficar "+texto_tarde+" ao longo do dia, mas volta a ficar "+texto_noite+" a noite. ", end = "")

		elif ((texto_manha!=texto_tarde) and (texto_tarde==texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("amanhece o ceu "+texto_manha+", mas fica "+texto_noite+" durante o resto do dia. ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("permanece "+texto_manha+" durante toda a manha, mas a tarde fica "+texto_noite+". ", end = "")
				elif aleatorio == 2:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("tem ceu "+texto_manha+" de manha, mas tarde e noite terminam com ceu "+texto_noite+". ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("permanece o ceu "+texto_manha+" durante a manha, mas fica "+texto_noite+" mais tarde. ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_noite = texto_noite.lower()
						print ("amanhece o ceu "+texto_manha+", mas fica "+texto_noite+" durante o resto do dia. ", end = "")


		elif ((texto_manha!=texto_tarde) and (texto_tarde!=texto_noite)):
				aleatorio = (randint(0,4))
				if aleatorio == 0:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("amanhece o ceu "+texto_manha+", que vai ficar "+texto_tarde+" ao longo do dia e "+texto_noite+" a noite. ", end = "")
				elif aleatorio == 1:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("permanece "+texto_manha+" durante a manha, fica "+texto_tarde+" a tarde. Noite "+texto_noite+". ", end = "")
				elif aleatorio == 2:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("tem ceu "+texto_manha+" de manha, mas fica "+texto_tarde+" ao longo do dia e "+texto_noite+" a noite. ", end = "")
				elif aleatorio == 3:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("amanhece o ceu "+texto_manha+", mas se torna "+texto_tarde+" e fica "+texto_noite+" a noite. ", end = "")
				elif aleatorio == 4:
						texto_manha = texto_manha.lower(); texto_tarde = texto_tarde.lower(); texto_noite = texto_noite.lower()
						print ("amanhece o ceu "+texto_manha+", que vai ficar "+texto_tarde+" ao longo do dia e acaba "+texto_noite+" a noite. ", end = "")

def FuncaoTemperatura (theurl): # Essa funcao busca todas as temperaturas da pagina
	
	thepage = urllib.request.urlopen(theurl)
	soup = BeautifulSoup(thepage, "html.parser")
	lista = ["ola", "mundo", "aqui", "estamos", "te"]
	i = 0
	for temps in soup.findAll('div', {"id":"quadro1_interno_circulo_img"}):
		lista[i] = temps.find('input')
		i = i + 1

	lista[0] = str(lista[0]); lista[1] = str(lista[1]); lista[2] = str(lista[2]); lista[3] = str(lista[3]); lista[4] = str(lista[4])
	a = lista[0][114]; b = lista[0][115]
	temp_min_hoje = a+b
	a = lista[1][114]; b = lista[1][115]
	temp_max_hoje = a+b
	a = lista[2][114]; b = lista[2][115]
	temp_min_amanha = a+b
	a = lista[3][114]; b = lista[3][115]
	temp_max_amanha = a+b

	return (temp_min_hoje, temp_max_hoje, temp_min_amanha, temp_max_amanha)

def FuncaoUmidadeRelativa(theurl): # Essa funcao busca todas as temperaturas da pagina
	
	thepage = urllib.request.urlopen(theurl)
	soup = BeautifulSoup(thepage, "html.parser")
	lista = ["ola", "mundo"]
	i = 0
	for temps in soup.findAll('div', {"id":"quadro1_interno_dados_txt_umidade_min"}):
		lista[i] = temps.find('b')
		i = i + 1

	umidade_min_hoje = str(lista[0])
	umidade_min_hoje = str(umidade_min_hoje)
	umidade_min_hoje = umidade_min_hoje.replace("<b>","")  # reescreve a string obtida de uma maneira mais bonita
	umidade_min_hoje = umidade_min_hoje.replace("</b>","")
	umidade_min_amanha = str(lista[1])
	umidade_min_amanha = str(umidade_min_amanha)
	umidade_min_amanha = umidade_min_amanha.replace("<b>","")  # reescreve a string obtida de uma maneira mais bonita
	umidade_min_amanha = umidade_min_amanha.replace("</b>","")


	i = 0 
	for temps in soup.findAll('div', {"id":"quadro1_interno_dados_txt_umidade_max"}):
		lista[i] = temps.find('b')
		i = i + 1

	umidade_max_hoje = str(lista[0])
	umidade_max_hoje = str(umidade_max_hoje)
	umidade_max_hoje = umidade_max_hoje.replace("<b>","")  # reescreve a string obtida de uma maneira mais bonita
	umidade_max_hoje = umidade_max_hoje.replace("</b>","")

	umidade_max_amanha = str(lista[1])
	umidade_max_amanha = str(umidade_max_amanha)
	umidade_max_amanha = umidade_max_amanha.replace("<b>","")  # reescreve a string obtida de uma maneira mais bonita
	umidade_max_amanha = umidade_max_amanha.replace("</b>","")


	return (umidade_min_hoje, umidade_max_hoje, umidade_min_amanha, umidade_max_amanha)

def RaspagemDeDados (capital_escolhida, quando):
	if capital_escolhida == "1":
				capital_escolhida = "ARACAJU - SE"
				theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2800308'
	elif capital_escolhida == "2":
					capital_escolhida = "BELEM - PA"
					theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=1501402'
	elif capital_escolhida == "3":
				capital_escolhida = "BELO HORIZONTE - MG"
				theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=3106200'
				
	elif capital_escolhida == "4":
						 capital_escolhida = "BOA VISTA - RR"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=1400100'

	elif capital_escolhida == "5":
						 capital_escolhida = "BRASILIA - DF"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=5300108'

	elif capital_escolhida == "6":
						 capital_escolhida = "CAMPO GRANDE - MS"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=5002704'

	elif capital_escolhida == "7":
						 capital_escolhida = "CUIABA - MT"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=5103403'

	elif capital_escolhida == "8":
						 capital_escolhida = "CURITIBA - PR"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=4106902'

	elif capital_escolhida == "9":
						 capital_escolhida = "FLORIANOPOLIS - SC"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=4205407'

	elif capital_escolhida == "10":
						 capital_escolhida = "FORTALEZA - CE"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2304400'

	elif capital_escolhida == "11":
						 capital_escolhida = "GOIANIA - GO"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=5208707'

	elif capital_escolhida == "12":
						 capital_escolhida = "JOAO PESSOA - PB"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2507507'

	elif capital_escolhida == "13":
						 capital_escolhida = "MACAPA - AP"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=1600303'

	elif capital_escolhida == "14":
						 capital_escolhida = "MACEIO  - AL"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2704302'

	elif capital_escolhida == "15":
						 capital_escolhida = "MANAUS - AM"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=1302603'

	elif capital_escolhida == "16":
						 capital_escolhida = "NATAL - RN"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2408102'

	elif capital_escolhida == "17":
						 capital_escolhida = "PALMAS - TO"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=1721000'

	elif capital_escolhida == "18":
						 capital_escolhida = "PORTO ALEGRE - RS"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=4314902'

	elif capital_escolhida == "19":
						 capital_escolhida = "PORTO VELHO - RO"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=1100205'

	elif capital_escolhida == "20":
						 capital_escolhida = "RECIFE - PE"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2611606'

	elif capital_escolhida == "21":
						 capital_escolhida = "RIO BRANCO - AC"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=1200401'

	elif capital_escolhida == "22":
						 capital_escolhida = "RIO DE JANEIRO - RJ"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=3304557'

	elif capital_escolhida == "23":
						 capital_escolhida = "SALVADOR - BA"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2927408'

	elif capital_escolhida == "24":
						 capital_escolhida = "SAO LUIS - MA"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2111300'

	elif capital_escolhida == "25":
						 capital_escolhida = "SAO PAULO - SP"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=3550308'

	elif capital_escolhida == "26":
						 capital_escolhida = "TERESINA - PI"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=2211001'

	elif capital_escolhida == "27":
						 capital_escolhida = "VITORIA - ES"
						 theurl = 'http://www.inmet.gov.br/portal/index.php?r=tempo2/verProximosDias&code=3205309'


	thepage = urllib.request.urlopen(theurl)
	soup = BeautifulSoup(thepage, "html.parser")
	
	if quando == "hoje":
		#Umidade
		umidade_minima, umidade_maxima, lixo1, lixo2 = FuncaoUmidadeRelativa(theurl)


		#Quadro manha
		texto_manha = soup.find('div', {"id":"quadro1_interno_manha_quadro_txt"}).find('i')
		texto_manha = str(texto_manha)
		texto_manha = texto_manha.replace("<i>","")			# reescreve a string obtida de uma maneira mais bonita
		texto_manha = texto_manha.replace(" </i>","")


		#Quadro Tarde
		texto_tarde = soup.find('div', {"id":"quadro1_interno_tarde_quadro_txt2"}).find('i')
		texto_tarde = str(texto_tarde)
		texto_tarde = texto_tarde.replace("<i>","")			# reescreve a string obtida de uma maneira mais bonita
		texto_tarde = texto_tarde.replace(" </i>","")


		#Quadro Noite
		texto_noite = soup.find('div', {"id":"quadro1_interno_noite_quadro_txt3"}).find('i')
		texto_noite = str(texto_noite)
		texto_noite = texto_noite.replace("<i>","")			# reescreve a string obtida de uma maneira mais bonita
		texto_noite = texto_noite.replace(" </i>","")

		#Quadro Temperatura maxima
		temp_min, temp_max, lixo1, lixo2 = FuncaoTemperatura(theurl)


	elif quando == "amanha":

				#Umidade
		lixo1, lixo2, umidade_minima, umidade_maxima = FuncaoUmidadeRelativa(theurl)


		#Quadro manha
		texto_manha = soup.find('div', {"id":"quadro2_interno_manha_quadro_txt"}).find('i')
		texto_manha = str(texto_manha)
		texto_manha = texto_manha.replace("<i>","")			# reescreve a string obtida de uma maneira mais bonita
		texto_manha = texto_manha.replace(" </i>","")



		#Quadro Tarde
		texto_tarde = soup.find('div', {"id":"quadro2_interno_tarde_quadro_txt2"}).find('i')
		texto_tarde = str(texto_tarde)
		texto_tarde = texto_tarde.replace("<i>","")			# reescreve a string obtida de uma maneira mais bonita
		texto_tarde = texto_tarde.replace(" </i>","")


		#Quadro Noite
		texto_noite = soup.find('div', {"id":"quadro2_interno_noite_quadro_txt3"}).find('i')
		texto_noite = str(texto_noite)
		texto_noite = texto_noite.replace("<i>","")			# reescreve a string obtida de uma maneira mais bonita
		texto_noite = texto_noite.replace(" </i>","")

		#Quadro Temperatura
		lixo1, lixo2, temp_min, temp_max = FuncaoTemperatura (theurl)

	
	return (capital_escolhida, temp_max , temp_min , texto_manha , texto_tarde , texto_noite , umidade_minima , umidade_maxima)

def Escolher_capital ():
			print("Este programa informara a umidade, temperatura e o tempo ao longo do dia.")
			print("Escolha uma das capitais a seguir pelo numero:")
			print("1 - ARACAJU - SE")
			print("2 - BELEM - PA")
			print("3 - BELO HORIZONTE - MG")
			print("4 - BOA VISTA - RR")
			print("5 - BRASILIA - DF")
			print("6 - CAMPO GRANDE - MS")
			print("7 - CUIABA - MT")
			print("8 - CURITIBA - PR")
			print("9 - FLORIANOPOLIS - SC")
			print("10 - FORTALEZA - CE")
			print("11 - GOIANIA - GO")
			print("12 - JOAO PESSOA - PB")
			print("13 - MACAPA - AP")
			print("14 - MACEIO  - AL")
			print("15 - MANAUS - AM")
			print("16 - NATAL - RN")
			print("17 - PALMAS - TO")
			print("18 - PORTO ALEGRE - RS")
			print("19 - PORTO VELHO - RO")
			print("20 - RECIFE - PE")
			print("21 - RIO BRANCO - AC")
			print("22 - RIO DE JANEIRO - RJ")
			print("23 - SALVADOR - BA")
			print("24 - SAO LUIS - MA")
			print("25 - SAO PAULO - SP")
			print("26 - TERESINA - PI")
			print("27 - VITORIA - ES")
			capital_escolhida = input("Escolha uma das capitais a seguir pelo numero: ") # capital_escolhida deve ser um numero estre 1 e 27
			quando = input("Qual dia(hoje ou amanha)? ")
			if quando == "hoje":
				Quando = "Hoje"
			elif quando == "amanha":
				Quando = "Amanha"

			return (capital_escolhida, quando, Quando)


(qual_capital, quando, Quando) = Escolher_capital()  #funcao que pede a cidade

qual_capital, temp_max, temp_min, texto_manha, texto_tarde, texto_noite, umidade_min, umidade_max = RaspagemDeDados(qual_capital, quando)


um_ja_foi = 0
dois_ja_foi = 0
tres_ja_foi = 0
quatro_ja_foi = 0  #Variaveis usadas para indicar quais dados ja foram escolhidos na parte randomica
# grupo 1: nome da cidade
# grupo 2: temperatura maxima e minima
# grupo 3: umidade maxima e minima
# grupo 4: textos sobre o tempo da manha, tarde e noite

aleatorio = (randint(1, 4))

if aleatorio == 3:  #Nao queremos que a informacao comece por umidade
	aleatorio = 4


if aleatorio == 1:
	um_ja_foi = 1
	Grupo_1_1_IniciarLide(qual_capital, quando, Quando)

elif aleatorio == 2:
		dois_ja_foi = 1
		Grupo_2_2_inicio_frase(temp_min, temp_max)
elif aleatorio == 4:
		quatro_ja_foi = 1
		Grupo_4_2_inicio_de_lide(texto_manha, texto_tarde, texto_noite)

# Ja temos a primeira frase INCOMPLETA na tela e so temos mais TRES informacoes a serem usadas.

if um_ja_foi == 0: # o grupo 1 (nome da cidade) precisa sair ou na primeira ou na segunda frase
	um_ja_foi = 1
	Grupo_1_2_no_fim_da_frase(qual_capital, quando, Quando)
else: # aqui, o grupo 1 foi sorteado na variavel aleatoria. Precisamos agora completar a primeira frase
	aleatorio = (randint(2, 4))

	if aleatorio == 3:
		aleatorio = 2 # novamente, nao queremos que umidade seja a primeira informacao

	if aleatorio == 2:
		dois_ja_foi = 1
		Grupo_2_3_no_fim_de_frase(temp_min, temp_max)
	elif aleatorio == 4:
		quatro_ja_foi = 1
		Grupo_4_3_fim_da_frase(texto_manha, texto_tarde, texto_noite)

# Ja temos a primeira frase COMPLETA na tela e so temos mais DUAS informacoes a serem usadas. (umidade e mais outra)

aleatorio = (randint(0, 3)) # usamos outras variavel aleatoria para randomizar as duas ultimas informacoes
if aleatorio == 0: # se der zero, usaremos duas frases completas pra finalizar a previsao do tempo
	Grupo_3_1_frase_completa(umidade_min, umidade_max)
	tres_ja_foi = 1
	if quatro_ja_foi == 0:
		Grupo_4_1_frase_completa(texto_manha, texto_tarde, texto_noite)
		quatro_ja_foi = 1
	else:
		Grupo_2_1_frase_completa(temp_min, temp_max) #acaba, ja demos todas as informacoes.

elif aleatorio == 1:
		if quatro_ja_foi == 0:
			Grupo_4_1_frase_completa(texto_manha, texto_tarde, texto_noite)
		else:
			Grupo_2_1_frase_completa(temp_min, temp_max)
		Grupo_3_1_frase_completa(umidade_min, umidade_max)

if aleatorio == 2:
	Grupo_3_2_no_inicio_de_frase(umidade_min, umidade_max)
	tres_ja_foi = 1
	if quatro_ja_foi == 0:
		Grupo_4_3_fim_da_frase(texto_manha, texto_tarde, texto_noite)
	else:
		Grupo_2_3_no_fim_de_frase(temp_min, temp_max)

elif aleatorio == 3:
		if (quatro_ja_foi == 0):
			Grupo_4_2_inicio_de_lide(texto_manha, texto_tarde, texto_noite)
		else:
			Grupo_2_2_inicio_frase(temp_min, temp_max)
		Grupo_3_3_no_fim_de_frase(umidade_min, umidade_max)
print("")
print("Fonte: INMET")
print("")
