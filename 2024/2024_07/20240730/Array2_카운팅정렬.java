import java.util.Arrays;

public class Array2_카운팅정렬 {
	public static void main(String[] args) {
		int[] arr = {1,54, 5,6,2,9,1,2,22, 16};
		int[] newarr = countingSort(arr);
		System.out.println(Arrays.toString(newarr));
		
	}
	
	static int[] countingSort(int[] arr) {
		int max = 0;
		int[] newarr = new int[arr.length];
		for (int i = 0; i<arr.length; i++) {
			max = Math.max(max, arr[i]);
		}
		
		int[] count = new int[max+1];
		for (int i = 0; i<arr.length; i++) {
			count[arr[i]]++;
		}
		
		int[] acc = new int[max+1];
		acc[0]=count[0];
		for (int i = 1; i<max+1; i++) {
			acc[i]=acc[i-1]+count[i];
		}
		
		for (int i = arr.length-1; i>=0; i--) {
			newarr[--acc[arr[i]]]=arr[i];
		}
		return newarr;
	}
}
