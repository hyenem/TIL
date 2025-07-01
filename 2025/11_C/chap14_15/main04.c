#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
    
    char name1[][10] = {"둘리","도우너","고길동"};
    printf("%d\n",sizeof(name1));

    char* name2[3];
    name2[0] = "둘리";
    name2[1] = "도우너";
    name2[2] = "김수안무";

    for (size_t i = 0; i < sizeof(name2)/sizeof(name2[0]); i++){
        for (size_t j = 0; j < sizeof(name2[0])/sizeof(name2[0][0]); j++){
            printf("%d ",name2[i][j]);
        }
        printf("\n");
    }
    return 0;
}