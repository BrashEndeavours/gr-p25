INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_P25 p25)

FIND_PATH(
    P25_INCLUDE_DIRS
    NAMES p25/api.h
    HINTS $ENV{P25_DIR}/include
        ${PC_P25_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    P25_LIBRARIES
    NAMES gnuradio-p25
    HINTS $ENV{P25_DIR}/lib
        ${PC_P25_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(P25 DEFAULT_MSG P25_LIBRARIES P25_INCLUDE_DIRS)
MARK_AS_ADVANCED(P25_LIBRARIES P25_INCLUDE_DIRS)

