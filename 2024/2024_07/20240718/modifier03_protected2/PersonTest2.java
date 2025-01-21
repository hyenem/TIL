package modifier03_protected2;

import modifier03_protected.Person;

// 다른 패키지에 있는 클래스
// 상속을 받은 것은 : PersonTest2가 상속을 받은 것임
public class PersonTest2 extends Person { // extends를 하면 상속.
    public static void main(String[] args) {
        Person p = new Person();

        // 다른 클래스에 있으면 기본적으로는 안됨.
        //p.age =10; 
        
        // 상속을 받은 다음 그 상속을 받은 클래스를 통해서만 접근 가능.
        PersonTest2 p2 = new PersonTest2();
        p2.age =10;
        
    }
}
