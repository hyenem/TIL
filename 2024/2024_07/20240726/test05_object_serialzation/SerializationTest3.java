package test05_object_serialzation;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

public class SerializationTest3 {
	public static void main(String[] args) {
		//파일 => 객체
		try(ObjectInputStream ois = new ObjectInputStream(new FileInputStream("luna.dat"))){
			Object obj = ois.readObject(); // 실제 해당 클래스의 객체로 만들어주는데, 박스만 Object.
			System.out.println(obj);
		} catch (IOException | ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			// 에러 발생!!!
			// 왜 역질렬화가 안될까?
			// Person 설계도를 수정했기 때문에
		}
	}
}
