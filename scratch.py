import numpy
import tensorflow as tf
from matplotlib import pyplot as plt
from matrix_operations import *


def sigmoid_activation_layer():
    pass
def relu_activate_layer():
    pass

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
	plt.show()

if __name__ == '__main__':
	main()