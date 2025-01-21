package test04_filter_stream;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class ScannerTest {
	public static void main(String[] args) {
		method2();
		method3();
	}
	
	private static void method3() {
		try (Scanner sc = new Scanner(new FileInputStream("big_input.txt"));
				){
			
			long start = System.nanoTime();
			while(sc.hasNext()) {
				int num = sc.nextInt();
			}
			long end = System.nanoTime();
			System.out.println(end - start);
		} catch (Exception e) {
			// TODO: handle exception
		}
	}

	public static void method2() {// 버퍼드 리더를 쓴 경우
		// 문자 스트림 : FileReader, FileWriter
		// 버퍼 기능을 추가해보자. : BufferedReader, BufferedWriter
		
		try(BufferedReader reader = new BufferedReader(new FileReader("big_input.txt"));
				BufferedWriter writer = new BufferedWriter(new FileWriter("big_input_2.txt"));
				) {
			
			String line; // BufferedReader은 입력을 줄 단위로 받는다.
			while ((line=reader.readLine())!=null) {
				writer.write(line);
				writer.newLine();
			}
			System.out.println("복사 끝.");
		} catch (IOException e) {
			// TODO: handle exception
		}
	}
	
	
}
