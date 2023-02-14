import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from matrix_operations import *


def main():
	#feedforward network
	rand_int2 = numpy.random.randint(0,5,(4,5)) # random numpy array of shape (4,5)
	(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

	assert x_train.shape == (60000, 28, 28)
	assert x_test.shape == (10000, 28, 28)
	assert y_train.shape == (60000,)
	assert y_test.shape == (10000,)

	# plot first few images
	for i in range(9):
		# define subplot
		plt.subplot(330 + 1 + i)
		# plot raw pixel data
		plt.imshow(x_train[i], cmap=plt.get_cmap('gray'))

	# show the figure
	#plt.show()

	a_1d = np.arange(4)
	a_2d = np.arange(12).reshape((3, 4))
	b_2d = (a_2d.copy() * 2)#.reshape((4,3))
	'''
	result = multiply_matrixes(a_2d, b_2d)
	print(a_2d)
	print(b_2d)
	print(result)
	'''
	print(a_1d)
	print(a_2d)
	result = vector_dot_product(a_1d, a_1d)
	
	print(result)

if __name__ == '__main__':
	main()