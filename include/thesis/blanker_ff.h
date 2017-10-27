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


#ifndef INCLUDED_THESIS_BLANKER_FF_H
#define INCLUDED_THESIS_BLANKER_FF_H

#include <thesis/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace thesis {

    /*!
     * \brief <+description of block+>
     * \ingroup thesis
     *
     */
    class THESIS_API blanker_ff : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<blanker_ff> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of thesis::blanker_ff.
       *
       * To avoid accidental use of raw pointers, thesis::blanker_ff's
       * constructor is in a private implementation
       * class. thesis::blanker_ff::make is the public interface for
       * creating new instances.
       */
      static sptr make(int min_normal_samples, int max_normal_samples, int min_blank_samples, int max_blank_samples);

      virtual void set_min_blank_samples(int min_blank_samples) = 0;
      virtual void set_max_blank_samples(int max_blank_samples) = 0;
    };

  } // namespace thesis
} // namespace gr

#endif /* INCLUDED_THESIS_BLANKER_FF_H */

