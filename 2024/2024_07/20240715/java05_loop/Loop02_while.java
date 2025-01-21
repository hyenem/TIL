package java05_loop;

public class Loop02_while {
    public static void main(String[] args) {
        // while(조건식) { 반복내용}
        // 조건식 생략 불가능
        
        
        int n = 10;
        
        // 조건식이 위배가 되게끔 증감을 결정해야 한다.
        while(n > 5) {
            System.out.println("이거 실행되나? "+n);
            n--;
        }
        
    }
}
