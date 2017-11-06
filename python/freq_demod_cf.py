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
from p25_utils import _def_gain_adjust
from p25_utils import _def_verbose
from p25_utils import _def_log

class freq_demod_cf(gr.hier_block2):
    """
    docstring for block freq_demod_cf
    """
    def __init__(self,
            sample_rate=_def_sample_rate,
            max_amplitude=_def_max_amplitude,
            max_deviation=_def_max_deviation,
            gain_adjust=_def_gain_adjust,
            verbose=_def_verbose,
            log=_def_log):

        self.sample_rate = sample_rate
        self.max_amplitude = max_amplitude
        self.max_deviation = max_deviation
        self.gain_adjust = gain_adjust
        self.verbose = verbose
        self.log = log

        gr.hier_block2.__init__(self,
            "freq_demod_cf",
            gr.io_signature(1, 1, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_float))       # Output signature

        self.gain = self.sample_rate / (2 * pi * (self.max_deviation / max_amplitude))

        # Perform Frequency Demodulation
        self.quadrature_demodulator = analog.quadrature_demod_cf(self.gain * self.gain_adjust)

        # Connect Blocks
        self.connect(self,
                     self.quadrature_demodulator,
                     self)

        if verbose:
            self._print_verbose()

        if log:
            self._setup_logging()

    def set_gain_adjust(self,
                        gain_adjust=_def_gain_adjust):
        self.gain_adjust = gain_adjust
        self.quadrature_demodulator.set_gain(self.gain * self.gain_adjust)
        
    def set_max_amplitude(self,
                          max_amplitude=_def_max_amplitude):
        self.max_amplitude = max_amplitude
        self.gain = self.sample_rate / (2 * pi * (self.max_deviation / self.max_amplitude))
        self.quadrature_demodulator.set_gain(self.gain * self.gain_adjust)

    def set_max_deviation(self,
                          max_deviation=_def_max_deviation):
        if self.verbose:
            print "Max Deviation was:", self.max_deviation, "now, ", max_deviation
        self.max_deviation = max_deviation
        self.gain = self.sample_rate / (2 * pi * (self.max_deviation / self.max_amplitude))
        self.quadrature_demodulator.set_gain(self.gain * self.gain_adjust)

    def _print_verbose(self):
        print "P25 Frequency Demodulator verbose ON."

    def _setup_logging(self):
        print "P25 Frequency Demodulator logging ON."