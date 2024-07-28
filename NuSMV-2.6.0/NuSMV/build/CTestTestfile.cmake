# CMake generated Testfile for 
# Source directory: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV
# Build directory: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(short "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/bin/NuSMV" "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/examples/smv-dist/short.smv")
set_tests_properties(short PROPERTIES  _BACKTRACE_TRIPLES "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/CMakeLists.txt;607;add_test;/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/CMakeLists.txt;0;")
add_test(bmc "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/bin/NuSMV" "-bmc" "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/examples/bmc/barrel5.smv")
set_tests_properties(bmc PROPERTIES  _BACKTRACE_TRIPLES "/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/CMakeLists.txt;611;add_test;/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/CMakeLists.txt;0;")
subdirs("build-cudd")
subdirs("build-MiniSat")
subdirs("code/nusmv/core")
subdirs("code/nusmv/addons_core")
subdirs("code/nusmv/shell")
subdirs("doc")
subdirs("contrib")
subdirs("examples")
