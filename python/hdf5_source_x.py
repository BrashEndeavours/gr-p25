#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
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

import logging
import uuid
import h5py
from gnuradio import gr
import numpy as np

class _hdf5_source_x(gr.sync_block):
    """
    docstring for block _hdf5_source_x
    """
    def __init__(self,
                 num_outputs,
                 dataset_name,
                 data_filename,
		         log_level, 
 		         log_filename,
                 name,
                 dtype):
        self.num_outputs = num_outputs
        self.dataset_name = dataset_name
        self.data_filename = data_filename
        self.log_level = log_level
        self.log_filename = log_filename
        self.name = name
        self.dtype=dtype
        self.current_pos = 0
        
        gr.sync_block.__init__(self,
                               self.name,
                               in_sig=[],
                               out_sig=[self.dtype for n in range(num_outputs)])

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

        self.init_file_import()

        self.logger.info("HDF5 Sink initialized, filename: {}".format(self.data_filename))

    def work(self, input_items, output_items):
        min_stream_length = 0

        # Test if out  of samples
        if self.current_pos == self.dataset.shape[0]:
            return -1

        # Otherwise, calculate min samples requested of all streams
        for n in range(self.num_outputs):
            if len(output_items[n]) > min_stream_length:
                min_stream_length = len(output_items[n])

        # Test if requested streams exceeds capability
        if min_stream_length + self.current_pos > self.dataset.shape[0]:
            min_stream_length = self.dataset.shape[0] - self.current_pos

        self.logger.debug("Dataset shape: {}".format(self.dataset.shape))
        
         # Test if requested streams exceeds capability
        if min_stream_length + self.current_pos > self.dataset.shape[0]:
            min_stream_length = self.dataset.shape[0] - self.current_pos
        
        for n in range(self.num_outputs):
            array = self.dataset[self.current_pos:self.current_pos + min_stream_length,n]
            self.logger.debug("Stream: {}, shape: {}, total shipped: {}".format(n,
                                                array.shape,
                                                self.current_pos + min_stream_length))
            output_items[n][:min_stream_length] = array
            
        self.current_pos += min_stream_length

        return min_stream_length

    def init_file_import(self):
        try:
            self.datafile = h5py.File(self.data_filename, "r")
        except:
            pass
        self.datafile = h5py.File(self.data_filename, "r")
        self.dataset = self.datafile[self.dataset_name]
        return

    def close_file_import(self):
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


class hdf5_source_b(_hdf5_source_x):
    """
    docstring for block hdf5_source_b
    """
    def __init__(self, num_outputs, dataset_name, data_filename, log_level, log_filename):
        super(hdf5_source_b, self).__init__(num_outputs, 
                                          dataset_name, 
                                          data_filename, 
                                          log_level, 
                                          log_filename,
                                          name="hdf5_source_b",
                                          dtype=np.int8)

class hdf5_source_s(_hdf5_source_x):
    """
    docstring for block hdf5_source_s
    """
    def __init__(self, num_outputs, dataset_name, data_filename, log_level, log_filename):
        super(hdf5_source_s, self).__init__(num_outputs, 
                                          dataset_name, 
                                          data_filename, 
                                          log_level, 
                                          log_filename,
                                          name="hdf5_source_s",
                                          dtype=np.int16)

class hdf5_source_i(_hdf5_source_x):
    """
    docstring for block hdf5_source_i
    """
    def __init__(self, num_outputs, dataset_name, data_filename, log_level, log_filename):
        super(hdf5_source_i, self).__init__(num_outputs, 
                                          dataset_name, 
                                          data_filename, 
                                          log_level, 
                                          log_filename,
                                          name="hdf5_source_i",
                                          dtype=np.int32)
class hdf5_source_f(_hdf5_source_x):
    """
    docstring for block hdf5_source_f
    """
    def __init__(self, num_outputs, dataset_name, data_filename, log_level, log_filename):
        super(hdf5_source_f, self).__init__(num_outputs, 
                                          dataset_name, 
                                          data_filename, 
                                          log_level, 
                                          log_filename,
                                          name="hdf5_source_f",
                                          dtype=np.float32)