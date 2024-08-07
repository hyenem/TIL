import java.util.Arrays;

public class Array01_버블정렬 {
	public static void main(String[] args) {
		
		//배열의 초기화
		int[] arr = { 55, 7, 78, 12, 42};
		
		// 버블 정렬
		// i : 각 사이클마다 최대 데이터가 정렬될 위치
		for (int i = arr.length-1; i>=0; i--) {
			for (int j = 0; j<i; j++) {
				if (arr[j]>arr[j+1]) {
					int tmp = arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=tmp;
				}
			}
			System.out.println(Arrays.toString(arr));
		}
	}
}
