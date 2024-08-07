package test04_filter_stream;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class InputTest {
	public static void main(String[] args) throws NumberFormatException, IOException {
		// 만약에 파일을 통해서 입력을 받으라고 한다면?
//		System.setIn(new FileInputStream("input.txt"));
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("input.txt")));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] nums = new int[N];
		for (int i = 0; i<N; i++) {
			nums[i] = Integer.parseInt(br.readLine());
		}
		
		System.out.println(Arrays.toString(nums));
	}
}
