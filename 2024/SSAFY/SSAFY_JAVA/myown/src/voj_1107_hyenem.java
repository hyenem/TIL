import java.util.Scanner;
import java.util.Arrays;

public class voj_1107_hyenem {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int[] brokenButton = new int[M];
		
		for (int i = 0; i < M; i++) {
			brokenButton[i]=sc.nextInt();
		}
		
		int[] nonBrokenButton = new int[10-M];
		int point = 0;
		here : for (int i = 0; i<10; i++) {
			for (int j = 0; j<M; j++) {
				if (brokenButton[j]==i) {
					continue here;
				}
			}
			nonBrokenButton[point++]=i;
		}
		
		int nLength = 1;
		if (N!=0) {
			nLength = (int)(Math.log10(N)+1);
		} 
		
		int min = Math.abs(N-100);
		
		int searchArea = 1;
		int divide = 1;
		for (int i = 0; i<nLength+1; i++) {
			searchArea *= (10-M);
			divide *= 10;
		}
		
		for (int i=nLength+1; i>0; i--){
			for (int j=0; j<searchArea; j++) {
				for(int k=0; k<i; k++) {
					int nowNum = nonBrokenButton[j/divide]
				}
			}
		}
		
		System.out.print(min);
	}
}
