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

from gnuradio import gr
import numpy as np
import h5py
import logging
import os
import uuid

class _variable_sink_x(gr.sync_block):
    """
    docstring for block _variable_sink_x
    """
    def __init__(self,
                 num_inputs,
		         log_level, 
 		         log_filename,
                 name,
                 dtype):
        self.num_inputs = num_inputs
        self.log_level = log_level
        self.log_filename = log_filename
        self.name = name
        self.dtype = dtype
        gr.sync_block.__init__(self,
                               self.name,
                               in_sig=[self.dtype for n in range(num_inputs)],
                               out_sig=[])

        self.loggername = uuid.uuid4().hex

        self.logger = logging.getLogger(__name__)
        self.logger.propagate = False
        self.formatter = logging.Formatter('%(asctime)s | %(levelname)s | {} | %(message)s'.format(__name__))

        self.console = logging.StreamHandler()
        self.console.setLevel(self.log_level)
        self.console.setFormatter(self.formatter)
        self.logger.addHandler(self.console)

        if self.log_filename:
            self.fhandler = logging.FileHandler(self.log_filename)
            self.fhandler.setLevel(self.log_level)
            self.fhandler.setFormatter(self.formatter)
            self.logger.addHandler(self.fhandler)

        self.logger.setLevel(self.log_level)
        if log_level == logging.NOTSET:
            self.logger.disabled = True

        self.array = np.array(object=[],
                              dtype=self.dtype).reshape(0, self.num_inputs)

        self.init_mem_export()
        self.logger.info("Variable Sink Enabled")

    def work(self, input_items, output_items):
        min_stream_length = 0
        self.logger.debug("Variable Shape Before: {}".format(self.array.shape))

        for n in range(self.num_inputs):
            if len(input_items[n]) > min_stream_length:
                min_stream_length = len(input_items[n])

        self.logger.debug("Number of Samples to add {}".format(min_stream_length))

        array = np.asarray(input_items[:][:min_stream_length])
        array = array.transpose()

        self.process_mem_export(array=array)
        
        self.logger.debug("Variable Shape After: {}".format(self.array.shape))
        return min_stream_length

    def init_mem_export(self):
        self.array = np.array([]).reshape(0, self.num_inputs)
        return

    def process_mem_export(self, array):
        self.array = np.append(self.array, array, axis=0)
        return

    def get_data(self):
        return self.array

    def get_data_size(self):
        return self.array.shape

class variable_sink_b(_variable_sink_x):
    """
    docstring for block variable_sink_b
    """
    def __init__(self, num_inputs, log_level, log_filename):
        super(variable_sink_b, self).__init__(num_inputs, 
                                              log_level, 
                                              log_filename,
                                              name="variable_sink_b",
                                              dtype=np.int8)

class variable_sink_s(_variable_sink_x):
    """
    docstring for block variable_sink_s
    """
    def __init__(self, num_inputs, log_level, log_filename):
        super(variable_sink_b, self).__init__(num_inputs, 
                                              log_level, 
                                              log_filename,
                                              name="variable_sink_s",
                                              dtype=np.int16)

class variable_sink_i(_variable_sink_x):
    """
    docstring for block variable_sink_i
    """
    def __init__(self, num_inputs, log_level, log_filename):
        super(variable_sink_b, self).__init__(num_inputs, 
                                              log_level, 
                                              log_filename,
                                              name="variable_sink_i",
                                              dtype=np.int32)

class variable_sink_f(_variable_sink_x):
    """
    docstring for block variable_sink_f
    """
    def __init__(self, num_inputs, log_level, log_filename):
        super(variable_sink_b, self).__init__(num_inputs, 
                                              log_level, 
                                              log_filename,
                                              name="variable_sink_f",
                                              dtype=np.float32)