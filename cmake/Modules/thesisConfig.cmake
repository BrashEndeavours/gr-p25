INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_THESIS thesis)

FIND_PATH(
    THESIS_INCLUDE_DIRS
    NAMES thesis/api.h
    HINTS $ENV{THESIS_DIR}/include
        ${PC_THESIS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    THESIS_LIBRARIES
    NAMES gnuradio-thesis
    HINTS $ENV{THESIS_DIR}/lib
        ${PC_THESIS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(THESIS DEFAULT_MSG THESIS_LIBRARIES THESIS_INCLUDE_DIRS)
MARK_AS_ADVANCED(THESIS_LIBRARIES THESIS_INCLUDE_DIRS)

