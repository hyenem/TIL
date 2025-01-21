package test04_finally;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class ExceptionTest2 {
	public static void main(String[] args) {
		// try ~ catch~finally => try with resources
		
		FileInputStream fis = null;
		//왜 try 밖에서 정의해줬냐면
		
		try {
			// 이 블록 안에서 선언된 변수 => 이 블록 안에서만 슬 수 있음
			fis = new FileInputStream("text.txt");
		} catch (FileNotFoundException e) {
			System.out.println("예외가 발생했어요.");
		} finally {
			try {	
				if(fis != null) {
				fis.close();
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		try(FileInputStream fis2 = new FileInputStream("test.txt")){
			
		} catch(IOException e) {
			System.out.println("예외가 발생했어요");
		}
	}
	
}
