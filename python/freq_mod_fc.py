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

from gnuradio import gr, analog, filter
from math import pi
from p25_utils import _def_sample_rate
from p25_utils import _def_max_amplitude
from p25_utils import _def_max_deviation
from p25_utils import _def_sensitivity_adjust
from p25_utils import _def_verbose
from p25_utils import _def_log

class freq_mod_fc(gr.hier_block2):
    """
    docstring for block freq_mod_fc
    """
    def __init__(self,
            sample_rate=_def_sample_rate,
            max_amplitude=_def_max_amplitude,
            max_deviation=_def_max_deviation,
            sensitivity_adjust=_def_sensitivity_adjust,
            verbose=_def_verbose,
            log=_def_log):

        self.sample_rate = sample_rate
        self.max_amplitude = max_amplitude
        self.max_deviation = max_deviation
        self.sensitivity_adjust = sensitivity_adjust
        self.verbose = verbose
        self.log = log

        gr.hier_block2.__init__(self,
            "freq_mod_fc",
            gr.io_signature(1, 1, gr.sizeof_float),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_gr_complex)) # Output signature

        # Perform Frequency Modulation
        self.sensitivity = (2 * pi * (self.max_deviation / self.max_amplitude)) / self.sample_rate
        self.fm_modulator = analog.frequency_modulator_fc (self.sensitivity * self.sensitivity_adjust)

        # Connect Blocks
        self.connect(self,
                     self.fm_modulator,
                     self)

        if verbose:
            self._print_verbose()

        if log:
            self._setup_logging()

    def set_max_amplitude(self,
                          max_amplitude=_def_max_amplitude):
        self.max_amplitude = max_amplitude
        self.sensitivity = (2 * pi * (self.max_deviation / self.max_amplitude)) / self.sample_rate
        self.fm_modulator.set_sensitivity(self.sensitivity * self.sensitivity_adjust)
        
    def set_max_deviation(self,
                          max_deviation=_def_max_deviation):
        self.max_deviation = max_deviation
        self.sensitivity = (2 * pi * (self.max_deviation / self.max_amplitude)) / self.sample_rate
        self.fm_modulator.set_sensitivity(self.sensitivity * self.sensitivity_adjust)

    def set_sensitivity_adjust(self,
                               sensitivity_adjust=_def_sensitivity_adjust):
        self.sensitivity_adjust = sensitivity_adjust
        self.fm_modulator.set_sensitivity(self.sensitivity * self.sensitivity_adjust)

    def _print_verbose(self):
        print "P25 Frequency Modulator verbose ON."


    def _setup_logging(self):
        print "P25 Frequency Modulator logging ON."