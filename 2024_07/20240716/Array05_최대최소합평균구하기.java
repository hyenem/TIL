package java_Day02_배열;

public class Array05_최대최소합평균구하기 {
	public static void main(String[] args) {
		int[] nums = {53, 211, 11, 66, 84, 132, 12};
		
		// 최대, 최소, 합, 평균
		// 1. 최댓값 구하기: 최댓값을 담을 임시 변수를 아주 작은 값으로 설정 | 첫번째 값으로 설정해놓고,
		// 2. 반복문을 돌면서 비교한다.
		
		// 1. 첫번째 값을 최대로 가정한다.
		int max = nums[0];
		int min = nums[0];
		int sum = nums[0];
		
		// 2. 배열의 두번째값부터 비교하면서 더 큰게 있다면 업데이트한다.
		for (int i = 1; i < nums.length; i++) {
			if (nums[i] > max) {
				max = nums[i];
			}
			if (nums[i]<min) {
				min=nums[i];
			}
			sum += nums[i];
		}
		
		System.out.println(max);
		System.out.println(min);
		System.out.println(sum);
		
		double avg = (double)sum / nums.length;
		System.out.printf("%2.2f",avg);
	}
}
