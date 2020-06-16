from proton.matrices.matrix import *
from proton.errors.errors import *
import copy
class elementary():
	'''
	elemntary class hanndles elementry operarions on a matrix obj.
	'''
	def __init__(self,matr):
		if(type(matr)==list):
			matr = matrix(matr)
		if(type(matr) != matrix):
			raise OnlyMatrixAllowed(matr)
		self.__matlist = copy.deepcopy(matr.pull())
		self.__numrow = matr.getRowCount()
		self.__numcol = matr.getRowCount()
	
	def __getitem__(self,index = ""):
		index = index.capitalize()
		if(index[0] == 'C'):
			return self.__pullcol(int(index[1:len(index)]))
		if(index[0]=='R'):
			return self.__pullrow(int(index[1:len(index)]))
		else:
			raise OrderMismatch("Can only return column or a row.")

	def __setitem__(self,index="",value=[]):
		index = index.capitalize()
		if(index[0] == "C"):
			self.__pushcol(int(index[1:len(index)]),value)
		if(index[0]=='R'):
			self.__pushrow(int(index[1:len(index)]),value)
		else:
			raise OrderMismatch(f"Invalid {index} for {self}")


	def __pullrow(self,index):
		if(index>=self.__numrow or index <0):
			raise IndexError(f"Cannot find {index} in {self}.")
		return copy.deepcopy(self.__matlist[index])
	
	def __pullcol(self,index):
		if(index>=self.__numcol or index <0):
			raise IndexError(f"Cannot find {index} in {self}.")
		m = [0 for k in range(self.__numcol)]
		for i in range(self.__numrow):
			m[i] = self.__matlist[i][index]
		return m
	
	def __pushcol(self,index,value=[]):
		if(index>=self.__numcol or index <0):
			raise IndexError(f"Cannot find column {index} in {self}.")
		if(len(value)!= self.__numrow):
			raise IndexError(f"The index of {value} does not match that of {self}")

		for i in range(self.__numrow):
			self.__matlist[i][index] = value[i]
	
	def __pushrow(self,index,value=[]):
		if(index>=self.__numrow or index <0):
			raise IndexError(f"Cannot find row of {index} in {self}.")
		if(len(value)!= self.__numcol):
			raise IndexError(f"The index of {value} does not match that of {self}")
		self.__matlist[index] = copy.deepcopy(value)