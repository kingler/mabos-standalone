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
include code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/compiler_depend.make

# Include the progress variables for this target.
include code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/progress.make

# Include the compile flags for this target's objects.
include code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/flags.make

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/flags.make
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyBase.c
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.o -MF CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.o.d -o CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyBase.c

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyBase.c > CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.i

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyBase.c -o CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.s

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/flags.make
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyCore.c
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.o -MF CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.o.d -o CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyCore.c

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyCore.c > CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.i

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyCore.c -o CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.s

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/flags.make
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyPsl.c
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.o -MF CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.o.d -o CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyPsl.c

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyPsl.c > CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.i

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/DependencyPsl.c -o CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.s

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/flags.make
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/dependencyPkg.c
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.o -MF CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.o.d -o CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/dependencyPkg.c

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/dependencyPkg.c > CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.i

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/dependencyPkg.c -o CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.s

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/flags.make
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.o: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/FormulaDependency.c
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.o: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.o -MF CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.o.d -o CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/FormulaDependency.c

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/FormulaDependency.c > CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.i

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency/FormulaDependency.c -o CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.s

code_nusmv_core_compile_dependency: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyBase.c.o
code_nusmv_core_compile_dependency: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyCore.c.o
code_nusmv_core_compile_dependency: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependencyPsl.c.o
code_nusmv_core_compile_dependency: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/dependencyPkg.c.o
code_nusmv_core_compile_dependency: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/FormulaDependency.c.o
code_nusmv_core_compile_dependency: code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/build.make
.PHONY : code_nusmv_core_compile_dependency

# Rule to build all files generated by this target.
code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/build: code_nusmv_core_compile_dependency
.PHONY : code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/build

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/clean:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency && $(CMAKE_COMMAND) -P CMakeFiles/code_nusmv_core_compile_dependency.dir/cmake_clean.cmake
.PHONY : code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/clean

code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/depend:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/compile/dependency /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : code/nusmv/core/compile/dependency/CMakeFiles/code_nusmv_core_compile_dependency.dir/depend

