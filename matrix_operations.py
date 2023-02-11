import numpy

def add_matrix_by_vector(matrix_, vector_):
	'''
	Matrices are not usually added to vectors.
	what we are looking for is "broadcasting"
	which is where the vector is broadcast the 
	larger array to that we actually have a
	compatible shape to add together.

	ex. 3x3 matrix and a 3x1 vector
	transforms the 3x1 vector into a 3x3 matrix
	'''
	assert vector_.ndim == 1
	assert matrix_.ndim > 1

	return matrix_ + vector_

def add_matrices(matrix_1, matrix_2):
	assert numpy.shape(matrix_1) == numpy.shape(matrix_2)

	return matrix_1 + matrix_2

def add_vectors(vector_1, vector_2):
	assert vector_1.ndim == 1 and vector_2.ndim == 1
	assert numpy.shape(vector_1) == vector_2.shape(vector_2)
	
	return vector_1 + vector_2

def multiply_matrixes(matrix_1, matrix_2):
	assert matrix_1.ndim > 1 and matrix_2.ndim > 1
	
	matrix_1_row, matrix_1_col = numpy.shape(matrix_1)
	matrix_2_row, matrix_2_col = numpy.shape(matrix_2)

	assert matrix_1_col == matrix_2_row
	
	return numpy.matmul(matrix_1, matrix_2)
	

def multiply_matrix_by_vector(matrix_, vector_):
	assert matrix_.ndim > 1 and vector_.ndim == 1
	
	vector_row, vector_col = numpy.shape(vector_)
	matrix_row, matrix_col = numpy.shape(matrix_)

	assert matrix_col == vector_row
	
	return numpy.matmul(matrix_, vector_)		
	