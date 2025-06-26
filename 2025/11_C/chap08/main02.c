#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
 
int main() {
    SetConsoleOutputCP(65001);
    
    char name1[5+1];
    name1[0] = 'd'; 
    name1[1] = 'u'; 
    name1[2] = 'l'; 
    name1[3] = 'r'; 
    name1[4] = 'i'; 
    name1[5] = '\0'; 

    printf("name1 = %s \n",name1);

    char name2 [] = "또치";
    printf("name2 = %s \n",name2);

   //name1 = name2;
    
    char name3[] = "홍길동";
    char name4[20];
    printf("%s \n", name1);
    printf("%s \n", name2);
    printf("%s \n", name3);

    printf("%d \n", strlen(name1));  // 문자열 길이
    printf("%d \n", strlen(name3));  // 한글은 2개씩
    printf("%d \n", strcmp(name1, name2)); // -1,0,1
    printf("%s \n", strcpy(name4, "하이"));
    printf("%s \n", strcat(name4, " 홍길동"));
    printf("%u \n", strchr(name4, '홍')); //주소리턴
    printf("%d \n", strcspn(name4, "길동")); //시작인덱스리턴(한글2)

    return 0;
}