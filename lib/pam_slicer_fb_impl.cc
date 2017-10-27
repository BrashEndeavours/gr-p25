/* -*- c++ -*- */
/*
 * Copyright 2017 Blake Mackey.
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
#include "pam_slicer_fb_impl.h"

namespace gr {
  namespace thesis {

    pam_slicer_fb::sptr
    pam_slicer_fb::make(const std::vector<float> &slice_levels, const std::vector<int> &dibits)
    {
      return gnuradio::get_initial_sptr
        (new pam_slicer_fb_impl(slice_levels, dibits));
    }

    /*
     * The private constructor
     */
    pam_slicer_fb_impl::pam_slicer_fb_impl(const std::vector<float> &slice_levels, const std::vector<int> &dibits)
      : gr::sync_block("pam_slicer_fb",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(unsigned char)))
      , d_slice_levels(slice_levels)
      , d_dibits(dibits)
    {
    }

    /*
     * Our virtual destructor.
     */
    pam_slicer_fb_impl::~pam_slicer_fb_impl()
    {
    }

    int
    pam_slicer_fb_impl::work(int noutput_items,
			      gr_vector_const_void_star &input_items,
			      gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];

      for(int i = 0; i < noutput_items; i++) {
	      bool found = false;
	      float sym = in[i];
        for (std::vector<float>::const_iterator i_slice = d_slice_levels.begin(); i_slice != d_slice_levels.end(); i_slice++){
  	      if(sym < *i_slice) {
  	        out[i] = d_dibits[std::distance(d_slice_levels.begin(), i_slice)];
            found = true;
            break;
          }
        }
        if (found == false){
          out[i] = d_dibits[d_dibits.size() - 1];
        }
	    }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace thesis */
} /* namespace gr */
