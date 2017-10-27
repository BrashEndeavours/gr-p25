/* -*- c++ -*- */
/*
 * Copyright 2017 SLt Blake Mackey.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_THESIS_FOURPAM_DEMOD_FF_IMPL_H
#define INCLUDED_THESIS_FOURPAM_DEMOD_FF_IMPL_H

#include <thesis/fourpam_demod_ff.h>

namespace gr {
  namespace thesis {
        /*!
         * \brief DESCRIPTION HERE
         * \ingroup thesis
         *
         */
        class fourpam_demod_ff_impl : public fourpam_demod_ff
        {
         private:
          const float d_block_rate;
          boost::scoped_array<float> d_history;
          size_t d_history_last;
          gr::msg_queue::sptr d_freq_msgs;
          double d_symbol_clock;
          double d_symbol_spread;
          const float d_symbol_time;
          double fine_frequency_correction;
          double coarse_frequency_correction;

          /**
           * Called when we want the input frequency to be adjusted.
           */
          void send_frequency_correction();

          /**
           * Tracking loop.
           */
          bool tracking_loop_mmse(float input, float *output);

         public:
          fourpam_demod_ff_impl(gr::msg_queue::sptr freq_msgs, float sample_rate, float symbol_rate);
          ~fourpam_demod_ff_impl();

          // Where all the action really happens
          void forecast (int noutput_items, gr_vector_int &ninput_items_required);

          int general_work(int noutput_items,
    		       gr_vector_int &ninput_items,
    		       gr_vector_const_void_star &input_items,
    		       gr_vector_void_star &output_items);
        };

  } // namespace thesis
} // namespace gr

#endif /* INCLUDED_THESIS_FOURPAM_DEMOD_FF_IMPL_H */
