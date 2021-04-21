#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Descripción:	Implementación de la técnica de Algoritmos de reemplazo GDSF
#			Basada en el uso de colas con prioridad
#			GDSF elimina el nodo con menor score H y tiene en cuenta su frecuencia
#			H = L + C*F
# Autor: Gabriel Tolosa - Matías Rocha - UNLu
# Modificado: 5/4/17


import Queue
import time

class Elemento(object):
    def __init__(self, score, query):
        self.score = float("{0:.4f}".format(score))
        self.query = query
        return
        
	def __cmp__(self, other):
		return cmp(self.score, other.score)

class GDSCache():
	
	def __init__(self, s, path):
		self.max_size = s
		self.size = 0
		self.cache = {}
		self.pathCosto = path
		self.cacheCost = self.cargarCostos()
		self.cachePQ = Queue.PriorityQueue()
		self.L = 0
		self.F = {}
		self.hits = 0
		self.miss = 0
		self.corrects = 0
		self.totalHIT = 0
		
		
	def insert(self, query):		
		if (self.size >= self.max_size):
			#Si el tamaño del cache actual esta al tope, debo desalojar uno
			salir = True
			while salir:
				next_element = self.cachePQ.get()	#Obtengo el elemento de menor score del cachePQ
				clave = next_element.query	#Obtengo su query
				hValue = next_element.score	#Obtengo su score
				try:
					#Tiro un try, si el elemento esta en el cache no tira error
					cacheValue = self.cache[clave]	#Obtengo el score del cache propiamennte dicho
					if hValue != cacheValue:
						#Si tienen diferentes hvalue es un elemento "invalido" por ende lo elimino de la PQ y sigo iterando
						#self.cachePQ.get()
						pass
					else:
						#Si son iguales, quiere decir que el elemento es válido por ende es eliminado del caché
						self.size -= 1 #Decremento en 1 el caché
						self.L = cacheValue #Asigno el L con el menor
						del self.cache[clave] #Borro de mi diccionario cache el elemento
						#del self.F[clave] #Borro de mi diccionario cache el elemento
						salir = False
				except:
					#Si el try tira error, quiere decir que no está en el caché. No hago nada y vuelvo a pedir
					pass
		
		#Inserto el nuevo elemento
		score = float(self.L) + ((float(self.cacheCost[query]) / 1) * float(self.F[query]))	#Calculo el score
		self.cache[query] = float("{0:.4f}".format(score))
		self.size += 1 #Incremento en 1 el caché
		e = Elemento(score, query)		#Elemento a ingresar
		self.cachePQ.put(e)
		return
					
	def update(self, query):
			#Si el elemento esta en el caché, solo actualizo el Hvalue
			self.F[query] += 1	#Sumo uno a la freq
			score = float(self.L) + ((float(self.cacheCost[query]) / 1) * float(self.F[query]))	#Calculo el score
			e = Elemento(score, query)		#Elemento a ingresar
			self.cachePQ.put(e)	#Encolo elemento
			self.cache[query] = float("{0:.4f}".format(score)) #Actualizo el score en mi cache
			return
			
	def cargarCostos(self):
		costos = {}
		try:
			archivo = open (self.pathCosto, "r")
		except e:
			print "Error de lectura: " + e
		linea = archivo.readline()	#Leo linea del archivo de info
		print "Cargando costos en memoria"
		while linea != "":
			split = linea.split("\t:\t")	#Spliteo por tab
			costos[split[0].strip()] = float(split[1].strip())	#Cargo en la query con su respectivo costo
			linea = archivo.readline()	#Leo linea del archivo de info
		print "Proceso terminado"
		archivo.close()
		return costos
				
	def accessCache(self, query, hitBand):
		#print "Query: ", query
		tf = 0
		try:
			costo = self.cacheCost[query.strip()]	#Si el costo existe se lo asigno
		except:
			costo = 0	#Si no existe le pongo 0
		if float(costo) != 0:
		#Si el costo no es cero			
			self.corrects += 1
			if (query in self.cache):
				#Si la query esta en la caché, es decir hay un HIT actualizo el score	
				
				self.update(query.strip())
				if hitBand:
					#Si la bandera de hits esta activa, cuento un hit
					self.hits += 1
			else:
			#Si el elemento no esta en el caché, lo agrego
				if (query in self.F):
					pass
				else:
					self.F[query.strip()] = 1
					
				self.insert(query.strip())
				tf = costo 	#Si el query no esta en el cache, simulo costo con el de terrier
				if hitBand:
					#Si la bandera de hits esta activa, cuento un miss
					self.miss += 1
		return tf
			
				
	def getTotalHit(self):
		print self.hits
		print self.miss
		print self.corrects
		total = float(self.hits) / (float(self.hits) + float(self.miss))
		return total
		
	def getTotalCorrects(self):
		return self.corrects
