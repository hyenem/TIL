package java03_operator;

public class Op05_삼항연산자 {
    public static void main(String[] args) {
        // 삼항연산자
        // 조건식? 식1(참) : 식2(거짓)
        
        //랜덤 숫자 발생기 
        int num = (int) (Math.random() * 10) + 1;
        
        // 0<= Math.random() <1
        // (Math.random() * 10) + 1 : 1부터 10까지의 정수값이 나옴
        
        // num이 홀수인지 짝수인지.
        System.out.println(num);
        System.out.println(num % 2 == 0 ? "짝" : "홀");
    }
}
