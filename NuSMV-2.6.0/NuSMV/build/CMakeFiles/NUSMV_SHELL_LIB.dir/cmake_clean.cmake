file(REMOVE_RECURSE
  "lib/libnusmvshell.a"
  "lib/libnusmvshell.pdb"
)

# Per-language clean rules from dependency scanning.
foreach(lang C)
  include(CMakeFiles/NUSMV_SHELL_LIB.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
