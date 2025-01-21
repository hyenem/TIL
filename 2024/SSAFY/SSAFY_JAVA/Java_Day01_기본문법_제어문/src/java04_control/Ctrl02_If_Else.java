package java04_control;

public class Ctrl02_If_Else {
    public static void main(String[] args) {
        // if(조건식) { } 조건식이 참일 경우 if 블록 내부 수행
        // else { } 조건식이 거짓인 경우 else 블록 내부 수행 
        
        // 무슨 음료를 마실 수 있는가?
        int age = 17;
        
        if(age < 20){
            System.out.println("사이다만 마실 수 있다.");
        } else {
           System.out.println("맥주를 마실 수 있다.");
        }
        
        // ㅇㅇ랜드 입장권 가격은??
        int price;
        if( age < 20)
            price = 20000;
        else
            price = 50000;
        
        System.out.println(price);
        
        
    }
}
