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

#ifndef INCLUDED_THESIS_BLANKER_FF_IMPL_H
#define INCLUDED_THESIS_BLANKER_FF_IMPL_H

#include <thesis/blanker_ff.h>
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/uniform_int_distribution.hpp>

namespace gr {
  namespace thesis {

    class blanker_ff_impl : public blanker_ff
    {
     private:
      const int d_min_normal;
      const int d_max_normal;
      int d_min_blank;
      int d_max_blank;
      bool d_currently_normal;
      int d_normal_streak;
      int d_blank_streak;
      boost::random::mt19937 d_rng;
      boost::random::uniform_int_distribution<> calc_normal_streak;
      boost::random::uniform_int_distribution<> calc_blank_streak;

     public:
      blanker_ff_impl(int min_normal_samples, int max_normal_samples, int min_blank_samples, int max_blank_samples);
      ~blanker_ff_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

      virtual void set_min_blank_samples(int min_blank_samples);
      virtual void set_max_blank_samples(int max_blank_samples);
    };

  } // namespace thesis
} // namespace gr

#endif /* INCLUDED_THESIS_BLANKER_FF_IMPL_H */

