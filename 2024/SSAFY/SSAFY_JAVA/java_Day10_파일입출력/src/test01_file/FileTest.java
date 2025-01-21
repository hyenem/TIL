package test01_file;

import java.io.File;

public class FileTest {
	public static void main(String[] args) {
		// File : 파일 & 디렉토리 관리하기 위한 클래스
		File f = new File("dog.jpg"); // 상대경로를 쓰고있다.
		System.out.println(f.exists());
		System.out.println(f.isFile());
		System.out.println(f.isAbsolute());
		System.out.println(f.getAbsolutePath());
		System.out.println(f.length()+"byte.");
		
		File src = new File("src");
		System.out.println(src.exists());
		System.out.println(src.isDirectory());
		
		File folder = new File("folder");
		System.out.println(folder.exists());
		folder.mkdir();
	}
}
