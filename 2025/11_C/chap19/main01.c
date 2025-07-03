#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#include "point.h"
#include "point2.h"

int main() {
    SetConsoleOutputCP(65001);

    Point p;
    p.r = 10;
    p.c = 20;
    p.cnt = 30;

    printf("%d %d %d\n", p.r, p.c, p.cnt);

    return 0;
}
