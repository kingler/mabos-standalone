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
include code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/compiler_depend.make

# Include the progress variables for this target.
include code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/progress.make

# Include the compile flags for this target's objects.
include code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/flags.make

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/flags.make
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/Prop.c
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop.c.o -MF CMakeFiles/code_nusmv_core_prop.dir/Prop.c.o.d -o CMakeFiles/code_nusmv_core_prop.dir/Prop.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/Prop.c

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_prop.dir/Prop.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/Prop.c > CMakeFiles/code_nusmv_core_prop.dir/Prop.c.i

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_prop.dir/Prop.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/Prop.c -o CMakeFiles/code_nusmv_core_prop.dir/Prop.c.s

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/flags.make
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/PropDb.c
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.o -MF CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.o.d -o CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/PropDb.c

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/PropDb.c > CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.i

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/PropDb.c -o CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.s

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/flags.make
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/propPkg.c
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.o -MF CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.o.d -o CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/propPkg.c

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/propPkg.c > CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.i

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/propPkg.c -o CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.s

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/flags.make
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/Prop_Rewriter.c
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.o -MF CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.o.d -o CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/Prop_Rewriter.c

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/Prop_Rewriter.c > CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.i

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/Prop_Rewriter.c -o CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.s

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propProp.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/flags.make
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propProp.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/propProp.c
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propProp.c.o: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propProp.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propProp.c.o -MF CMakeFiles/code_nusmv_core_prop.dir/propProp.c.o.d -o CMakeFiles/code_nusmv_core_prop.dir/propProp.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/propProp.c

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propProp.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_prop.dir/propProp.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/propProp.c > CMakeFiles/code_nusmv_core_prop.dir/propProp.c.i

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propProp.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_prop.dir/propProp.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop/propProp.c -o CMakeFiles/code_nusmv_core_prop.dir/propProp.c.s

code_nusmv_core_prop: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop.c.o
code_nusmv_core_prop: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/PropDb.c.o
code_nusmv_core_prop: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propPkg.c.o
code_nusmv_core_prop: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/Prop_Rewriter.c.o
code_nusmv_core_prop: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/propProp.c.o
code_nusmv_core_prop: code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/build.make
.PHONY : code_nusmv_core_prop

# Rule to build all files generated by this target.
code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/build: code_nusmv_core_prop
.PHONY : code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/build

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/clean:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop && $(CMAKE_COMMAND) -P CMakeFiles/code_nusmv_core_prop.dir/cmake_clean.cmake
.PHONY : code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/clean

code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/depend:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/prop /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : code/nusmv/core/prop/CMakeFiles/code_nusmv_core_prop.dir/depend

