package modifier01_private;

public class PersonTest {
    public static void main(String[] args) {
        Person p = new Person();
        
        // p. 접근 불가
        // private은 자기 자신만 접근 가능하므로
        // 다른 클래스에서 접근 불가능
    }
}
