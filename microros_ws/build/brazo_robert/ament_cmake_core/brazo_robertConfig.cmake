# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_brazo_robert_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED brazo_robert_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(brazo_robert_FOUND FALSE)
  elseif(NOT brazo_robert_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(brazo_robert_FOUND FALSE)
  endif()
  return()
endif()
set(_brazo_robert_CONFIG_INCLUDED TRUE)

# output package information
if(NOT brazo_robert_FIND_QUIETLY)
  message(STATUS "Found brazo_robert: 0.0.0 (${brazo_robert_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'brazo_robert' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT brazo_robert_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(brazo_robert_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${brazo_robert_DIR}/${_extra}")
endforeach()
