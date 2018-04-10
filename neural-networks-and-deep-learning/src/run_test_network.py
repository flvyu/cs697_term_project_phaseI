"""
run_test_network.py
~~~~~~~~~~~~~~~~~~~~~~

Garrett trying to get network.py running on the digit dataset

Copied from mnist_average_darkness.py

"""

#### Libraries
# Standard library

# My libraries
import mnist_loader
from crater_network import Network

def main():

    # Load the data
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

    # training phase: compute the average darknesses for each digit,
    # based on the training data

    # Make the network
    print "Making Network...."
    netwk = Network([28*28,30,10])
    print "Training the Network...."
    netwk.SGD(training_data, epochs=5, mini_batch_size=100, eta=0.01)


    # testing phase: see how many of the test images are classified
    # correctly

    # Evaluate results
    eval = netwk.evaluate(validation_data)


    print eval


if __name__ == "__main__":
    main()
