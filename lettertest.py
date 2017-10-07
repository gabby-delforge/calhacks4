import converter
import numpy

training_data = converter.convert("MNISTfiles/test_images", "MNISTfiles/test_labels")

class Network(object):
	""" Sizes is an array whose length equals the number of layers in the NN, 
	and whose values represent the number of nodes in each layer. 
	Biases and weights are initialized randomly to start with. """
	def __init__(self, sizes):

	""" Given an input a, feeds the input through each layer to get an output. """
	def get_output(self, a):

	"""Uses stochastic gradient descent to minimize loss. 
		rate = learning rate
		epochs = number of times to run through training
		mini_batch_size = size of mini_batch to use to update weights - can be resource-heavy
		test_data = used for tracking progress, resource-heavy. """
	def learn(self, rate, epochs, mini_batch_size, test_data = None):

	"""Uses the training data in MINI_BATCH to update the network's weights and biases. """
	def update_mini_batch(self, mini_batch, rate):


def sigmoid(z):
	return 1.0/(1.0 + np.exp(-z))

"""Derivative of the sigmoid function. """
def sigmoid_prime(z):







