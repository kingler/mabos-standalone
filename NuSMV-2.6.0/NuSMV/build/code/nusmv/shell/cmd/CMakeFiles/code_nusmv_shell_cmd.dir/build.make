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
include code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/compiler_depend.make

# Include the progress variables for this target.
include code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/progress.make

# Include the compile flags for this target's objects.
include code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/flags.make

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/flags.make
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmd.c
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.o -MF CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.o.d -o CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmd.c

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmd.c > CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.i

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmd.c -o CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.s

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/flags.make
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdCmd.c
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.o -MF CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.o.d -o CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdCmd.c

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdCmd.c > CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.i

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdCmd.c -o CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.s

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/flags.make
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdFile.c
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.o -MF CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.o.d -o CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdFile.c

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdFile.c > CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.i

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdFile.c -o CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.s

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/flags.make
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdMisc.c
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.o -MF CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.o.d -o CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdMisc.c

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdMisc.c > CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.i

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd/cmdMisc.c -o CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.s

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/flags.make
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.o: code/nusmv/shell/cmd/cmdHelp.c
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.o: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.o -MF CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.o.d -o CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd/cmdHelp.c

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd/cmdHelp.c > CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.i

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd/cmdHelp.c -o CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.s

code_nusmv_shell_cmd: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmd.c.o
code_nusmv_shell_cmd: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdCmd.c.o
code_nusmv_shell_cmd: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdFile.c.o
code_nusmv_shell_cmd: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdMisc.c.o
code_nusmv_shell_cmd: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/cmdHelp.c.o
code_nusmv_shell_cmd: code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/build.make
.PHONY : code_nusmv_shell_cmd

# Rule to build all files generated by this target.
code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/build: code_nusmv_shell_cmd
.PHONY : code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/build

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/clean:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd && $(CMAKE_COMMAND) -P CMakeFiles/code_nusmv_shell_cmd.dir/cmake_clean.cmake
.PHONY : code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/clean

code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/depend:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/shell/cmd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : code/nusmv/shell/cmd/CMakeFiles/code_nusmv_shell_cmd.dir/depend

