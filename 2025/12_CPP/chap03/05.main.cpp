#include <iostream>
#include <cstdlib>
#include <windows.h>
#include "point.h"
using namespace std;

int main() {
    SetConsoleOutputCP(65001);

    Point p;
    p.printPoint();

    return 0;
}