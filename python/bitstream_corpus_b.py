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

from itertools import product
import logging
import numpy as np
import uuid
from gnuradio import gr

class bitstream_corpus_b(gr.sync_block):
    """
    docstring for block bitstream_corpus_b
    """
    def __init__(self,
                 min_value,
                 max_value,
                 value_range,
                 seq_length,
                 repeat,
                 shuffle,
                 log_level,
                 filename,
                 flush_bytes):
        self.min_value = min_value
        self.max_value = max_value
        self.value_range = value_range
        self.seq_length = seq_length
        self.repeat = repeat
        self.shuffle = shuffle
        self.log_level = log_level
        self.filename = filename
        self.flush_bytes = flush_bytes
        gr.sync_block.__init__(self,
                               name="bitstream_corpus_b",
                               in_sig=None,
                               out_sig=[np.uint8])

        self.loggername = uuid.uuid4().hex
        self.logger = logging.getLogger(self.loggername)

        self.formatter = logging.Formatter('%(asctime)s | %(levelname)s | {} | %(message)s'.format(__name__))

        self.console = logging.StreamHandler()
        self.console.setLevel(self.log_level)
        self.console.setFormatter(self.formatter)
        self.logger.addHandler(self.console)

        if self.filename:
            self.fhandler = logging.FileHandler(self.filename)
            self.fhandler.setLevel(self.log_level)
            self.fhandler.setFormatter(self.formatter)
            self.logger.addHandler(self.fhandler)

        self.logger.setLevel(self.log_level)
        if log_level == logging.NOTSET:
            self.logger.disabled = True
            
        self.index = 0
        self.array_size = 0

        self.logger.info("Bitstream Corpus: Min={}, Max={}, Value Range={},Sequence Length={}".format(
                                self.min_value,
                                self.max_value,
                                self.value_range,
                                self.seq_length))
        self.generate_array()

    def work(self, input_items, output_items):

        nOutput = len(output_items[0])

        self.logger.info("Number of output items requested: {}".format(nOutput))
        self.logger.info("Beginning Index: {}, Array Size: {}".format(self.index, self.array_size))
        if self.index == self.array_size:
            self.logger.info("Repeat?: {}".format(self.repeat))
            if self.repeat:
                self.logger.info("Number of output items processed: {}".format(0))
                self.logger.info("Ending Index: {}, Array Size: {}".format(self.index, self.array_size))
                self.generate_array()
                self.index = 0
            else:
                if self.flush_bytes == 0:
                    return -1

                if nOutput <= self.flush_bytes:
                    self.logger.info("Processed {} flush bytes".format(nOutput))
                    x = (0,) * nOutput
                    self.flush_bytes -= nOutput
                    n_processed = len(x)
                    output_items[0][:n_processed] = x
                    return n_processed

                else:
                    self.logger.info("Processed {} flush bytes".format(self.flush_bytes))
                    x = (0,) * self.flush_bytes
                    self.flush_bytes = 0
                    n_processed = len(x)
                    output_items[0][:n_processed] = x
                    return n_processed


        if (self.array_size - self.index) >= nOutput:
            x = self.array[self.index:(self.index+nOutput)]
            self.index = self.index+nOutput
        else:
            x = self.array[self.index:]
            self.index = self.array_size

        n_processed = len(x)

        self.logger.info("Number of output items processed: {}".format(n_processed))
        self.logger.info("Ending Index: {}, Array Size: {}".format(self.index, self.array_size))

        output_items[0][:n_processed] = x
        return n_processed

    def generate_array(self):
        if not self.value_range:
            temp_range = range(self.min_value, self.max_value + 1)
        else:
            temp_range = self.value_range
        temp_array = [p for p in product(temp_range, repeat=self.seq_length)]
        if self.shuffle:
            np.random.shuffle(temp_array)
        self.array = np.asarray(temp_array, dtype=np.uint8).flatten()
        self.array_size = len(self.array)

    def set_min_value(self, min_value):
        self.min_value = min_value

    def set_max_value(self, max_value):
        self.max_value = max_value

    def set_value_range(self, value_range):
        self.value_range = value_range

    def set_seq_length(self, seq_length):
        self.seq_length = seq_length