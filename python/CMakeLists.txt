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
    dibit_mapper_bf.py
    p25_utils.py
    rx_shaping_filter_ff.py
    tx_shaping_filter_ff.py
    rx_nyquist_filter_ff.py
    tx_nyquist_filter_ff.py
    freq_mod_fc.py
    freq_demod_cf.py
    c4fm_modulator_bf.py
    c4fm_demodulator_fb.py
    c4fm_demodulator_fixed_fb.py DESTINATION ${GR_PYTHON_DIR}/p25
)

########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

set(GR_TEST_TARGET_DEPS gnuradio-p25)
set(GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/swig)
GR_ADD_TEST(qa_dibit_mapper_bf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_dibit_mapper_bf.py)
GR_ADD_TEST(qa_rx_shaping_filter_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_rx_shaping_filter_ff.py)
GR_ADD_TEST(qa_tx_shaping_filter_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_tx_shaping_filter_ff.py)
GR_ADD_TEST(qa_rx_nyquist_filter_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_rx_nyquist_filter_ff.py)
GR_ADD_TEST(qa_tx_nyquist_filter_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_tx_nyquist_filter_ff.py)
GR_ADD_TEST(qa_freq_mod_fc ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_freq_mod_fc.py)
GR_ADD_TEST(qa_freq_demod_cf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_freq_demod_cf.py)
GR_ADD_TEST(qa_c4fm_modulator_bf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_c4fm_modulator_bf.py)
GR_ADD_TEST(qa_c4fm_demodulator_fb ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_c4fm_demodulator_fb.py)
GR_ADD_TEST(qa_c4fm_demodulator_fixed_fb ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_c4fm_demodulator_fixed_fb.py)
