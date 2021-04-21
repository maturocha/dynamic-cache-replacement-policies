#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Descripción:	Testeo de la implementación de la técnica de Algoritmos de reemplazo LRU(Menos recientemente usado) 
#				Las estadisticas que imprime en esta nueva version es el hit-ratio por longitud de queries
# Autor: Matías Rocha - UNLu
# Modificado: 13/11/16
 
import sys
import time
#sys.path.append("lib")
sys.path.append("/storage/matur/GDSF/lib")

import parametros
import GDSCache


def procesar(path, pathC, tam, warm, test):
	tiempo = 0
	cache = GDSCache.GDSCache(tam, pathC)	#Declaro el cache GDS con un tamaño dado
	print "Leyendo el archivos de queries y procesando"
	try:
		print path
		archivo = open (path, "r") 
	except e:
		print "Error de lectura: " + e
		
	query = archivo.readline()	#leo la primer linea
	if warm != 0:
		#Si el calentamiento es mayor a 0, hay calentamiento
		cW = 1 #contador de calentamiento
		while (query != '') and (cW <= int(warm)):
			#Mientras no sea linea vacia o Mientras no haya terminado el calentamiento
			tiempo += cache.accessCache(query.strip(), False) #Cacheo pero no hago el recuento de hit, porque es calentamiento
			cW += 1 #Sumo el contador de calentamiento
			query = archivo.readline()	#leo otra linea
	cQ = 1	#Contador de queries leidas
	while (query != '') and (cQ <= int(test)):
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
		log = open('estadisticasGDSF.log', 'a+') 
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
	p = parametros.Parametros()
	tam = p.getSize()
	path = p.getFile()
	warm = p.getQuery_warm()
	test = p.getQuery_test()
	pathC = p.getFileC()
	#Procesamiento de las queries, mediante el archivo de texto
	hit, corrects, tiempo = procesar(path, pathC, tam, warm, test)
	#Creacion del log
	createLog(tam, warm, test, hit, corrects, tiempo)

if __name__ == "__main__":
    main() 
