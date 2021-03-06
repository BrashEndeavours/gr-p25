#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: rx_filter_test
# Generated: Sun Nov  5 11:53:42 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import logging
import p25
import sip
import sys
from gnuradio import qtgui


class rx_filter_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "rx_filter_test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("rx_filter_test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "rx_filter_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sample_rate = sample_rate = 4800
        self.rec_delay = rec_delay = 5
        self.orig_bit_delay = orig_bit_delay = 60
        self.chan_delay = chan_delay = 5

        ##################################################
        # Blocks
        ##################################################
        self._rec_delay_range = Range(0, 200, 1, 5, 200)
        self._rec_delay_win = RangeWidget(self._rec_delay_range, self.set_rec_delay, 'Recover Delay', "counter_slider", float)
        self.top_layout.addWidget(self._rec_delay_win)
        self._orig_bit_delay_range = Range(0, 300, 1, 60, 200)
        self._orig_bit_delay_win = RangeWidget(self._orig_bit_delay_range, self.set_orig_bit_delay, 'Original Bit Delay', "counter_slider", float)
        self.top_layout.addWidget(self._orig_bit_delay_win)
        self._chan_delay_range = Range(0, 200, 1, 5, 200)
        self._chan_delay_win = RangeWidget(self._chan_delay_range, self.set_chan_delay, 'Channel Delay', "counter_slider", float)
        self.top_layout.addWidget(self._chan_delay_win)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
        	256, #size
        	48000, #samp_rate
        	'Nyquist Filter Test', #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.5)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-5, 5)

        self.qtgui_time_sink_x_0_1_0.set_y_label('Level', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(True)

        if not True:
          self.qtgui_time_sink_x_0_1_0.disable_legend()

        labels = ['Original Bits', 'Channel Waveform', 'Post Bits', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_win)
        self.p25_tx_nyquist_filter_ff_0 = p25.tx_nyquist_filter_ff(
            filter_gain=1.0,
            sample_rate=48000,
            symbol_rate=4800,
            span=11,
            verbose=False,
            log=False
          )
        self.p25_dibit_mapper_bf_0 = p25.dibit_mapper_bf(
            dibit_map=([1, 3, -1, -3]),
            log_level=logging.NOTSET,
            filename=''
          )
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(10, ((1,)))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(10, ((1,)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(10, ((1,0,0,0,0,0,0,0,0,0)))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_int*1, sample_rate,True)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_0_1_0_0 = blocks.delay(gr.sizeof_float*1, int(rec_delay))
        self.blocks_delay_0_1_0 = blocks.delay(gr.sizeof_float*1, int(chan_delay))
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, int(orig_bit_delay))
        self.analog_random_uniform_source_x_0 = analog.random_uniform_source_i(0, 4, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_uniform_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.blocks_delay_0_1_0, 0), (self.qtgui_time_sink_x_0_1_0, 1))
        self.connect((self.blocks_delay_0_1_0_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.p25_dibit_mapper_bf_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_1_0, 2))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.p25_dibit_mapper_bf_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.p25_dibit_mapper_bf_0, 0), (self.p25_tx_nyquist_filter_ff_0, 0))
        self.connect((self.p25_tx_nyquist_filter_ff_0, 0), (self.blocks_delay_0_1_0, 0))
        self.connect((self.p25_tx_nyquist_filter_ff_0, 0), (self.blocks_delay_0_1_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rx_filter_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.blocks_throttle_0.set_sample_rate(self.sample_rate)

    def get_rec_delay(self):
        return self.rec_delay

    def set_rec_delay(self, rec_delay):
        self.rec_delay = rec_delay
        self.blocks_delay_0_1_0_0.set_dly(int(self.rec_delay))

    def get_orig_bit_delay(self):
        return self.orig_bit_delay

    def set_orig_bit_delay(self, orig_bit_delay):
        self.orig_bit_delay = orig_bit_delay
        self.blocks_delay_0_1.set_dly(int(self.orig_bit_delay))

    def get_chan_delay(self):
        return self.chan_delay

    def set_chan_delay(self, chan_delay):
        self.chan_delay = chan_delay
        self.blocks_delay_0_1_0.set_dly(int(self.chan_delay))


def main(top_block_cls=rx_filter_test, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
