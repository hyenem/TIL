package java04_control;

public class Ctrl01_If {
    public static void main(String[] args) {
        // if(조건식) { } 조건식이 참일 경우 블록 내부 수행
        // 조건식: boolean 형태의 값을 봔환하는 식이나, boolean 값이 들어감
        // 수행할 문장이 한 문장이라면 중괄호 생략 가능
        
        int n = 15;
        if(n > 10) {
            System.out.println("블록 내부를 수행한다.");
        }
        
        if(n > 10)
            System.out.println("해당 문장을 수행한다.");
            System.out.println("얘도 수행?"); // 이 문장은 조건문과 관련이 없다.
           
        
              
    }
}
