
public class Array2_버블정렬 {
	public static void main(String[] args) {
		
		int[] nums = {10, 64, 25, 11, 28, 77, 34};
		
	}
	
	static void selectionSort(int[] arr) {
		for(int i = 0; i<arr.length-1; i++) {
			int minIdx = i;
			for (int j = i; j<arr.length; j++) {
				if(arr[minIdx]>arr[j]) {
					minIdx=j;
				}
			}
			int tmp = arr[minIdx];
			arr[minIdx] = arr[i];
			arr[i]=tmp;
		}
	}
}
