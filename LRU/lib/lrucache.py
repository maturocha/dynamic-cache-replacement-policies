class Nodo ():

	def __init__(self, data):
		self.valor = data
		self.nodoPrev = None
		self.nodoSig = None

 	def getValue(self):
		return self.valor

	def setValor (self, data):
		self.valor = data

	def getPrev(self):
		return self.nodoPrev

	def setPrev(self, nodo):
		self.nodoPrev = nodo

	def getSig(self):
		return self.nodoSig

	def setSig(self, nodo):
		self.nodoSig = nodo


 	def toString(self):
		return str(self.valor)
     

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

	def printList (self): #Imprime toda la cola
		string = ""
		if (self.head == None): #Si es nulo la cabeza devuelvo
			return
		else: #sino
			aux = self.head	#El nodo cabeza lo pongo en auxiliar y comienzo a recorrer
			while aux.getSig() != None:	#Si el valor no es nulo
				string += aux.toString() + ","	#imprimo
				aux = aux.getSig()	#Obtengo el siguiente
			string += aux.toString()	#imprimo
		return string
			
	def addPage(self, pageNumber):
	#Agrega un nodo a la lista
		pageNode = Nodo(pageNumber)		#Nodo a ingresar
		if (self.head == None):		#Pregunto si la cabeza es nula, la lista esta vacia
			self.head = pageNode		#seteo la cabeza
			self.tail = pageNode		#Y por ende la cola tmabien
			self.setCurrSize(1)		#La cantidad de nodos en lista es 1
			return pageNode
		elif (self.currSize < self.size):	#Si el tamanio es menor al tope
			self.currSize += 1		#Incremento el tamanio actual
		else:
			self.tail = self.tail.getPrev()	#Sino seteo la cola como el anterior a la cola
			self.tail.setSig(None)		#El siguiente sera nulo (Eliminando el ultimo)
		pageNode.setSig(self.head)			#Seteo la excabeza de la cola como el siguiente del nodo ingresante
		self.head.setPrev(pageNode)			#Seteo al nodo ingresante como el previo de la excabeza
		self.head = pageNode				#Seteo al nodo ingresante como la nueva cabeza
		return pageNode
			
		
	def movePageToHead(self, pageNode):
	#Mueve una pagina al comienzo de la lista
		if (pageNode == None) or (pageNode == self.head):	
		#Si la pagina no es nula o es la misma cabeza devuelvo
			return
		
		if (pageNode == self.tail):
		#Si la pagina es la cola
			self.tail = self.tail.getPrev()	#Seteo la cola como el anterior
			self.tail.setSig(None)		#Y el siguiente es nulo
		
		nodePrev = pageNode.getPrev()	#Obtengo el nodo previo en un auxiliar nodeS
		nodeSig = pageNode.getSig()		#Obtengo el nodo siguiente en un auxiliar nodeP
         	nodePrev.setSig(nodeSig)		#Seteo el nodo siguiente al nodo previo como el auxiliar siguiente
         	if nodeSig != None:			#Enlazo el nodo sig y el anterior
         		nodeSig.setPrev(nodePrev)
         	pageNode.setPrev(None)		#Seteo al anterior como nulo (es la nueva cabeza!)
         	pageNode.setSig(self.head)		#Seteo la cabeza como siguiente
         	self.head.setPrev(pageNode)		#Seteo el nuevo nodo como el anterior a la vieza cabeza
         	self.head = pageNode			#Y por ultimo, el nuevo nodo pasa a ser la nueva cabeza :)



class LRUCache ():
	
	def __init__(self, cache_s):
		self.cache_size = cache_s
		self.pageList = DobleLista(cache_s)
		self.pageMap = {}
		self.hit = 0
		self.total = 0
		
	def getTotalHit(self):
		total = float(self.hit) / float(self.total)
		return total
		
	def accessPage(self, pageNumber, hit):
	#Metodo que registra un acceso a una pagina determinada
		if hit:
			self.total += 1
		pageNode = Nodo(None)
		if (pageNumber in self.pageMap):
			#Si la pagina esta en el cache
			if hit:
				self.hit += 1
			pageNode = self.pageMap[pageNumber]	#Muevo la pagina al comienzo segun LRU
			self.pageList.movePageToHead(pageNode)
		else:
			#si la pagina no esta en el cache, la agrego
			if (self.pageList.getCurrSize() == self.pageList.getSize()):
			#Si el cache esta lleno 
				del self.pageMap[self.pageList.getTail().getValue()]	#Eliminio del cache el valor de la cola
			pageNode = self.pageList.addPage(pageNumber)	#Agrego a la lista la pagina
			self.pageMap[pageNumber] = pageNode
		

	def printCacheState(self):
		print "Cache: { " + self.pageList.printList() + " }"
