#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Descripción:	Testeo de la implementación de la técnica de Algoritmos de reemplazo LRU(Menos recientemente usado) 
#		Arroja tiempos, reales de procesamiento
# Autor: Matías Rocha - UNLu
# Modificado: 3/11/16
 
import sys
import time
#sys.path.append("lib")
sys.path.append("/storage/matur/LRU/lib")

import parametros
import lrucache


def procesar(path, tam, warm, test):
	print "Leyendo el archivos de queries y procesando"
	cache = lrucache.LRUCache(tam)	#Declaro el cache LRU con un tamaño dado
	try:
		archivo = open (path, "r")
	except e:
		print "Error de lectura: " + e
		
	query = archivo.readline()	#leo la primer linea
	if warm != 0:
		#Si el calentamiento es mayor a 0, hay calentamiento
		cW = 1 #contador de calentamiento
		while (query != '') and (cW < int(warm)):
			#Mientras no sea linea vacia o Mientras no haya terminado el calentamiento
			cache.accessPage(query.strip(), False) #Cacheo pero no hago el recuento de hit, porque es calentamiento
			cW += 1 #Sumo el contador de calentamiento
			query = archivo.readline()	#leo otra linea
	cQ = 1	#Contador de queries leidas
	while (query != '') and (cQ <= test):
		cache.accessPage(query.strip(), True) #Cacheo y hago el recuento de hit
		cQ += 1 #Contador de queries
		query = archivo.readline()	#leo otra linea
	
	print "Proceso terminado"
	archivo.close()
	hit = cache.getTotalHit()
	return hit

def createLog(tam, warm, test, hit, time):
	try:
		log = open('estadisticasLRU.log', 'a+') 
	except e:
		print e
	try:
		linea = log.readline()
		if linea[0] != "Q":
			log.write("%s \t\t\t %s \t\t\t\t %s \t\t\t\t %s \t\t\t\t %s\n" % ("Queries (cant)", "Cache Size (Elements)","Warm-up", "Hit Ratio", "Time"))
	except:
		log.write("%s \t\t\t %s \t\t\t\t %s \t\t\t\t %s \t\t\t\t %s\n" % ("Queries (cant)", "Cache Size (Elements)","Warm-up", "Hit Ratio", "Time"))
	log.write("%s \t\t\t\t\t %s \t\t\t\t\t\t\t %s \t\t\t\t\t\t\t %s \t\t\t\t\t\t\t %s\n" % (str(test), str(tam), str(warm), str(hit), str(float("{0:.4f}".format(time)))))
	log.close()


def main ():
	#Instancio la clase parametros
	t1 = time.time()
	p = parametros.Parametros()
	tam = p.getSize()
	path = p.getFile()
	warm = p.getQuery_warm()
	test = p.getQuery_test()
	#Procesamiento de las queries, mediante el archivo de texto
	hit = procesar(path, tam, warm, test)
	print "El hit es de: " + str(hit)
	t2 = time.time()
	tf = t2 -t1
	print "TIEMPO DE EJECUCION: ", tf
	#Creacion del log
	createLog(tam, warm, test, hit, tf)
	

if __name__ == "__main__":
    main() 
