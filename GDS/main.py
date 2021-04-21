#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Descripción:	Testeo de la implementación de la técnica de Algoritmos de reemplazo GDS
# Autor: Matías Rocha - UNLu
# Modificado: 15/12/16
 
import sys
import time
#sys.path.append("/home/matur/PIR/Implementaciones/GDS/lib")
sys.path.append("/storage/matur/GDS/lib")

import parametros
import GDScache


def procesar(tam, warm, test):
	print "Leyendo el archivos de queries y procesando"
	cache = GDScache.GDSCache(tam)	#Declaro el cache GDS con un tamaño dado
	c = parametros.Parameters()
	path = c.getPathQuery() #Obtengo path de querys
	tiempo = 0
	try:
		archivo = open (path, "r")
	except e:
		print "Error de lectura: " + e
	cW = 1 #contador de calentamiento
	cQ = 1	#Contador de queries leidas
	query = archivo.readline()	#leo la primer linea
	if warm != 0:
		#Si el calentamiento es mayor a 0, hay calentamiento
		while (query != '') and (cW < int(warm)):
			#Mientras no sea linea vacia o Mientras no haya terminado el calentamiento
			tiempo += cache.accessCache(query.strip(), False) #Cacheo pero no hago el recuento de hit, porque es calentamiento
			cW += 1 #Sumo el contador de calentamiento
			cO += 1
			query = archivo.readline()	#leo otra linea
	while (query != '') and (cQ <= test):
		tiempo += cache.accessCache(query.strip(), True) #Cacheo y hago el recuento de hit
		cQ += 1 #Contador de queries
		query = archivo.readline()	#leo otra linea
	
	print "Proceso terminado"
	archivo.close()
	hit = cache.getTotalHit()
	corrects = cache.getTotalCorrects()
	return hit, corrects, tiempo

def createLog(tam, warm, test, hit, corrects, time):
	try:
		log = open('estadisticasGDS.log', 'a+') 
	except e:
		print e
	try:
		linea = log.readline()
		if linea[0] != "Q":
			log.write("%s \t\t\t %s \t\t\t\t %s \t\t\t\t\t %s \t\t\t\t\t\t\t\t %s \t\t\t\t\t\t\t %s\n" % ("Queries (cant)", "Cache Size (Elements)","Warm-up", "Hit Ratio", "Corrects", "Time"))
	except:
		log.write("%s \t\t\t %s \t\t\t\t %s \t\t\t\t\t %s \t\t\t\t\t\t\t\t %s \t\t\t\t\t\t\t %s\n" % ("Queries (cant)", "Cache Size (Elements)","Warm-up", "Hit Ratio", "Corrects", "Time"))
	log.write("%s \t\t\t\t\t %s \t\t\t\t\t\t\t %s \t\t\t\t\t\t\t %s \t\t\t\t\t\t\t %s \t\t\t\t\t\t\t %s\n" % (str(test), str(tam), str(warm), str(hit), str(corrects), str(float("{0:.4f}".format(time)))))
	log.close()


def main ():
	#Instancio la clase parametros
	print "LLEGA"
	p = parametros.Parametros()
	tam = p.getSize()
	warm = p.getQuery_warm()
	test = p.getQuery_test()
	#Procesamiento de las queries, mediante el archivo de texto
	hit, corrects, tiempo = procesar(tam, warm, test)
	#Creacion del log
	createLog(tam, warm, test, hit, corrects, tiempo)

if __name__ == "__main__":
    main() 
