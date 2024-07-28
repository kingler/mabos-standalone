file(REMOVE_RECURSE
  "lib/libnusmvgrammar.a"
  "lib/libnusmvgrammar.pdb"
)

# Per-language clean rules from dependency scanning.
foreach(lang C)
  include(CMakeFiles/NUSMV_GRAMMAR_LIB.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
