import numpy

def add_matrix_to_vector(matrix_, vector_):
	'''
	Matrices generally cannot be added to vectors.
	What we are actually looking for is "broadcasting"
	which is where the vector is broadcast the 
	larger array to that we actually have a
	compatible shape to add together.

	ex. 3x3 matrix and a 3x1 vector
	transforms the 3x1 vector into a 3x3 matrix
	'''
	assert vector_.ndim == 1
	assert matrix_.ndim == 2

	row_size, col_size = numpy.shape(matrix_)

	for row in row_size:
		for col in col_size:
			matrix_[row, col] += vector_[col]

	return matrix_ + vector_

def add_matrices(matrix_1, matrix_2):
	assert numpy.shape(matrix_1) == numpy.shape(matrix_2)

	return matrix_1 + matrix_2

def add_vectors(vector_1, vector_2):
	assert vector_1.ndim == 1 and vector_2.ndim == 1
	assert numpy.shape(vector_1) == vector_2.shape(vector_2)
	
	return vector_1 + vector_2

def multiply_matrixes(matrix_1, matrix_2):
	assert matrix_1.ndim == 2 and matrix_2.ndim == 2
	
	matrix_1_row, matrix_1_col = numpy.shape(matrix_1)
	matrix_2_row, matrix_2_col = numpy.shape(matrix_2)

	assert matrix_1_col == matrix_2_row
	
	return numpy.matmul(matrix_1, matrix_2)
	

def multiply_matrix_by_vector(matrix_, vector_):
	assert matrix_.ndim == 2 and vector_.ndim == 1
	
	vector_size = numpy.shape(vector_)[0]
	matrix_row, matrix_col = numpy.shape(matrix_)

	assert matrix_col == vector_size
	
	return numpy.matmul(matrix_, vector_)		
	
def vector_dot_product(vector_1, vector_2):
	assert vector_1.ndim == 1 and vector_2.ndim == 1

	vector_1_size = numpy.shape(vector_1)[0]
	vector_2_size = numpy.shape(vector_2)[0]

	assert vector_1_size == vector_2_size

	dot_product_result = 0
	for element in range(vector_1_size):
		dot_product_result += vector_1[element] * vector_2[element]
	
	return dot_product_result

def matrix_and_vector_dot_product(matrix_, vector_):
	assert matrix_.ndim == 2 and vector_.ndim == 1
	
	vector_size = numpy.shape(vector_)[0]
	matrix_row, matrix_col = numpy.shape(matrix_)

	assert matrix_col == vector_size


	

