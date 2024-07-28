file(REMOVE_RECURSE
  "lib/libnusmvaddonscore.a"
  "lib/libnusmvaddonscore.pdb"
)

# Per-language clean rules from dependency scanning.
foreach(lang C)
  include(CMakeFiles/NUSMV_ADDONSCORE_LIB.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
