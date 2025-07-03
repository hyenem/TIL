#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

struct person{
    char* name;
    int age;
};

int main() {
    SetConsoleOutputCP(65001);
    struct person arr[3];
    printf("sizeof = %d\n", sizeof(struct person));
    printf("sizeof = %d\n", sizeof(arr));

    for (size_t i = 0; i < 3; i++)
    {
        arr[i].name =(char*)malloc(10);
    }
    

    for (size_t i = 0; i < 3; i++)
    {
        free(arr[i].name);
    }
    
    return 0;
}