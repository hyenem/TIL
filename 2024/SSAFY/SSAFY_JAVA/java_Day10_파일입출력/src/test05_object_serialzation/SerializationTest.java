package test05_object_serialzation;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class SerializationTest {
	public static void main(String[] args) {
		Person p = new Person("luna", 5);
		Student s = new Student("max", 3, "java");
		
		// 객체 => 파일에 저장
		try(ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("luna.dat"))){
			oos.writeObject(p);
			oos.writeObject(s);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
