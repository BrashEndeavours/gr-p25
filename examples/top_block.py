#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Nov  5 16:21:08 2017
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.ctrlport.monitor import *
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import gnuradio.filter as filter
import math
import p25
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sample_rate = sample_rate = 48000
        self.noise = noise = 0
        self.input_chooser = input_chooser = 1
        self.delay2_0 = delay2_0 = 17
        self.delay2 = delay2 = 5

        ##################################################
        # Blocks
        ##################################################
        self._noise_range = Range(0, 1, 0.01, 0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise', "counter_slider", float)
        self.top_layout.addWidget(self._noise_win)
        self._input_chooser_options = (0, 1, )
        self._input_chooser_labels = ('Test Symbol stream [3,3,-3,-3]', 'Stochastic Stream', )
        self._input_chooser_tool_bar = Qt.QToolBar(self)
        self._input_chooser_tool_bar.addWidget(Qt.QLabel('Input Selection'+": "))
        self._input_chooser_combo_box = Qt.QComboBox()
        self._input_chooser_tool_bar.addWidget(self._input_chooser_combo_box)
        for label in self._input_chooser_labels: self._input_chooser_combo_box.addItem(label)
        self._input_chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._input_chooser_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._input_chooser_options.index(i)))
        self._input_chooser_callback(self.input_chooser)
        self._input_chooser_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_input_chooser(self._input_chooser_options[i]))
        self.top_grid_layout.addWidget(self._input_chooser_tool_bar, 0,0,1,1)
        self._delay2_0_range = Range(0, 100, 1, 17, 200)
        self._delay2_0_win = RangeWidget(self._delay2_0_range, self.set_delay2_0, 'Input delay', "counter_slider", float)
        self.top_layout.addWidget(self._delay2_0_win)
        self._delay2_range = Range(0, 100, 1, 5, 200)
        self._delay2_win = RangeWidget(self._delay2_range, self.set_delay2, 'delay2', "counter_slider", float)
        self.top_layout.addWidget(self._delay2_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	512, #size
        	48000, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['', '', '', '', '',
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

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	4800, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-5, 5)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Chain Fixed', 'Chain Actual', 'Chain Fixed Test', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, 2, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.p25_freq_mod_fc_0 = p25.freq_mod_fc(
          sample_rate=48000,
          max_amplitude=4.38895,
          max_deviation=2827,
          sensitivity_adjust=1,
          verbose=False,
          log=False
          )
        self.p25_freq_demod_cf_0 = p25.freq_demod_cf(
          sample_rate=48000,
          max_amplitude=4.38895,
          max_deviation=2827,
          gain_adjust=1.0,
          verbose=False,
          log=False
          )
        self.p25_c4fm_modulator_bf_0 = p25.c4fm_modulator_bf(
            filter_gain=1,
            dibit_map=([1.0/3.0, 1.0, -(1.0/3.0), -1.0]),
            sample_rate=48000,
            symbol_rate=4800,
            span=11,
            verbose=False,
            log=False
          )
        self.p25_c4fm_demodulator_fixed_fb_0 = p25.c4fm_demodulator_fixed_fb(
            filter_gain=3.0,
            dibits=([3, 2, 0, 1]),
            sample_rate=48000,
            symbol_rate=4800,
            delay=int(delay2),
            span=11,
            verbose=False,
            log=False
          )
        self.p25_c4fm_demodulator_fb_0 = p25.c4fm_demodulator_fb(
            filter_gain=3.0,
            dibits=([3, 2, 0, 1]),
            sample_rate=48000,
            symbol_rate=4800,
            span=11,
            verbose=False,
            log=False
          )
        self.blocks_vector_source_x_0 = blocks.vector_source_i((1,1,3,3), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_int*1, 240000,True)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 1024)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vii((1 if input_chooser == 1 else 0, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vii((1 if input_chooser == 0 else 0, ))
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(delay2_0))
        self.blocks_ctrlport_monitor_performance_0 = not False or monitor("gr-perf-monitorx")
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_2 = blocks.add_vcc(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vii(1)
        self.analog_random_uniform_source_x_0 = analog.random_uniform_source_i(0, 4, 0)
        self.analog_noise_source_x_1 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, float(noise), 0)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_add_xx_2, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_noise_source_x_1, 0), (self.blocks_add_xx_2, 1))
        self.connect((self.analog_random_uniform_source_x_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.p25_freq_demod_cf_0, 0))
        self.connect((self.blocks_add_xx_2, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.p25_c4fm_modulator_bf_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_skiphead_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.p25_c4fm_demodulator_fb_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.p25_c4fm_demodulator_fixed_fb_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.p25_c4fm_modulator_bf_0, 0), (self.p25_freq_mod_fc_0, 0))
        self.connect((self.p25_freq_demod_cf_0, 0), (self.p25_c4fm_demodulator_fb_0, 0))
        self.connect((self.p25_freq_demod_cf_0, 0), (self.p25_c4fm_demodulator_fixed_fb_0, 0))
        self.connect((self.p25_freq_mod_fc_0, 0), (self.blocks_add_xx_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(float(self.noise))

    def get_input_chooser(self):
        return self.input_chooser

    def set_input_chooser(self, input_chooser):
        self.input_chooser = input_chooser
        self._input_chooser_callback(self.input_chooser)
        self.blocks_multiply_const_vxx_2.set_k((1 if self.input_chooser == 1 else 0, ))
        self.blocks_multiply_const_vxx_1.set_k((1 if self.input_chooser == 0 else 0, ))

    def get_delay2_0(self):
        return self.delay2_0

    def set_delay2_0(self, delay2_0):
        self.delay2_0 = delay2_0
        self.blocks_delay_0.set_dly(int(self.delay2_0))

    def get_delay2(self):
        return self.delay2

    def set_delay2(self, delay2):
        self.delay2 = delay2
        self.p25_c4fm_demodulator_fixed_fb_0.set_delay(int(self.delay2))


def main(top_block_cls=top_block, options=None):

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
    if True:
        if False:
            (tb.blocks_ctrlport_monitor_performance_0).start()
    else:
        sys.stderr.write("Monitor '{0}' does not have an enable ('en') parameter.".format("tb.blocks_ctrlport_monitor_performance_0"))
    qapp.exec_()


if __name__ == '__main__':
    main()
