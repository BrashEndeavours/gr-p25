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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from hdf5_sink_x import hdf5_sink_b, hdf5_sink_s, hdf5_sink_i, hdf5_sink_f

class _qa_hdf5_sink_x(gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data

class qa_hdf5_sink_b(_qa_hdf5_sink_x):
    def __init__(self):
        super(qa_hdf5_sink_b, self).__init__()

class qa_hdf5_sink_s(_qa_hdf5_sink_x):
    def __init__(self):
        super(qa_hdf5_sink_s, self).__init__()

class qa_hdf5_sink_i(_qa_hdf5_sink_x):
    def __init__(self):
        super(qa_hdf5_sink_i, self).__init__()

class qa_hdf5_sink_f(_qa_hdf5_sink_x):
    def __init__(self):
        super(qa_hdf5_sink_f, self).__init__()

if __name__ == '__main__':
    gr_unittest.run(qa_hdf5_sink_b, "qa_hdf5_sink_b.xml")
    gr_unittest.run(qa_hdf5_sink_s, "qa_hdf5_sink_s.xml")
    gr_unittest.run(qa_hdf5_sink_i, "qa_hdf5_sink_i.xml")
    gr_unittest.run(qa_hdf5_sink_f, "qa_hdf5_sink_f.xml")