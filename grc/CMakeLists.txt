# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

install(FILES
    thesis_fourpam_demod_ff.xml
    thesis_pam_slicer_fb.xml
    thesis_p25_c4fm_modulator_bf.xml
    thesis_p25_dibit_mapper_bf.xml
    thesis_p25_tx_nyquist_filter_ff.xml
    thesis_p25_tx_shaping_filter_ff.xml
    thesis_p25_rx_shaping_filter_ff.xml
    thesis_p25_freq_mod_fc.xml
    thesis_p25_rx_nyquist_filter_ff.xml
    thesis_p25_freq_demod_cf.xml
    thesis_p25_c4fm_demodulator_fb.xml
    thesis_blanker_ff.xml
    thesis_nn_demod_learning.xml
    thesis_bitstream_corpus_b.xml
    thesis_variable_sink_x.xml
    thesis_hdf5_sink_x.xml
    thesis_hdf5_source_x.xml DESTINATION share/gnuradio/grc/blocks
)
