#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (C) 2017 SLt Blake Mackey
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

from gnuradio import gr, digital
import logging
import uuid
from p25_utils import _def_dibit_map
from p25_utils import _def_verbose
from p25_utils import _def_log

class dibit_mapper_bf(gr.hier_block2):
    """
	Hierarchical block for creating P25 Dibit -> Symbol Mapping.

	The input is a dibit (two bit) stream (char, not packed) and the
	output is the float (P25 symbol) mapping.

	@param dibit_map: output sample rate
	@type dibit_map: float array
    @param verbose: Print console information?
    @type verbose: bool
    @param log: Log debugging data to console/files?
    @type log: bool
	"""
    def __init__(self,
                 dibit_map,
                 log_level,
                 filename):
        self.dibit_map = dibit_map
        self.log_level = log_level
        self.filename = filename
        gr.hier_block2.__init__(self,
                "dibit_mapper_bf",
                gr.io_signature(1, 1, gr.sizeof_char),  # Input signature
                gr.io_signature(1, 1, gr.sizeof_float)) # Output signature

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

        self.logger.debug("Dibit mapping: {}".format(self.dibit_map))

	    # Convert dibits to symbol map [00, 01, 10, 11] -> [1, 3, -1, -3].
        self.dibits_to_symbols = digital.chunks_to_symbols_bf(dibit_map)

        # Define blocks and connect them
        self.connect(self, self.dibits_to_symbols, self)