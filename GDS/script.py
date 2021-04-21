#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Descripción:	Script que levanta el main de GDS con parametros del txt 
# Autor: Matías Rocha - UNLu
# Modificado: 10/11/16
import commands
import os 

def main():
	finalList = []
	path = os.path.dirname(os.path.realpath(__file__))
	archivo = open(path + '/testeos.txt', 'r') 
	linea = archivo.readline() #Saco header
	linea = archivo.readline() #Leo datos
	while linea != "":
		dato = linea.split("\t\t\t\t")
		listD = [dato[0], dato[1], dato[2].strip()]
		finalList.append(listD)
		linea = archivo.readline()
	
	c = 1
	for info in finalList:
		print "Ejecutando prueba %d" %(c)
		result=commands.getoutput('/usr/bin/python %s/main.py %d %d %d' % (path, int(info[0]), int(info[1]), int(info[2])))
		print result
		c += 1

if __name__ == "__main__":
    main() 
