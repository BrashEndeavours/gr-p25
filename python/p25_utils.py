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

from math import pi, sin, cos
import numpy as np

# default values (used in __init__ and add_options)
_def_sample_rate = 48000
_def_filter_gain = 1.0
_def_symbol_rate = 4800
_def_symbol_deviation = 600 # Symbol deviation in Hz
_def_span = 11  			# Desired number of impulse response coeffs, in units of symbols
_def_dibit_map = [1, 3, -1, -3]
_def_max_deviation = 2827
_def_max_amplitude = 4.388595
_def_sensitivity_adjust = 1.0
_def_gain_adjust = 1.0
_def_verbose = False
_def_log = False

def rx_shaping_filter_gen():
	xfer = []	# frequency domain transfer
	for f in xrange(0,2881):
		# D(f)
		t = pi * f / 4800.0
		if t < 1e-6:
			df = 1.0
		else:
			df = sin (t) / t
		xfer.append(df)
	return xfer

def nyquist_filter_gen():
	xfer = []	# frequency domain transfer
	for f in xrange(0, 2881):
		# H(f)
		if f < 1920:
			hf = 1.0
		else:
			hf = 0.5 + 0.5 * cos (2 * pi * float(f) / 1920.0)
		xfer.append(hf)
	return xfer

def tx_shaping_filter_gen():
	xfer = []	# frequency domain transfer
	for f in xrange(0, 2881):
		# P(f)
		t = pi * f / 4800.0
		if t < 1e-6:
			pf = 1
		else:
			pf = t / sin (t)
		xfer.append(pf)
	return xfer

class generate_taps(object):
	"""
	Generate filter coefficients as per P25 C4FM spec
	"""
	def __init__(self,
			     filter_gain = 1.0,
				 sample_rate=_def_sample_rate,
				 symbol_rate=_def_symbol_rate,
				 span=_def_span,
				 generator=nyquist_filter_gen,
				 verbose=False):
		self.sample_rate = sample_rate
		self.symbol_rate = symbol_rate
		self.filter_gain = filter_gain
		self.sps = int(sample_rate / symbol_rate)
		self.span = span
		self.ntaps = (self.sps * span) | 1
		self.generator = generator
		self.verbose = verbose

	def generate(self):
		if self.verbose ==  True:
			print "Generating Filter verbose ON:"
			print "\t sample rate: %d" %(self.sample_rate)
			print "\t symbol rate: %d" %(self.symbol_rate)
			print "\t filter gain: %d" %(self.filter_gain)
			print "\t filter span: %d" %(self.span)
		impulse_response = np.fft.fftshift(np.fft.irfft(self.generator(), self.sample_rate))
		start = np.argmax(impulse_response) - (self.ntaps-1) / 2
		coeffs = impulse_response[start: start+self.ntaps]
		gain = self.filter_gain
		if self.verbose ==  True:
			print "Sum Coeffs: ", sum(coeffs)
			print "Gain: ", gain
			print "Coeffs: ", coeffs
			print "Coeffs * Gain: ", coeffs * gain
		return coeffs * gain  / sum(coeffs)
		

	def generate_code(self, varname='taps'):
		return '%s = [\n\t%s]' % (varname, ',\n\t'.join(['%10.6e' % f for f in self.generate()]))