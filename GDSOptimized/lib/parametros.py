#! /usr/bin/env python
# encoding: UTF-8
from argparse import ArgumentParser

class Parametros:
	#Variable global utilizada para parsear los parametros
	global arg
	
	""" -*- """
	def __init__(self):
		"""Constructor de la clase."""
		
		# Descripción de lo que hace el ejercicio
		parser = ArgumentParser(description='%(prog)s es un script que permite implementar la tecnica LRU de reemplazos en cache')

		parser.add_argument("fileP", type=str, help="Path completo del archivo de queries a levantar (ya limpio)")
		
		parser.add_argument("fileC", type=str, help="Path completo del archivo de costos de las queries")
		
		parser.add_argument("size", type=int, help="Tamaño del cache")
		
		parser.add_argument("queryWarm", type=int, help="Cantidad de queries de calentamiento (warm-up)")
		
		parser.add_argument("queryTest", type=int, help="Cantidad de queries de testeo")
		
		
		# Por último parsear los argumentos
		self.arg = parser.parse_args()
		
	def getFile(self):
		return self.arg.fileP
		
	def getFileC(self):
		return self.arg.fileC
		
	def getSize(self):
		return self.arg.size
		
	def getQuery_warm(self):
		return self.arg.queryWarm
	
	def getQuery_test(self):
		return self.arg.queryTest
		
	def getQuery_offset(self):
		return self.arg.queryOffset
	
	
		
