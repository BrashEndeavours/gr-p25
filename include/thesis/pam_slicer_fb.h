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


#ifndef INCLUDED_THESIS_PAM_SLICER_FB_H
#define INCLUDED_THESIS_PAM_SLICER_FB_H

#include <thesis/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace thesis {

    /*!
     * \brief <+description of block+>
     * \ingroup thesis
     *
     */
    class THESIS_API pam_slicer_fb : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<pam_slicer_fb> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of thesis::pam_slicer_fb.
       *
       * To avoid accidental use of raw pointers, thesis::pam_slicer_fb's
       * constructor is in a private implementation
       * class. thesis::pam_slicer_fb::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::vector<float> &slice_levels, const std::vector<int> &dibits);
    };

  } // namespace thesis
} // namespace gr

#endif /* INCLUDED_THESIS_PAM_SLICER_FB_H */
