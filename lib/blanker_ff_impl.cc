/* -*- c++ -*- */
/*
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "blanker_ff_impl.h"
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/uniform_int_distribution.hpp>

namespace gr {
  namespace thesis {

    blanker_ff::sptr
    blanker_ff::make(int min_normal_samples, int max_normal_samples, int min_blank_samples, int max_blank_samples)
    {
      return gnuradio::get_initial_sptr
        (new blanker_ff_impl(min_normal_samples, max_normal_samples, min_blank_samples, max_blank_samples));
    }

    /*
     * The private constructor
     */
    blanker_ff_impl::blanker_ff_impl(int min_normal_samples, int max_normal_samples, int min_blank_samples, int max_blank_samples)
      : gr::block("blanker_ff",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float))),
      d_min_normal(min_normal_samples),
      d_max_normal(max_normal_samples),
      d_normal_streak(0),
      d_min_blank(min_blank_samples),
      d_max_blank(max_blank_samples),
      d_blank_streak(0),
      d_currently_normal(true),
      calc_normal_streak(d_min_normal, d_max_normal),
      calc_blank_streak(d_min_blank, d_max_blank)
    {

      d_normal_streak = calc_normal_streak(d_rng);
      d_blank_streak = calc_blank_streak(d_rng);
    }

    /*
     * Our virtual destructor.
     */
    blanker_ff_impl::~blanker_ff_impl()
    {
    }

    void
    blanker_ff_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = noutput_items;
    }

    int
    blanker_ff_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      int samples_consumed = 0;
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      int current_input_index = 0;
      // first we run through all provided data
      for(int i = 0; i < noutput_items; i++) {
	      bool advanced_sample = false;
        do {
          if(d_currently_normal == true) {
            if(d_normal_streak == 0) {
              d_currently_normal = false;
              d_normal_streak = (int)calc_normal_streak(d_rng);
            } else {
              out[i] = in[current_input_index++];
              samples_consumed++;
              advanced_sample = true;
              d_normal_streak--;
            }
          } else {
            if(d_blank_streak == 0) {
              d_currently_normal = true;
              d_blank_streak = (int)calc_blank_streak(d_rng);
            } else {
              out[i] = 0;
              advanced_sample = true;
              d_blank_streak--;
            }
          }
        } while (advanced_sample == false);
      }
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (samples_consumed);
      //produce_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }
    void
    blanker_ff_impl::set_min_blank_samples(int min_blank_samples)
    {
      d_min_blank = min_blank_samples;
      calc_blank_streak = boost::random::uniform_int_distribution<>(d_min_blank, d_max_blank);
      d_blank_streak = calc_blank_streak(d_rng);
    }

    void
    blanker_ff_impl::set_max_blank_samples(int max_blank_samples)
    {
      d_max_blank = max_blank_samples;
      calc_blank_streak = boost::random::uniform_int_distribution<>(d_min_blank, d_max_blank);
      d_blank_streak = calc_blank_streak(d_rng);
    }

  } /* namespace thesis */
} /* namespace gr */

