# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.30

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.30.0/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.30.0/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build

# Include any dependencies generated for this target.
include code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/compiler_depend.make

# Include the progress variables for this target.
include code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/progress.make

# Include the compile flags for this target's objects.
include code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/flags.make

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/flags.make
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitInit.c
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.o -MF CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.o.d -o CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitInit.c

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitInit.c > CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.i

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitInit.c -o CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.s

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/flags.make
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/NuSMVEnv.c
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.o -MF CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.o.d -o CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/NuSMVEnv.c

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/NuSMVEnv.c > CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.i

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/NuSMVEnv.c -o CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.s

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/flags.make
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitData.c
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.o -MF CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.o.d -o CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitData.c

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitData.c > CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.i

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitData.c -o CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.s

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/flags.make
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitVers.c
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.o -MF CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.o.d -o CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitVers.c

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitVers.c > CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.i

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitVers.c -o CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.s

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/flags.make
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitBatch.c
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.o: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.o -MF CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.o.d -o CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitBatch.c

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitBatch.c > CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.i

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit/cinitBatch.c -o CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.s

code_nusmv_core_cinit: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitInit.c.o
code_nusmv_core_cinit: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/NuSMVEnv.c.o
code_nusmv_core_cinit: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitData.c.o
code_nusmv_core_cinit: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitVers.c.o
code_nusmv_core_cinit: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/cinitBatch.c.o
code_nusmv_core_cinit: code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/build.make
.PHONY : code_nusmv_core_cinit

# Rule to build all files generated by this target.
code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/build: code_nusmv_core_cinit
.PHONY : code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/build

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/clean:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit && $(CMAKE_COMMAND) -P CMakeFiles/code_nusmv_core_cinit.dir/cmake_clean.cmake
.PHONY : code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/clean

code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/depend:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/cinit /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : code/nusmv/core/cinit/CMakeFiles/code_nusmv_core_cinit.dir/depend

