#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Descripción:	Implementación de la técnica de Algoritmos de reemplazo GDS
#			Basada en el uso de Listas enlazadas y nodos, para entender su concepto
#			GDS elimina el nodo con menor score H, donde H = 1 / tamaño(elemento)
# Autor: Matías Rocha - UNLu
# Modificado: 15/12/16

import parametros

class Nodo ():

	def __init__(self, query):
		self.query = query
		self.score = 0 	#El valor es ahora el H(value)
		self.nodoPrev = None
		self.nodoSig = None

 	def getQuery(self):
		return self.query
		
 	def getScore(self):
		return self.score

	def setScore(self, data):
		self.score = float("{0:.4f}".format(data))

	def getPrev(self):
		return self.nodoPrev
		
	def setQuery(self, data):
		self.query = data

	def setPrev(self, nodo):
		self.nodoPrev = nodo

	def getSig(self):
		return self.nodoSig

	def setSig(self, nodo):
		self.nodoSig = nodo
		
	def toString(self):
		return str(self.query) + ":" + str(self.score)
     

class DobleLista():

	def __init__(self, tamanio):
		self.size = tamanio
		self.currSize = 0
		self.head = None
		self.tail = None

	def getHead(self):
		return self.head

	def setHead(nodo):
		self.head = nodo

	def getTail(self):
		return self.tail
	
	def setTail(self, nodo):
		self.tail = nodo

	def getCurrSize (self):
		return self.currSize

	def setCurrSize (self, tamanio):
		self.currSize = tamanio

	def getSize (self):
		return self.size

	def insert(self, query, score):
	#Agrega un nodo a la lista
		pageNode = Nodo(query)		#Nodo a ingresar
		pageNode.setScore(score)	#seteo Score
		if (self.currSize < self.size):	#Si el tamanio es menor al tope
			self.currSize += 1		#Incremento el tamanio actual
		else:
			#Si el tamaño es igual, esta lleno. Entonces borro la cola
			self.tail = self.tail.getPrev()	#Sino seteo la cola como el anterior a la cola
			self.tail.setSig(None)		#El siguiente sera nulo (Eliminando el ultimo)
		
		aux = self.head
		if (aux is None):		#Pregunto si el auxiliar es nulo, por ende la cabeza es nula, la lista esta vacia
			self.head=self.tail=pageNode		#seteo la cabeza y la cola
			#self.setCurrSize(1)		#La cantidad de nodos en lista es 1
		elif (pageNode.getScore() >= aux.getScore()):	#Si el auxiliar no es nulo, hay elementos.
			#Pregunto si es mayor el score nuevo a la cabeza, pasa a ser la nueva la cabeza	
			pageNode.setSig(self.head)	#El siguiente del nuevo, es la vieja cabeza
			self.head.setPrev(pageNode)	#El anterior a la vieja cabeza es el nuevo nodo
			self.head = pageNode		#La nueva cabeza es el nuevo nodo
		elif (self.currSize == 2):	#Si la cabeza es mayor, pregunto si hay un solo elemento, si lo hay 
			#El nuevo nodo pasa a ser la nueva cola
			self.head.setSig(pageNode)
			pageNode.setPrev(self.head)
			self.tail = pageNode
			self.tail.setSig(None)
		else:	#Sino comienzo a buscar donde insertar el nodo
			try:
				ant = aux
				while (pageNode.getScore() <= aux.getScore()) or (aux is None):
					#El ciclo corta cuando se encuentra un score mayor al ingresado ó cuando se llega al final
					ant = aux
					aux = aux.getSig()	#Pido otro
			except:
				pass
			if (aux is not None):
				#Si el auxiliar no es nulo
				pageNode.setPrev(ant)	#El auxiliar pasa a ser el siguiente del ingresante
				pageNode.setSig(ant.getSig())	#El anterior del auxiliar pasa a ser el anterior del ingresante
				ant.getSig().setPrev(pageNode)	#El ingresante pasa a ser el siguiente del anterior del auxiliar
				ant.setSig(pageNode)	#El ingresante pasa a ser el anterior del auxiliar
			else:
				#Si el auxiliar es nulo, quiere decir que era la cola
				pageNode.setPrev(self.tail)	#El anterior del ingresante es la cola
				self.tail.setSig(pageNode)	#El siguiente a la vieja cola es el ingresante
				self.tail = pageNode	#La nueva cola es el ingresante
			
		return pageNode	#Devuelvo	
		
		
	def update(self, query, score):
		pageNode = query		#Nodo a ingresar
		score = float("{0:.4f}".format(score))
		#scoreAnt = pageNode.getScore()
		if pageNode.getQuery() == self.head.getQuery():
			#Si el nodo a actualizar es la cabeza entonces el siguiente pasa ser la cabeza
