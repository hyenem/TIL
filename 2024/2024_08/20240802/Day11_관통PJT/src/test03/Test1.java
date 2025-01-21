package test03;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

import com.google.gson.Gson;

public class Test1 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("data/refrigerator.json")));
		String str = null; // 한줄씩 읽어오기 위한 임시변수
		StringBuilder sb = new StringBuilder();
		while ((str = br.readLine())!=null) {
			sb.append(str);
		}
		// 이 while문을 빠져나오면 sb에는 모든 문자열이 저장되어 있음.
		
		Gson gson = new Gson();
		Refrigerator[] arr = gson.fromJson(sb.toString(), Refrigerator[].class);
		
		System.out.println(Arrays.toString(arr));
		
		arr[0].setCategory("김치냉장고");
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("data/ref-copy.json")));
		String str2 = gson.toJson(arr);
		bw.write(str2);
		bw.close();
	}
}
