#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

struct person{
    char* name;
    int age;
};
// 구조체의 포인트 배열
int main() {
    SetConsoleOutputCP(65001);
    
    struct person* arr[3];
    for (size_t i = 0; i < 3; i++)
    {
        arr[i] = (struct person*)malloc(sizeof(struct person));
        arr[i] -> name = (char*)malloc(sizeof(10+1));
    }
    
    arr[0]->age = 10;
    strcpy(arr[0]->name, "둘리");

    for (size_t i = 0; i < 3; i++)
    {
        free(arr[i]->name);
        free(arr[i]);
    }
    

    return 0;
}