from plane import *
import sys

class Tilemap(list):

	def __init__(self, matrix):

		self.width = len(matrix[1])
		self.height = len(matrix)
		self.matrix = matrix

		for i in range(self.height):
			for j in range(self.width):
				self.append( Tile(i, j, matrix[i][j]) )

	def get_tile(self, x, y):
		try:
			return self[ (x * (self.height -1)) + y]
		except IndexError:
			print "IndexError: ", x, y

	def print_map_log(self):
		j = 0
		for i in range(len(self)):
			if j != self[i].x:
				print
				j = self[i].x
			print self[i], 
		print
		
	def print_solution_map(self, solution):

		matrix_solution = map(list, self.matrix)

		print "Caminho solucao: \n"

		for i in solution:
			matrix_solution[i.x][i.y] = '>'

		for line in matrix_solution:
			for tile in line:
				print tile,
			print

	# Funcao para achar a posicao final no Maze representado por 'F'

	def find_end(self):
		for i in range(len(self)):
			if self[i].type_char == "F":
				return self[i]
		return None

	# Funcao para achar a posicao inicial no Maze representado por 'I'

	def find_start(self):
		for i in range(len(self)):
			if self[i].type_char == "I":
				return self[i]
		return None


class Tile(object):

	def __init__(self, x, y, type_char):

		self.x = x
		self.y = y
		self.type_char = type_char
		self.parent = None
		self.g = 0
		self.h = 0
		self.f = 0

	def __repr__(self):
		return str((self.x, self.y))

	def __str__(self):
		return str(self.type_char)

	def get_cost(self):

		costs = { "I" : 999,
				  "F" : 0,
				  "M" : 200,
				  "." : 1,
				  "R" : 5,
				  "C" : 50}
		cost  = costs[self.type_char] 
		return cost

	def get_battle_time(self, base_num, planes):

		print "num avioes: ",len(planes)
		print "BATTLE!", base_num
		
		# return 3
		for plane in planes: 
			plane.energy -= 1

		base_cost = [60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120]
		power_sum = sum([ plane.power for plane in planes ])
		print base_num
		return float(base_cost[base_num] / power_sum)
		