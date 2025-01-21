package 분할정복;

public class 이진검색01_반복 {
	public static void main(String[] args) {
		int[] arr = {8,9, 17, 21, 23, 35, 88, 369};
		
		System.out.println(binarySearch(arr, 19));
	}
	
	static boolean binarySearch(int[] arr, int key) {
		int left = 0;
		int right = arr.length -1;
		
		while (left<=right) {
			int mid = (left+right)/2;
			// 인트 범위 벗어날 수도 있으니까 조심할 것
			
			if(arr[mid]==key) return true;
			else if(arr[mid]==key) right = mid -1;
			else left = mid + 1;
		}
		
		return false;
	}
}
