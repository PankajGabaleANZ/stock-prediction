'''trains a neural network model in TensorFlow'''
import sys
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import format_path

# pylint: disable=C0103,R0914,E1101,R0915

def run(train_data_path, test_data_path):
    '''prep data for training'''
    train_data = pd.read_csv(format_path(train_data_path), index_col='date')
    test_data = pd.read_csv(format_path(test_data_path), index_col='date')
    train(train_data, test_data)

def train(data_train, data_test):
    '''trains a neural network'''

    # Build X and y
    y_train = data_train[['adjusted']].transpose().values.flatten()
    data_train.drop(['adjusted'], axis=1)
    X_train = data_train.values

    y_test = data_train[['adjusted']].transpose().values.flatten()
    data_test.drop(['adjusted'], axis=1)
    X_test = data_test.values

    # number of training examples
    # n = data.shape[0]
    p = X_train.shape[1]

    # Placeholder, None means we don't yet know the number of observations flowing through
    X = tf.placeholder(dtype=tf.float32, shape=[None, p])
    Y = tf.placeholder(dtype=tf.float32, shape=[None])

    # Model architecture parameters
    n_neurons_1 = 128
    n_neurons_2 = 64
    n_neurons_3 = 32
    n_target = 1

    # Initializers
    sigma = 1
    weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale=sigma)
    bias_initializer = tf.zeros_initializer()

    # Layer 1: Variables for hidden weights and biases
    W_hidden_1 = tf.Variable(weight_initializer([p, n_neurons_1]))
    bias_hidden_1 = tf.Variable(bias_initializer([n_neurons_1]))
    # Layer 2: Variables for hidden weights and biases
    W_hidden_2 = tf.Variable(weight_initializer([n_neurons_1, n_neurons_2]))
    bias_hidden_2 = tf.Variable(bias_initializer([n_neurons_2]))
    # Layer 3: Variables for hidden weights and biases
    W_hidden_3 = tf.Variable(weight_initializer([n_neurons_2, n_neurons_3]))
    bias_hidden_3 = tf.Variable(bias_initializer([n_neurons_3]))

    # Output layer: Variables for output weights and biases
    W_out = tf.Variable(weight_initializer([n_neurons_3, n_target]))
    bias_out = tf.Variable(bias_initializer([n_target]))

    # Hidden layer
    hidden_1 = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), bias_hidden_1))
    hidden_2 = tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
    hidden_3 = tf.nn.relu(tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))

    # Output layer (must be transposed)
    out = tf.add(tf.matmul(hidden_3, W_out), bias_out)

    # Cost function
    mse = tf.reduce_mean(tf.squared_difference(out, Y))

    # Optimizer
    opt = tf.train.AdamOptimizer().minimize(mse)

    # Make Session
    net = tf.Session()

    # Run initializer
    net.run(tf.global_variables_initializer())

    # Setup plot
    # plt.ion()
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111)
    # line1, = ax1.plot(y_test)
    # line2, = ax1.plot(y_test * 0.5)
    # plt.show()

    # Fit neural net
    batch_size = 256
    mse_train = []
    mse_test = []

    # Run
    epochs = 10
    for e in range(epochs):

        # Shuffle training data
        shuffle_indices = np.random.permutation(np.arange(len(y_train)))
        X_train = X_train[shuffle_indices]
        y_train = y_train[shuffle_indices]

        # Minibatch training
        for i in range(0, len(y_train) // batch_size):
            start = i * batch_size
            batch_x = X_train[start:start + batch_size]
            batch_y = y_train[start:start + batch_size]
            # Run optimizer with batch
            net.run(opt, feed_dict={X: batch_x, Y: batch_y})

            # Show progress
            if np.mod(i, 50) == 0:
                # MSE train and test
                mse_train.append(net.run(mse, feed_dict={X: X_train, Y: y_train}))
                mse_test.append(net.run(mse, feed_dict={X: X_test, Y: y_test}))
                print('MSE Train: ', mse_train[-1])
                print('MSE Test: ', mse_test[-1])
                # Prediction
                pred = net.run(out, feed_dict={X: X_test})
                # line2.set_ydata(pred)
                # plt.title('Epoch ' + str(e) + ', Batch ' + str(i))
                # plt.pause(0.01)

    # Print final MSE after Training
    mse_final = net.run(mse, feed_dict={X: X_test, Y: y_test})
    print(mse_final)

if __name__ == '__main__':
    run(str(sys.argv[1]), str(sys.argv[2]))
