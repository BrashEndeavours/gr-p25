#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 SLt Blake Mackey.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Input, Dense
from keras.datasets import mnist
from keras import backend as K
from keras.engine.topology import Layer
import tensorflow
import numpy as np

import numpy
from gnuradio import gr

class nn_demod_learning(gr.sync_block):
    """
    docstring for block nn_demod_learning
    """
    def __init__(self, nHistory):
        gr.sync_block.__init__(self,
            name="nn_demod_learning",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
                
        # create model
        self.model = Sequential()
        self.model.add(Dense(64, input_dim=1, activation='linear'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='linear'))
                    
        # Compile model
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        print (self.model.summary())

        self.model.train_on_batch(np.array([0]), np.array([0]))
        prediction = self.model.predict_on_batch(np.array([0]))

    def work(self, input_items, output_items):
        #print ("in:", input_items, len(input_items[0]))
        #print ("out:", output_items, len(output_items[0]))
        in0 = input_items[0]
        out = output_items[0]
        
        for idx in range(len(input_items[0])):
            #print ("Input Item: ", in0[idx], "Index: ", idx)

            metrics = self.model.train_on_batch(np.array([in0[idx]]), np.array([in0[idx]]))
            prediction = self.model.predict_on_batch(np.array([in0[idx]]))
            #print ("Target: ", in0[idx], "Predict:", prediction[0])
            out[idx] = prediction[0]
        output_items[0][:] = out
        return len(output_items[0])

