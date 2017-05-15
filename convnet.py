from __future__ import division, print_function, absolute_import

import h5py
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

h5f = h5py.File('/Desktop/Self-Driving-Car/PreparedData/dataset.h5','r')
X = h5f['X']
Y = h5f['Y']

network = input_data(shape=[None, 128, 128, 1], name='input')
network = conv_2d(network, 32, 3, activation='relu', regularizer='L2')
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = cinv_2d(network, 64, 3, activation='relu', regularizer='L2')
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = fully_connected(network, 128, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 256, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 10, activation='softmax')
network = regression(network, optimizer='adam', learning_rate=0.01, loss='categorical_crossentropy', name ='target')


model = tflearn.DNN(network, tensorboard_verbose=0)
model.fit({'input': X}, {'target': Y}, n_epoch=20, run_id='convnet_self_driving_car')

model.save('cnnsdc.model')
