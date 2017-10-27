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
from gnuradio import gr, gru, eng_notation
from gnuradio.digital import modulation_utils
from gnuradio import filter, digital, blocks
from gnuradio.eng_option import eng_option
from optparse import OptionParser

from p25_rx_nyquist_filter_ff import p25_rx_nyquist_filter_ff
from p25_dibit_mapper_bf import p25_dibit_mapper_bf
from p25_rx_shaping_filter_ff import p25_rx_shaping_filter_ff

from thesis import pam_slicer_fb
from thesis import fourpam_demod_ff

from p25_utils import generate_taps, nyquist_filter_gen, rx_shaping_filter_gen
from p25_utils import _def_sample_rate
from p25_utils import _def_symbol_rate
from p25_utils import _def_dibit_map
from p25_utils import _def_span
from p25_utils import _def_filter_gain
from p25_utils import _def_verbose
from p25_utils import _def_log

class p25_c4fm_demodulator_fb(gr.hier_block2):
    """
	Hierarchical block for RRC-filtered P25 FM demodulation.

	The input is a float "C4FM" signal at baseband and the
	output is the dibit (P25 symbol) stream (char, not packed).

	@param sample_rate: sample rate
	@type sample_rate: integer
	@param symbol_rate: symbol rate
	@type symbol_rate: integer
    @param verbose: Print console information?
    @type verbose: bool
    @param log: Log debugging data to console/files?
    @type log: bool
	"""
    def __init__(self,
                 filter_gain=_def_filter_gain,
                 span=_def_span,
                 sample_rate=_def_sample_rate,
				 symbol_rate=_def_symbol_rate,
                 slice_levels=[-2, 0, 2],
                 dibits=[3, 2, 0, 1],
                 verbose=_def_verbose,
                 log=_def_log):

        self.filter_gain = filter_gain
        self.span = span
        self.sample_rate = sample_rate
        self.symbol_rate = symbol_rate
        self.slice_levels = slice_levels
        self.dibits = dibits
        self.verbose = verbose
        self.log = log

        gr.hier_block2.__init__(self, "p25_c4fm_demodulator_bf",
        			gr.io_signature(1, 1, gr.sizeof_float),  # Input signature
        			gr.io_signature(1, 1, gr.sizeof_char))   # Output signature

        # Create RX Shaping filter.
        self.rx_shaping_filter = p25_rx_shaping_filter_ff(
                                filter_gain=self.filter_gain,
                                sample_rate=self.sample_rate,
                                symbol_rate=self.symbol_rate,
                                span=self.span,
                                verbose=self.verbose,
                                log=self.log)

		# Create Nyquist RC filter.
        self.nyquist_filter = p25_rx_nyquist_filter_ff(
                                filter_gain=self.filter_gain,
                                sample_rate=self.sample_rate,
                                symbol_rate=self.symbol_rate,
                                span=self.span,
                                verbose=self.verbose,
                                log=self.log)

        # Create the 4PAM Demodulator
        self.fourpam_demod = fourpam_demod_ff(
                                freq_msgs=gr.msg_queue(2),
                                sample_rate=self.sample_rate,
                                symbol_rate=self.symbol_rate)

		# Create the dibit mapping.
        self.dibits_to_symbols = pam_slicer_fb(
                                slice_levels=self.slice_levels,
                                dibits=self.dibits)

		# All connections.
        self.connect(self,
                     self.rx_shaping_filter,
                     self.nyquist_filter,
                     self.fourpam_demod,
                     self.dibits_to_symbols,
                     self)

        if verbose:
            self._print_verbose()

        if log:
            self._setup_logging()

    def _print_verbose(self):
        print "P25 Demodulator verbose ON."
        print "\t interpolation: %d" %(self._interpolation)
        print "\t decimation: %d" %(self._decimation)
        print "\t sample rate: %d" %(self.sample_rate)
        print "\t symbol rate: %d" %(self.symbol_rate)
        print "\t filter gain: %d" %(self.filter_gain)
        print "\t filter span: %d" %(self.span)

    def _setup_logging(self):
        print "P25 C4FM Demodulator logging ON."
