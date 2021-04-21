#! /usr/bin/env python
# encoding: UTF-8
from argparse import ArgumentParser
import ConfigParser
import os 

class Parametros:
	#Variable global utilizada para parsear los parametros
	global arg
	
	""" -*- """
	def __init__(self):
		"""Constructor de la clase."""
		
		# Descripción de lo que hace el ejercicio
		parser = ArgumentParser(description='%(prog)s es un script que permite implementar la tecnica GDS de reemplazos en cache')

		parser.add_argument("size", type=int, help="Tamaño del cache")
		
		parser.add_argument("queryWarm", type=int, help="Cantidad de queries de calentamiento (warm-up)")
		
		parser.add_argument("queryTest", type=int, help="Cantidad de queries de testeo")
				
		# Por último parsear los argumentos
		self.arg = parser.parse_args()
		
	def getSize(self):
		return self.arg.size
		
	def getQuery_warm(self):
		return self.arg.queryWarm
	
	def getQuery_test(self):
		return self.arg.queryTest
		
class Parameters:

	def __init__(self):
		config = ConfigParser.ConfigParser()
		path = os.path.dirname(os.path.realpath(__file__))
		config.read(path + "/conf/properties.ini")
		self.pathQuery = config.get('PATH', 'QUERY')
		self.pathCosts = config.get('PATH', 'COSTS')

	def getPathQuery(self):
		return self.pathQuery
		
	def getPathCosts(self):
		return self.pathCosts
	
	
		
