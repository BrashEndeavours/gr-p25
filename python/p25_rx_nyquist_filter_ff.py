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

from gnuradio import gr, gru, filter
from p25_utils import _def_symbol_rate
from p25_utils import _def_sample_rate
from p25_utils import _def_span
from p25_utils import _def_verbose
from p25_utils import _def_log
from p25_utils import generate_taps, nyquist_filter_gen

class p25_rx_nyquist_filter_ff(gr.hier_block2):
    """
    docstring for block p25_rx_nyquist_filter_ff
    """ #
    def __init__(self,
                 filter_gain=1.0,
                 sample_rate=_def_sample_rate,
                 symbol_rate=_def_symbol_rate,
                 span=_def_span,
                 verbose=_def_verbose,
                 log=_def_log):

        self.filter_gain = filter_gain
        self.sample_rate = sample_rate
        self.symbol_rate = symbol_rate
        self.span = span
        self.verbose = verbose
        self.log = log

        gr.hier_block2.__init__(self,
            "p25_rx_nyquist_filter_ff",
            gr.io_signature(1, 1, gr.sizeof_float),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_float))  # Output signature

		# Determine Decimation factor.
        lcm = gru.lcm(self.symbol_rate, self.sample_rate)
        self.decimation = int(lcm // self.sample_rate)

        # Create Nyquist Raised Cosine filter.
        self.nyquist_filter = filter.fir_filter_fff(self.decimation,
                generate_taps(filter_gain=self.filter_gain,
                              sample_rate=self.sample_rate,
                              symbol_rate=self.symbol_rate,
                              span=self.span,
                              generator=nyquist_filter_gen).generate())

        # Define blocks and connect them
        self.connect(self, self.nyquist_filter, self)

    def _print_verbose(self):
        print "P25 RX Nyquist Filter verbose ON."

    def _setup_logging(self):
        print "P25 RX Nyquist Filter logging ON."
