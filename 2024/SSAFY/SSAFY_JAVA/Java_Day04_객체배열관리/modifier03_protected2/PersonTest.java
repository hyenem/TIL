package modifier03_protected2;

import modifier03_protected.Person;

// 다른 패키지에 있는 클래스
public class PersonTest {
    public static void main(String[] args) {
        Person p = new Person();

        // 다른 클래스에 있으면 기본적으로는 안됨.
        //p.age =10; 
        
    }
}
