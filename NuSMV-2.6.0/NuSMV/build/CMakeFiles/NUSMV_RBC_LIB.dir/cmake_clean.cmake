file(REMOVE_RECURSE
  "lib/libnusmvrbc.a"
  "lib/libnusmvrbc.pdb"
)

# Per-language clean rules from dependency scanning.
foreach(lang C)
  include(CMakeFiles/NUSMV_RBC_LIB.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
