# Install script for directory: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/Library/Developer/CommandLineTools/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/nusmv/contrib" TYPE FILE FILES
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/README"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/iscas89-2smv"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/kiss2-2smv"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/smv2table.awk"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/smv-mode.el"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/order_bits.pl"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/nusmv-mode.el"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/NuSMV.m4"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/emacs-gdb-macros.el"
    "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/contrib/remove_string.pl"
    )
endif()

