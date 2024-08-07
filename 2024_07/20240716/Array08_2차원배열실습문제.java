package java_Day02_배열;

public class Array08_2차원배열실습문제 {
	public static void main(String[] args) {
		int[][] grid = {{2,3,1,4,7},{8,13,3,33,1},{7,4,5,80,12},{17,9,11,5,4},{4,5,91,27,7}};

		int count = 0; // 개수 저장 변수
		int sum = 0;  // 합 저장 변수
		
		for (int row = 0; row<5; row++) {
			for (int col = 0; col<5; col++) {
				if (grid[row][col]%3 ==0) {
					count++;
					sum += grid[row][col];
				}
			}
		}
		
		System.out.println(count);
		System.out.println(sum);
		
		count = 0; // 개수 저장 변수
		sum = 0;  // 합 저장 변수
		
		out: for (int row = 0; row<5; row++) {
			for (int col = 0; col<5; col++) {
				if (grid[row][col]%3 !=0) {
					continue out;
				}
				
				//coutinue: 2,2 => 2,3
				//coutinue out: 2,2 => 3,0
				
				// coutinue;는 해당 반복문 안에서 contimue 밑에 내용을 수행하지 않고
				// 바로 다음 반복으로 넘어간다.
				
				// break
				// 해당 반복을 종료
				count++;
				sum += grid[row][col];
			}
		}
		
		System.out.println(count);
		System.out.println(sum);
	}
}
