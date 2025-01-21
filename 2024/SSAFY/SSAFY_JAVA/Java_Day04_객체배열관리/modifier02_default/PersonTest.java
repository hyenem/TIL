package modifier02_default;

// 다른 클래스이지만..
// 같은 패키지 안에 들어있는 클래스
public class PersonTest {
    public static void main(String[] args) {
        Person p = new Person();
        
        p.age = 30; // 같은 패키지이므로 접근 가능.
        // p.name 
        
    }
}
