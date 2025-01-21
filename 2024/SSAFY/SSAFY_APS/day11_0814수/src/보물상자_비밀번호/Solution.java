package 보물상자_비밀번호;

import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Set;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case<=T; test_case++) {
			int N = sc.nextInt();
			int K = sc.nextInt();
			LinkedList<Character> queue = new LinkedList<>();
			String str = sc.next();
			for (int i = 0; i<N; i++) {
				queue.add(str.charAt(i));
			}
			Set<Integer> list = new HashSet<>();
			for(int i = 0; i<N/4; i++) {
				for(int j = 0; j<4; j++) {
					int nowNum =0;
					String nowstr = "";
					for(int k = 0; k<N/4; k++) {
						char nowChar = queue.get(0);
						nowstr+=nowChar;
						queue.remove(0);
						if(nowChar=='A'||nowChar=='B'||nowChar=='C'
								||nowChar=='D'||nowChar=='E'||nowChar=='F') {
							nowNum = nowNum*16 + nowChar-'A'+10;
						} else {
							nowNum = nowNum*16+ nowChar-'0';
						}
						queue.add(nowChar);
					}
					list.add(nowNum);
					
				}
				char switchChar = queue.get(queue.size()-1);
				queue.remove(queue.size()-1);
				queue.addFirst(switchChar);
			}

			Object[] arr = list.toArray();
			Arrays.sort(arr);
			
			System.out.println("#"+test_case+" "+((Integer)arr[arr.length-K]).intValue());
		}
	}
}
