#Import
import os
import numpy
#Variables
alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Funciones
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def limpiarLlave(llave,alfabeto):	#Limpia la llave
	llave = llave.lower()
	llaveLimpia= []
	for c in llave:
		#Si el caracter no esta, lo descarta
		if c in alfabeto:
			#Si no esta anteriormente la agrega a la cadena limpia
			if not (c in llaveLimpia):	llaveLimpia.append(c)
	return llaveLimpia

def generarMatriz(llave,alfabeto):

	return 0

def hill(llave,cadena,encriptar):
	llaveLimpia		= limpiarLlave(llave,alfabeto)
	matriz,mapa		= generarMatriz(llaveLimpia, list(alfabeto))
	#cadenaLimpia	= limpiarCadena(cadena,alfabeto)
	#cadenaProcesada	= encriptarHill(cadenaLimpia,mapa,matriz,modo)
	return 0

#MAIN
while True:
	clear()
	print('*********** Inicio-Hill *************')
	print('********** anlleguziamongu **********\n')
	llave	=input('Ingrese llave:\n> ')
	cadena	=input('\nIngrese cadena:\n> ')
	modo	=input('\n¿Que hacer?:\n\n[Enter: Encriptar]\n[D: Desencriptar]\n\n>: ')
	hill(llave,cadena,modo.lower()!='d')
	if input('\n¿Desea realizar otra accion?: [Enter: continuar] [S: salir]').lower() == 's': break

clear()
