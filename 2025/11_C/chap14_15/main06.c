#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

void print(char** name){
    printf("print name = %d",sizeof(name));
}
int main() {
    SetConsoleOutputCP(65001);
    char* name[3];
    name[0] = "둘리";
    name[1] = "도우너";
    name[2] = "김수안무";
    printf("main name = %d",sizeof(name));
    print(name);
    
    char** pname = name;
    return 0;
}