#			print "Es la cabeza"
			sig = self.head.getSig()		#Obtengo el siguiente
			sig.setPrev(None)
			self.head = sig
			ant = sig = self.head
			#self.currSize -= 1
			#p = self.addPage(pageNode.getQuery(), score)
			#return p
		elif pageNode.getQuery() == self.tail.getQuery():
			#Si no es la cabeza, pero es la cola entonces el anterior pasa a ser a la nueva cola
#			print "Es la cola"
			ant = self.tail.getPrev()
			ant.setSig(None)
			self.tail = ant
			ant = sig = self.tail
			#self.currSize -= 1
			#p = self.addPage(pageNode.getQuery(), score)
			#return p
		else:
			#Si no es ni la cola ni la cabeza entonces esta en el medio
#			print "Mediooo"
			ant = pageNode.getPrev()	#obtengo el anterior
			sig = pageNode.getSig()		#Obtengo el siguiente
			ant.setSig(sig)
			sig.setPrev(ant)
			
		###################
		#Aca hago una especie de corte para saber de donde arrancar para disminuir tiempo
		###################	
		
		if pageNode.getScore() >= score:
			#Como el score nuevo es menor al viejo, comienzo a recorer desde ese punto hacia adelante
#			print "El score nuevo es menor al viejo"
			pageNode.setScore(score)
			aux2 = aux = ant
			try:
				while (pageNode.getScore()) <= aux.getScore() or (aux is None):
					#El ciclo corta cuando se encuentra un score mayor al ingresado ó cuando se llega al final
					aux2 = aux
					aux = aux.getSig()	#Pido otro
			except:
				pass
				
			if aux2.getQuery() == self.head.getQuery():
				#Pregunto si el auxiliar es la cabeza
				pageNode.setSig(self.head)
				pageNode.setPrev(None)
				self.head.setPrev(pageNode)
				self.head = pageNode
			elif aux2.getQuery() == self.tail.getQuery():
				#Es la cola
				pageNode.setSig(self.tail)
				pageNode.setPrev(self.tail.getPrev())
				self.tail.getPrev().setSig(pageNode)
				self.tail.setPrev(pageNode)
			else:
				#Si no es la cabeza
				if (aux is not None):
					pageNode.setPrev(aux2)	#El auxiliar pasa a ser el siguiente del ingresante
					pageNode.setSig(aux2.getSig())	#El anterior del auxiliar pasa a ser el anterior del ingresante
					aux2.getSig().setPrev(pageNode)	#El ingresante pasa a ser el siguiente del anterior del auxiliar
					aux2.setSig(pageNode)	#El ingresante pasa a ser el anterior del auxiliar
				else:
					#Si el auxiliar es nulo, quiere decir que era la cola
					pageNode.setPrev(self.tail)	#El anterior del ingresante es la cola
					self.tail.setSig(pageNode)	#El siguiente a la vieja cola es el ingresante
					self.tail = pageNode	#La nueva cola es el ingresante
		else:
			#Como el score nuevo es mayor al viejo, comienzo a reccorer desde ese punto hacia atras
