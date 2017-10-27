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


#ifndef INCLUDED_THESIS_FOURPAM_DEMOD_FF_H
#define INCLUDED_THESIS_FOURPAM_DEMOD_FF_H

#include <thesis/api.h>
#include <gnuradio/block.h>
#include <gnuradio/msg_queue.h>

namespace gr {
  namespace thesis {

    /*!
     * \brief DESCRIPTION HERE
     * \ingroup thesis
     *
     */
    class THESIS_API fourpam_demod_ff : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<fourpam_demod_ff> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of thesis::fourpam_demod_ff.
       *
       * To avoid accidental use of raw pointers, thesis::fourpam_demod_ff's
       * constructor is in a private implementation
       * class. thesis::fourpam_demod_ff::make is the public interface for
       * creating new instances.
       */
      static sptr make(gr::msg_queue::sptr freq_msgs, float sample_rate, float symbol_rate);
    };

  } // namespace thesis
} // namespace gr

#endif /* INCLUDED_THESIS_FOURPAM_DEMOD_FF_H */
