import java.util.Arrays;

public class zigzag {
	public static void main(String[] args) {
		int[][] arr = new int[3][3];

		int num =1;
		for (int r =0; r<arr.length; r++) {
			for (int c =0; c<arr[r].length; c++) {
				arr[r][c] = num++;
			}
		}
		
		System.out.println(Arrays.deepToString(arr));
		
		for(int r = 0; r<arr.length; r++) {
			for (int c=arr[r].length-1; c>=0; c--) {
				System.out.print(arr[r][c]+", ");
			}
			System.out.println();
		}
	}
}
