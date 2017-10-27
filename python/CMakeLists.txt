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

########################################################################
# Include python install macros
########################################################################
include(GrPython)
if(NOT PYTHONINTERP_FOUND)
    return()
endif()

########################################################################
# Install python sources
########################################################################
GR_PYTHON_INSTALL(
    FILES
    __init__.py
    p25_utils.py
    p25_c4fm_modulator_bf.py
    p25_dibit_mapper_bf.py
    p25_tx_nyquist_filter_ff.py
    p25_tx_shaping_filter_ff.py
    p25_rx_shaping_filter_ff.py
    p25_freq_mod_fc.py
    p25_rx_nyquist_filter_ff.py
    p25_freq_demod_cf.py
    p25_c4fm_demodulator_fb.py
    nn_demod_learning.py
    bitstream_corpus_b.py
    variable_sink_x.py
    hdf5_sink_x.py
    hdf5_source_x.py DESTINATION ${GR_PYTHON_DIR}/thesis
)

########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

set(GR_TEST_TARGET_DEPS gnuradio-thesis)
set(GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/swig)
GR_ADD_TEST(qa_fourpam_demod_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_fourpam_demod_ff.py)
GR_ADD_TEST(qa_fourpam_slicer_fb ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_fourpam_slicer_fb.py)
GR_ADD_TEST(qa_p25_mod_bf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_mod_bf.py)
GR_ADD_TEST(qa_p25_dibit_mapper_bf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_dibit_mapper.py)
GR_ADD_TEST(qa_p25_tx_nyquist_filter_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_tx_nyquist_filter.py)
GR_ADD_TEST(qa_p25_tx_shaping_filter_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_tx_shaping_filter_ff.py)
GR_ADD_TEST(qa_p25_rx_shaping_filter_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_rx_shaping_filter.py)
GR_ADD_TEST(qa_p25_freq_mod_fc ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_freq_mod_fc.py)
GR_ADD_TEST(qa_p25_rx_nyquist_filter_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_rx_nyquist_filter_ff.py)
GR_ADD_TEST(qa_p25_freq_demod_cf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_freq_demod_cf.py)
GR_ADD_TEST(qa_p25_c4fm_demodulator_fb ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_p25_c4fm_demodulator_fb.py)
GR_ADD_TEST(qa_blanker_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_blanker_ff.py)
GR_ADD_TEST(qa_nn_demod_learning ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_nn_demod_learning.py)
GR_ADD_TEST(qa_bitstream_corpus_b ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_bitstream_corpus_b.py)
GR_ADD_TEST(qa_variable_sink_x ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_variable_sink_x.py)
GR_ADD_TEST(qa_hdf5_sink_x ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_hdf5_sink_x.py)
GR_ADD_TEST(qa_hdf5_source_x ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_hdf5_source_x.py)
