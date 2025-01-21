import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case <T+1; test_case++) {
			
			int N = sc.nextInt();
			int[] arr = new int[N];
			int[] maxArr = new int[N+1];
			int point = 1;
			
			for (int i = 0; i<N; i++) {
				arr[i]=sc.nextInt();
			}
			
			for (int i = 0; i<N; i++) {
				int count = 0;
				for (int j = i+1; j<N; j++) {
					if (arr[i]<arr[j]) {
						count++;
					}
					if (count == 0) {
						maxArr[point++]=i;
					}
				}
			}
			int ans = 0;
			for (int i = 1; i<point; i++) {
				int res = 0;
				for (int j = maxArr[i-1]; j<maxArr[i]; j++) {
					res -= arr[j];
				}
				res += arr[maxArr[i]]*(maxArr[i]-maxArr[i-1]+1);
				if (res > 0) {
					ans +=res;
				}
			}
			System.out.println(Arrays.toString(maxArr));
			System.out.println("#"+test_case+" "+ans);
		}
	}
}
