#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
/*

*/
struct person{
    char* name;
    int age;
};

int main() {
    SetConsoleOutputCP(65001);
    
    char tmp[] = "둘리";
    struct person p;
    
    p.name = (char*)malloc(strlen(tmp)+1);
    strcpy(p.name, tmp);

    free(p.name);
    return 0;
}