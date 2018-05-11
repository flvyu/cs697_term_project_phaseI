from collections import Counter

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import theano
import theano.tensor as T

import network3
from network3 import sigmoid, tanh, ReLU, LReLU, ELU, Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer

import crater_loader

IMAGE_SIZE = 28

EPOCHS = 10
MB_SIZE = 1
ETA = .03
RUNS = 1


#training_data, validation_data, test_data = network3.load_data_shared()

# PHASE II -- Crater Data
training_data, validation_data, test_data = \
   crater_loader.load_crater_data_phaseII_wrapper("non_rotated_28x28.pkl", 28)

def leakyrelu():
    for lmbda in [0.0, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]:
        for j in range(RUNS):
            print "num %s, leaky relu, with regularization %s" % (j, lmbda)
            net = Network([
                ConvPoolLayer(image_shape=(MB_SIZE, 1, IMAGE_SIZE, IMAGE_SIZE),
                              filter_shape=(10, 1, 5, 5),
                              poolsize=(2, 2),
                              activation_fn=LReLU),
                ConvPoolLayer(image_shape=(MB_SIZE, 10, 12, 12),
                              filter_shape=(20, 10, 3, 3),
                              poolsize=(2, 2),
                              activation_fn=LReLU),
                FullyConnectedLayer(n_in=20*5*5, n_out=200, activation_fn=LReLU),
                FullyConnectedLayer(n_in=200, n_out=200, activation_fn=LReLU),
                FullyConnectedLayer(n_in=200, n_out=100, activation_fn=LReLU),
                SoftmaxLayer(n_in=100, n_out=2)], MB_SIZE)
            net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=lmbda)

def elu():
    for lmbda in [0.0, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1.0]:
        for j in range(RUNS):
            print "num %s, leaky relu, with regularization %s" % (j, lmbda)
            net = Network([
                ConvPoolLayer(image_shape=(MB_SIZE, 1, IMAGE_SIZE, IMAGE_SIZE),
                              filter_shape=(10, 1, 5, 5),
                              poolsize=(2, 2),
                              activation_fn=ELU),
                ConvPoolLayer(image_shape=(MB_SIZE, 10, 12, 12),
                              filter_shape=(20, 10, 3, 3),
                              poolsize=(2, 2),
                              activation_fn=ELU),
                FullyConnectedLayer(n_in=20*5*5, n_out=200, activation_fn=ELU),
                FullyConnectedLayer(n_in=200, n_out=200, activation_fn=ELU),
                FullyConnectedLayer(n_in=200, n_out=100, activation_fn=ELU),
                SoftmaxLayer(n_in=100, n_out=2)], MB_SIZE)
            net.SGD(training_data, EPOCHS, MB_SIZE, ETA, validation_data, test_data, lmbda=lmbda)

def run_experiments():
    #leakyrelu()
    elu()