/* -*- c++ -*- */

#define THESIS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "thesis_swig_doc.i"

%{
#include "thesis/fourpam_demod_ff.h"
#include "thesis/pam_slicer_fb.h"
#include "thesis/blanker_ff.h"
%}


%include "thesis/fourpam_demod_ff.h"
GR_SWIG_BLOCK_MAGIC2(thesis, fourpam_demod_ff);
%include "thesis/pam_slicer_fb.h"
GR_SWIG_BLOCK_MAGIC2(thesis, pam_slicer_fb);
%include "thesis/blanker_ff.h"
GR_SWIG_BLOCK_MAGIC2(thesis, blanker_ff);
