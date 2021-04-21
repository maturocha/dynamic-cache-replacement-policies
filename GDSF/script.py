#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Descripción:	Script que levanta el script de testeo 
# Autor: Matías Rocha - UNLu
# Modificado: 10/11/16
import commands

def main():
	finalList = []
	archivo = open('/storage/matur/GDSF/testeos.txt', 'r') 
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
		result=commands.getoutput('/usr/bin/python /storage/matur/GDSF/main.py %s %s %d %d %d' % ("/storage/matur/querys/queryLog.txt", "/storage/matur/costos/tiemposSegados.txt", int(info[0]), int(info[1]), int(info[2])))
		print result
		c += 1

if __name__ == "__main__":
    main() 
