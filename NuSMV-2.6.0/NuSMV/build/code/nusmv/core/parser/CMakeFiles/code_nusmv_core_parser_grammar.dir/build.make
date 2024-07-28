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
include code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/compiler_depend.make

# Include the progress variables for this target.
include code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/progress.make

# Include the compile flags for this target's objects.
include code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/flags.make

code/nusmv/core/parser/input.c: code/nusmv/core/parser/input.l
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "[FLEX][nusmv_core_lexer] Building scanner with flex 2.6.4"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser && /usr/bin/flex -Pnusmv_yy -o/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/input.c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/input.l

code/nusmv/core/parser/grammar.c: code/nusmv/core/parser/grammar.y
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "[BISON][nusmv_core_parser] Building parser with bison 2.3"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser && /usr/bin/bison -d -p nusmv_yy -d -o /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y

code/nusmv/core/parser/grammar.h: code/nusmv/core/parser/grammar.c
	@$(CMAKE_COMMAND) -E touch_nocreate code/nusmv/core/parser/grammar.h

code/nusmv/core/parser/input.l: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/input.l.1.25
code/nusmv/core/parser/input.l: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/input.l.1.50
code/nusmv/core/parser/input.l: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/input.l.2.25
code/nusmv/core/parser/input.l: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/input.l.2.50
code/nusmv/core/parser/input.l: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/input.l.2.51
code/nusmv/core/parser/input.l: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/input.l.2.75
code/nusmv/core/parser/input.l: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/input.l.3.50
code/nusmv/core/parser/input.l: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/cmake/combine_grammar.py
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "generating flex source /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/input.l"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser && /Users/kinglerbercy/miniconda3/envs/mabos-standalone/bin/python /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/cmake/../cmake/combine_grammar.py --output /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/input.l input.l.1.25 input.l.1.50 input.l.2.25 input.l.2.50 input.l.2.51 input.l.2.75 input.l.3.50

code/nusmv/core/parser/grammar.y: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/grammar.y.1.25
code/nusmv/core/parser/grammar.y: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/grammar.y.1.50
code/nusmv/core/parser/grammar.y: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/grammar.y.2.50
code/nusmv/core/parser/grammar.y: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/grammar.y.2.51
code/nusmv/core/parser/grammar.y: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser/grammar.y.3.50
code/nusmv/core/parser/grammar.y: /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/cmake/combine_grammar.py
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "generating bison source /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser && /Users/kinglerbercy/miniconda3/envs/mabos-standalone/bin/python /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/cmake/../cmake/combine_grammar.py --output /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.y --start begin grammar.y.1.25 grammar.y.1.50 grammar.y.2.50 grammar.y.2.51 grammar.y.3.50

code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.o: code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/flags.make
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.o: code/nusmv/core/parser/input.c
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.o: code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.o -MF CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.o.d -o CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/input.c

code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/input.c > CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.i

code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/input.c -o CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.s

code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.o: code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/flags.make
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.o: code/nusmv/core/parser/grammar.c
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.o: code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.o"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.o -MF CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.o.d -o CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.o -c /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.c

code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.i"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.c > CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.i

code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.s"
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser && /Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/grammar.c -o CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.s

code_nusmv_core_parser_grammar: code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/input.c.o
code_nusmv_core_parser_grammar: code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/grammar.c.o
code_nusmv_core_parser_grammar: code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/build.make
.PHONY : code_nusmv_core_parser_grammar

# Rule to build all files generated by this target.
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/build: code_nusmv_core_parser_grammar
.PHONY : code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/build

code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/clean:
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser && $(CMAKE_COMMAND) -P CMakeFiles/code_nusmv_core_parser_grammar.dir/cmake_clean.cmake
.PHONY : code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/clean

code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/depend: code/nusmv/core/parser/grammar.c
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/depend: code/nusmv/core/parser/grammar.h
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/depend: code/nusmv/core/parser/grammar.y
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/depend: code/nusmv/core/parser/input.c
code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/depend: code/nusmv/core/parser/input.l
	cd /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/code/nusmv/core/parser /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser /Users/kinglerbercy/Projects/Apps/mas-repo/mabos-standalone/NuSMV-2.6.0/NuSMV/build/code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : code/nusmv/core/parser/CMakeFiles/code_nusmv_core_parser_grammar.dir/depend

