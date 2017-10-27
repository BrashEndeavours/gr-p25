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

class _hdf5_sink_x(gr.sync_block):
    """
    docstring for block _hdf5_sink_x
    """
    def __init__(self,
                 num_inputs,
                 dataset_name,
                 data_filename,
		         log_level, 
 		         log_filename,
                 name,
                 dtype):
        self.num_inputs = num_inputs
        self.dataset_name = dataset_name
        self.data_filename = data_filename
        self.log_level = log_level
        self.log_filename = log_filename
        self.name = name
        self.dtype=dtype
        
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

        self.init_file_export()

        self.logger.info("HDF5 Sink initialized, filename: {}".format(self.data_filename))

    def work(self, input_items, output_items):
        min_stream_length = 0

        for n in range(self.num_inputs):
            if len(input_items[n]) > min_stream_length:
                min_stream_length = len(input_items[n])

        array = np.asarray(input_items[:][:min_stream_length])
        array = array.transpose()

        self.process_file_export(min_stream_length=min_stream_length,
                                 array=array)

        return min_stream_length

    def init_file_export(self):
        try:
            os.remove(self.data_filename)
        except Exception:
            pass
        if self.data_filename == "":
            self.logger.error("Filename empty")
        else:
            self.datafile = h5py.File(self.data_filename, "w")
            self.dataset = self.datafile.create_dataset(self.dataset_name,
                                                        shape=(0, self.num_inputs),
                                                        maxshape=(None, self.num_inputs),
                                                        dtype=self.dtype,
                                                        data=self.array)
        return

    def process_file_export(self, min_stream_length, array):
        self.disk_array_len = self.dataset.shape[0]
        self.logger.debug("HDF5 Shape Before: {}".format(self.dataset.shape))
        self.logger.debug("Number of Samples to add {}".format(min_stream_length))
        
        self.dataset.resize((self.dataset.shape[0] + min_stream_length, self.num_inputs))
        
        self.dataset[self.disk_array_len:self.disk_array_len + min_stream_length] = array
        self.datafile.flush()

        self.logger.debug("HDF5 Shape After: {}".format(self.dataset.shape))
        return

    def close_file_export(self):
        try:
            self.datafile.close()
        except:
            pass

    def set_dataset_name(self, dataset_name):
        self.dataset_name = dataset_name
        return

    def get_dataset_name(self):
        return self.dataset_name
   
    def set_data_filename(self, data_filename):
        self.data_filename = data_filename
        return

    def get_data_filename(self):
        return self.data_filename


class hdf5_sink_b(_hdf5_sink_x):
    """
    docstring for block hdf5_sink_b
    """
    def __init__(self, num_inputs, dataset_name, data_filename, log_level, log_filename):
        super(hdf5_sink_b, self).__init__(num_inputs, 
                                          dataset_name, 
                                          data_filename, 
                                          log_level, 
                                          log_filename,
                                          name="hdf5_sink_b",
                                          dtype=np.int8)

class hdf5_sink_s(_hdf5_sink_x):
    """
    docstring for block hdf5_sink_s
    """
    def __init__(self, num_inputs, dataset_name, data_filename, log_level, log_filename):
        super(hdf5_sink_s, self).__init__(num_inputs, 
                                          dataset_name, 
                                          data_filename, 
                                          log_level, 
                                          log_filename,
                                          name="hdf5_sink_s",
                                          dtype=np.int16)

class hdf5_sink_i(_hdf5_sink_x):
    """
    docstring for block hdf5_sink_i
    """
    def __init__(self, num_inputs, dataset_name, data_filename, log_level, log_filename):
        super(hdf5_sink_i, self).__init__(num_inputs, 
                                          dataset_name, 
                                          data_filename, 
                                          log_level, 
                                          log_filename,
                                          name="hdf5_sink_i",
                                          dtype=np.int32)
class hdf5_sink_f(_hdf5_sink_x):
    """
    docstring for block hdf5_sink_f
    """
    def __init__(self, num_inputs, dataset_name, data_filename, log_level, log_filename):
        super(hdf5_sink_f, self).__init__(num_inputs, 
                                          dataset_name, 
                                          data_filename, 
                                          log_level, 
                                          log_filename,
                                          name="hdf5_sink_f",
                                          dtype=np.float32)