#			print "El score nuevo es mayor al viejo"
			pageNode.setScore(score)	#Actualizo el nodo con el nuevo score
			aux2 = aux = sig	#Cargo los auxiliares con el siguiente para recorrer hacia atrás
			try:
				while (float(pageNode.getScore()) >= float(aux.getScore())) or (aux is None):
					#El ciclo corta cuando se encuentra un score mayor al ingresado ó cuando se llega al final						
					aux2 = aux
					aux = aux.getPrev()	#Pido otro
			except:
				pass
	
			if aux2.getQuery() == self.tail.getQuery():
				#Pregunto si justo el aux es la cola
				pageNode.setPrev(self.tail)	#El auxiliar pasa a ser el siguiente del ingresante
				pageNode.setSig(None)	#El anterior del auxiliar pasa a ser el anterior del ingresante
				self.tail.setSig(pageNode)
				self.tail = pageNode
				
			elif aux2.getQuery() == self.head.getQuery():
				pageNode.setPrev(self.head)
				pageNode.setSig(self.head.getSig())
				self.head.getSig().setPrev(pageNode)
				self.head.setSig(pageNode)
			else:
				#Si no es la cola
					
				if (aux is not None):
					#Si el auxiliar no es nulo
					pageNode.setPrev(aux2)	#El auxiliar pasa a ser el siguiente del ingresante
					pageNode.setSig(aux2.getSig())	#El anterior del auxiliar pasa a ser el anterior del ingresante
					aux2.getSig().setPrev(pageNode)	#El ingresante pasa a ser el siguiente del anterior del auxiliar
					aux2.setSig(pageNode)	#El ingresante pasa a ser el anterior del auxiliar
				else:
					#Si el auxiliar es nulo, quiere decir que es la cabeza
					pageNode.setSig(self.head)	#El anterior del ingresante es la cola
					self.head.setPrev(pageNode)	#El siguiente a la vieja cola es el ingresante
					self.head = pageNode	#La nueva cola es el ingresante
			
		return pageNode	#Devuelvo	

class GDSCache ():
	
	def __init__(self, size):
		self.cache_size = size
		self.pageList = DobleLista(size)
		self.cacheDict = {}
		self.L = 0
		self.hits = 0
		self.miss = 0
		self.corrects = 0
		self.cacheCost = self.cargarCostoRAM()
	
	def cargarCostoRAM(self):
		p = parametros.Parameters()
		path = p.getPathCosts()
		costos = {}
		try:
			archivo = open (path, "r")
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
		
	def getCostoDisk(self, query):
		costo = 0
		band = True
		palabras = query.split(" ")
		for pal in palabras:
			try:
				costo += float(self.costos[pal])
			except:
				return 0
		return costo
	
		
	def accessCache(self, query, hitBand):
		query = query.strip()
		tf = 0
		try:
			costo = self.cacheCost[query]	#Si el costo existe se lo asigno
		except:
			costo = 0	#Si no existe le pongo 0

		if float(costo) != 0:
		#Si el costo no es cero
			self.corrects += 1
			pageNode = Nodo(None)
			if (self.cacheDict.has_key(query)):
				if hitBand:
					self.hits += 1
				#Si la query esta en la caché, es decir hay un HIT actualizo el score y la ubicación en la cola		
				score = float(self.L) + (float(costo) / 1)	#Calculo el score
				#Actualizo con el nuevo score
				self.cacheDict[query] = self.pageList.update(self.cacheDict[query], score)
			else:
				#Si el elemento no esta en el caché, lo agrego
				if hitBand:
						self.miss += 1
				tf = costo
				if (self.pageList.getCurrSize() == self.pageList.getSize()):
					#Si el caché esta lleno
					self.L = self.pageList.getTail().getScore()	#Obtengo el menor score
					#Si el cache esta lleno, borro el menor
					del self.cacheDict[self.pageList.getTail().getQuery()]	#Eliminio del cache el valor de la cola
				#Agrego a la lista enlazada la query con el score solamente
				score = float(self.L) + float(costo) / 1	#Calculo el score
				pageNode = self.pageList.insert(query, score)	#Agrego a la lista la pagina
				self.cacheDict[query] = pageNode

		return tf
	
	def getTotalHit(self):
		total = float(self.hits) / (float(self.hits) + float(self.miss))
		return total
		
	def getTotalCorrects(self):
		return self.corrects
