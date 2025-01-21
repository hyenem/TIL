package java03_operator;

public class Op04_논리연산자 {
    public static void main(String[] args) {
        
        System.out.println(true && true); // t
        System.out.println(true && false); // f
        System.out.println(false && true); // f
        System.out.println(false && false); // f
        
        System.out.println(true || true);
        System.out.println(true || false);
        System.out.println(false || true);
        System.out.println(false || false);
        
        int a = 10;
        int b = 20;
        // 기본
        
        System.out.println(a > b && a++ > b); // short circuit 발생(하나만 확인)
        System.out.println(a);
        System.out.println(a < b && a++ < b); // 둘다 확인 
        System.out.println(a);
        
        System.out.println(a > b || a++ > b); // 둘다 확인 
        System.out.println(a);
        System.out.println(a < b || a++ < b); // short circuit 발생 (앞에거 하나만 확인)
        System.out.println(a);
        
        
        System.out.println("-----");
        
        a = 10;
        b = 20;
        
        System.out.println(a > b & a++ > b); // 둘다 확인
        System.out.println(a);
        System.out.println(a < b & a++ < b); // 둘다 확인 
        System.out.println(a);
        
        System.out.println(a > b | a++ > b); // 둘다 확인 
        System.out.println(a);
        System.out.println(a < b | a++ < b); // 둘다 확인
        System.out.println(a);
        
        
        
        
        
    }
}
