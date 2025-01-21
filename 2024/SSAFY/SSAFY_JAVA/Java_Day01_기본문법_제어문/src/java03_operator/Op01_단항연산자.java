package java03_operator;

public class Op01_단항연산자 {

    public static void main(String[] args) {
       // 다음 중 올바른 값을 채워 넣으시오.
        int a = 5;
        System.out.println(a++); // 5, a는 6이 됨.
        System.out.println(++a); // 7
        System.out.println(--a); // 6
        System.out.println(a); // 6
        System.out.println(a--); // 6, a는 5가 됨.
        System.out.println(a++); // 5, a는 6이 됨.
        
        System.out.println(-a); // -6
        System.out.println(~a); // -7 : 1의 보수로 바뀜 
        System.out.println(~7); // -7 : 1의 보수로 바뀜 
        
        System.out.println(!false); // true : 논리 반전
        
    }
    
}
