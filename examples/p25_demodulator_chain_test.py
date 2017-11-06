#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: p25_demodulator_chain_test
# Generated: Sun Nov  5 13:43:16 2017
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import gnuradio.filter as filter
import logging
import math
import p25
import pam
import sip
import sys
from gnuradio import qtgui


class p25_demodulator_chain_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "p25_demodulator_chain_test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("p25_demodulator_chain_test")
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

        self.settings = Qt.QSettings("GNU Radio", "p25_demodulator_chain_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.wave_delay = wave_delay = 5
        self.sample_rate = sample_rate = 48000
        self.input_chooser = input_chooser = 1
        self.dibits_delay = dibits_delay = 17
        self.dibit_delay = dibit_delay = 11
        self.adjustment = adjustment = 0.051533333 * 48000 / 4800

        ##################################################
        # Blocks
        ##################################################
        self.tab1 = Qt.QTabWidget()
        self.tab1_widget_0 = Qt.QWidget()
        self.tab1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_0)
        self.tab1_grid_layout_0 = Qt.QGridLayout()
        self.tab1_layout_0.addLayout(self.tab1_grid_layout_0)
        self.tab1.addTab(self.tab1_widget_0, 'Byte to Dibit Mapping')
        self.tab1_widget_1 = Qt.QWidget()
        self.tab1_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_1)
        self.tab1_grid_layout_1 = Qt.QGridLayout()
        self.tab1_layout_1.addLayout(self.tab1_grid_layout_1)
        self.tab1.addTab(self.tab1_widget_1, 'Dibit to C4FM Mapping')
        self.tab1_widget_2 = Qt.QWidget()
        self.tab1_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_2)
        self.tab1_grid_layout_2 = Qt.QGridLayout()
        self.tab1_layout_2.addLayout(self.tab1_grid_layout_2)
        self.tab1.addTab(self.tab1_widget_2, 'Waveform Recovery')
        self.tab1_widget_3 = Qt.QWidget()
        self.tab1_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_3)
        self.tab1_grid_layout_3 = Qt.QGridLayout()
        self.tab1_layout_3.addLayout(self.tab1_grid_layout_3)
        self.tab1.addTab(self.tab1_widget_3, 'Non-Sliced Dibit Recovery')
        self.tab1_widget_4 = Qt.QWidget()
        self.tab1_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_4)
        self.tab1_grid_layout_4 = Qt.QGridLayout()
        self.tab1_layout_4.addLayout(self.tab1_grid_layout_4)
        self.tab1.addTab(self.tab1_widget_4, 'Sliced Dibit Recovery')
        self.top_layout.addWidget(self.tab1)
        self._wave_delay_range = Range(0, 200, 1, 5, 200)
        self._wave_delay_win = RangeWidget(self._wave_delay_range, self.set_wave_delay, 'Waveform Delay', "counter_slider", float)
        self.tab1_layout_3.addWidget(self._wave_delay_win)
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
        self._dibits_delay_range = Range(0, 200, 1, 17, 200)
        self._dibits_delay_win = RangeWidget(self._dibits_delay_range, self.set_dibits_delay, 'Dibits Delay', "counter_slider", float)
        self.tab1_layout_3.addWidget(self._dibits_delay_win)
        self._dibit_delay_range = Range(0, 200, 1, 11, 200)
        self._dibit_delay_win = RangeWidget(self._dibit_delay_range, self.set_dibit_delay, 'Dibit Delay', "counter_slider", float)
        self.tab1_layout_1.addWidget(self._dibit_delay_win)
        self.qtgui_time_sink_x_0_0_0_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	48000, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_update_time(0.0001)
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_y_axis(-4, 4)

        self.qtgui_time_sink_x_0_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0_0.disable_legend()

        labels = ['Original Dibit', 'Recovered Dibit', 'Sliced Dibit', 'Error', '',
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
                self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab1_layout_4.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_0_win)
        self.qtgui_time_sink_x_0_0_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	48000, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0_0.set_update_time(0.0001)
        self.qtgui_time_sink_x_0_0_0_0_0.set_y_axis(-4, 4)

        self.qtgui_time_sink_x_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0_0.disable_legend()

        labels = ['Transmitted Dibit', 'Shaped Waveform', 'Recovered Dibit', 'Error', '',
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
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab1_layout_3.addWidget(self._qtgui_time_sink_x_0_0_0_0_0_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	256, #size
        	48000, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.0001)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-4, 4)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['Original Byte', 'C4FM Waveform', 'Output Block Dibit', '', '',
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
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab1_layout_1.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	128, #size
        	48000, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.0001)
        self.qtgui_time_sink_x_0_0.set_y_axis(-4, 4)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['Original Byte', 'Converted Dibit', 'Output Block Dibit', '', '',
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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab1_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.pam_pam_slicer_fb_0 = pam.pam_slicer_fb(slice_levels=([-2, 0, 2]), dibits=([-3, -1, 1, 3]))
        self.p25_rx_shaping_filter_ff_0 = p25.rx_shaping_filter_ff(
            filter_gain=3,
            sample_rate=48000,
            symbol_rate=4800,
            span=11,
            verbose=False,
            log=False
          )
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
        self.p25_dibit_mapper_bf_0 = p25.dibit_mapper_bf(
            dibit_map=([1, 3, -1, -3]),
            log_level=logging.NOTSET,
            filename=''
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
        self.interp_fir_filter_xxx_0_0_1 = filter.interp_fir_filter_fff(10, ((1,)))
        self.interp_fir_filter_xxx_0_0_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0_0 = filter.interp_fir_filter_fff(10, ((1,)))
        self.interp_fir_filter_xxx_0_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_fff(10, ((1,)))
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(10, ((1,)))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(10, ((1,)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(10, ((0,0,0,0,0,1,)))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_vector_source_x_0 = blocks.vector_source_i((1,1,3,3), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_int*1, 240000,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vii((1 if input_chooser == 1 else 0, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vii((1 if input_chooser == 0 else 0, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((3, ))
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_0_0_0_1 = blocks.delay(gr.sizeof_float*1, int(dibits_delay))
        self.blocks_delay_0_0_0_0 = blocks.delay(gr.sizeof_float*1, int(wave_delay))
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, int(dibits_delay))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(dibit_delay))
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vii(1)
        self.analog_random_uniform_source_x_0 = analog.random_uniform_source_i(0, 4, 0)
        self._adjustment_range = Range(0, 10, 0.01, 0.051533333 * 48000 / 4800, 200)
        self._adjustment_win = RangeWidget(self._adjustment_range, self.set_adjustment, 'Sensitivity', "counter_slider", float)
        self.top_grid_layout.addWidget(self._adjustment_win, 1,0,1,5)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_uniform_source_x_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.interp_fir_filter_xxx_0_0_1, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_delay_0_0_0, 0), (self.interp_fir_filter_xxx_0_0_0, 0))
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 1))
        self.connect((self.blocks_delay_0_0_0_1, 0), (self.interp_fir_filter_xxx_0_0_0_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.p25_c4fm_modulator_bf_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.p25_dibit_mapper_bf_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.pam_pam_slicer_fb_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 2))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_1, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.interp_fir_filter_xxx_0_0_1, 0), (self.qtgui_time_sink_x_0_0_0_0_0_0, 1))
        self.connect((self.p25_c4fm_modulator_bf_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.p25_c4fm_modulator_bf_0, 0), (self.p25_freq_mod_fc_0, 0))
        self.connect((self.p25_dibit_mapper_bf_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.p25_dibit_mapper_bf_0, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.p25_dibit_mapper_bf_0, 0), (self.blocks_delay_0_0_0_1, 0))
        self.connect((self.p25_dibit_mapper_bf_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.p25_freq_demod_cf_0, 0), (self.p25_rx_shaping_filter_ff_0, 0))
        self.connect((self.p25_freq_mod_fc_0, 0), (self.p25_freq_demod_cf_0, 0))
        self.connect((self.p25_rx_shaping_filter_ff_0, 0), (self.blocks_delay_0_0_0_0, 0))
        self.connect((self.p25_rx_shaping_filter_ff_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.pam_pam_slicer_fb_0, 0), (self.blocks_char_to_float_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "p25_demodulator_chain_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_wave_delay(self):
        return self.wave_delay

    def set_wave_delay(self, wave_delay):
        self.wave_delay = wave_delay
        self.blocks_delay_0_0_0_0.set_dly(int(self.wave_delay))

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_input_chooser(self):
        return self.input_chooser

    def set_input_chooser(self, input_chooser):
        self.input_chooser = input_chooser
        self._input_chooser_callback(self.input_chooser)
        self.blocks_multiply_const_vxx_2.set_k((1 if self.input_chooser == 1 else 0, ))
        self.blocks_multiply_const_vxx_1.set_k((1 if self.input_chooser == 0 else 0, ))

    def get_dibits_delay(self):
        return self.dibits_delay

    def set_dibits_delay(self, dibits_delay):
        self.dibits_delay = dibits_delay
        self.blocks_delay_0_0_0_1.set_dly(int(self.dibits_delay))
        self.blocks_delay_0_0_0.set_dly(int(self.dibits_delay))

    def get_dibit_delay(self):
        return self.dibit_delay

    def set_dibit_delay(self, dibit_delay):
        self.dibit_delay = dibit_delay
        self.blocks_delay_0.set_dly(int(self.dibit_delay))

    def get_adjustment(self):
        return self.adjustment

    def set_adjustment(self, adjustment):
        self.adjustment = adjustment


def main(top_block_cls=p25_demodulator_chain_test, options=None):

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
