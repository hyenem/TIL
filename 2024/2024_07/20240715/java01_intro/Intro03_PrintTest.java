package java01_intro;

public class Intro03_PrintTest {
    public static void main(String[] args) {
        
        //print를 써보자
        System.out.print("Hello World\n");
        
        // 주석처리 : ctrl+/
        // \n을 사용하면 줄이 바뀐다.
        System.out.println("Hello World!!!");
        System.out.println("Hello World!!!");
        
        System.out.println("\\");
        System.out.println("\"");
        
        //printf : 포맷지정자 <= 어떤 값이 들어갈 자리
        System.out.printf("%d\n", 10); // 정수 (10진수)
        System.out.printf("%o\n", 10); // 정수 (8진수)
        System.out.printf("%x\n", 10); // 정수 (16진수) 소문자 
        System.out.printf("%X\n", 10); // 정수 (16진수) 대문자 
        
        System.out.printf("%4d\n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지 
        System.out.printf("%-4d\n", 10); // 4칸을 확보한 뒤 왼쪽부터 차지 
        System.out.printf("%04d\n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지 (빈칸은 0으로 채움)
        
        System.out.printf("%f\n", 10.12345); // 실수 (별다른 지정 없으면 소수점 여섯째자리까지 반올림)
        System.out.printf("%.2f\n", 10.12345); // 실수 (소수점 둘째자리까지 반올림)
        
        System.out.printf("%s\n", "싸피"); // 문자열
        System.out.printf("%c\n", 'A'); // 문자 
        System.out.printf("%d\n", (int)'A'); // 문자를 정수로 출력
        
        String str1;
        String str2;
        System.out.println(str1==str2);
        
    }
}
