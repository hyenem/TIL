package pkg1;

//import pkg1.pkg2.Person;

public class PersonTest {
    public static void main(String[] args) {
        
    	Person p = new Person();
    	System.out.println(p.pkg);
    	
    	pkg1.pkg2.Person p2 = new pkg1.pkg2.Person();
    	System.out.println(p2.pkg);
    	
    }
}
