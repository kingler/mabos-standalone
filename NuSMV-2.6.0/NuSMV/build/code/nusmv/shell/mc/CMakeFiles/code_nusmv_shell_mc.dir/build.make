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
include code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/compiler_depend.make

# Include the progress variables for this target.
include code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/progress.make

# Include the compile flags for this target's objects.
include code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/flags.make

code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.o: code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/flags.make
code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/mc/mcCmd.c
code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.o: code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/mc && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.o -MF CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.o.d -o CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/mc/mcCmd.c

code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/mc && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/mc/mcCmd.c > CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.i

code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/mc && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/mc/mcCmd.c -o CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.s

code_nusmv_shell_mc: code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/mcCmd.c.o
code_nusmv_shell_mc: code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/build.make
.PHONY : code_nusmv_shell_mc

# Rule to build all files generated by this target.
code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/build: code_nusmv_shell_mc
.PHONY : code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/build

code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/clean:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/mc && $(CMAKE_COMMAND) -P CMakeFiles/code_nusmv_shell_mc.dir/cmake_clean.cmake
.PHONY : code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/clean

code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/depend:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/mc /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/mc /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : code/nusmv/shell/mc/CMakeFiles/code_nusmv_shell_mc.dir/depend

