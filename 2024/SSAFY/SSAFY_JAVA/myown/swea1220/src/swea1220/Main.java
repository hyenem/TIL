package swea1220;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		for (int T = 1; T < 101; T++) {
			Scanner sc = new Scanner(System.in);
			int N = sc.nextInt();
			int[][] arr = new int[N][N];
			for (int i = 0 ; i<N; i++) {
				for (int j =0; j<N; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			
			int ans = 0;
			for (int j = 0; j<N; j++) {
				int count = 0;
				for (int i = 0; i<N; i++) {
					if (count%2==0 && arr[i][j]==1) {
						count++;
					} else if (count%2==1 && arr[i][j]==2) {
						count ++;
					}
				}
				ans += count/2;
			}
			System.out.println("#"+T+" "+ans);
		}
		
	}
}
