#include "library.h"

#include <iostream>

#include <range/v3/all.hpp>

void hello() {
   using std::cout;

   std::string s{"hello"};

   // output: h e l l o
   ranges::for_each(s, [](char c) { cout << c << ' '; });
   cout << '\n';
}
