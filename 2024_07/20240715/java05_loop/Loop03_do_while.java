package java05_loop;

import java.util.Scanner;

public class Loop03_do_while {
    public static void main(String[] args) {
        // do {
        // 실행 문장
        // } while(조건식);
        // 무조건 한번은 수행하고 조건식 판별하므로 
        // 최소 한 번은 실행.
        
        Scanner sc = new Scanner(System.in);
        int num;
        
        do {
            System.out.println("숫자를 입력하세요. (0이면 종료)");
            num = sc.nextInt();
        } while(num != 0);
        
    }
}
