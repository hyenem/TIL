package test05_object_serialzation;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;

public class SerialiazationTest4 {
	public static void main(String[] args) {
		List<Person> list = new ArrayList()<>();
		list.add(new Person("daisy", 3));
		list.add(new Person("Max", 4));
		
		try(ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("lis.dat"))) {
			
		}
	}
}
