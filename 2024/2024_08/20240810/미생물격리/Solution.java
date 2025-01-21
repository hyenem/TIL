package 미생물격리;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case=1; test_case<T+1; test_case++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			int K = sc.nextInt();
			// 미생물 정보 저장을 위한 리스트
			// 미생물이 합쳐지면 하나를 제거하기 위해서 배열이 아니라 리스트로 다룸
			List<int[]> list = new ArrayList<int[]>();
			for (int i = 0; i<K; i++) {
				int[] arr = new int[4];
				for (int j=0; j<4; j++) {
					arr[j]=sc.nextInt();
				}
				list.add(arr);
			}
			
			//M개의 라운드를 진행
			for (int i =0; i<M; i++) {
				// 이동하기
				for (int j = 0; j<list.size() ;j++) {
					if(list.get(j)[3]==1) list.get(j)[0]--;
					else if(list.get(j)[3]==2) list.get(j)[0]++;
					else if(list.get(j)[3]==3) list.get(j)[1]--;
					else if(list.get(j)[3]==4) list.get(j)[1]++;
				}
				
				//같으면 합치기
				//뒤에서 부터 가면
				//지울때 뒤에껄 지워야할듯
				for(int j=0; j<list.size(); j++) {
					// 여러개가 동시에 합쳐질 수도 있으니까 우선 제일 큰 쪽으로 방향부터 바꾸고
					int maxidx = j;
					for (int k = list.size()-1; k>=j+1; k--) {
						if(list.get(k)[0]==list.get(j)[0] && list.get(k)[1]==list.get(j)[1]) {
							if(list.get(maxidx)[2]<list.get(k)[2]) maxidx=k;
						}
					}
					list.get(j)[3]=list.get(maxidx)[3];
					
					// 그 다음에 제일 작은 쪽으로 숫자 합쳐주고
					// 합쳐진 아이들은 삭제해주기
					for (int k = list.size()-1; k>=j+1; k--) {
						if(list.get(k)[0]==list.get(j)[0] && list.get(k)[1]==list.get(j)[1]) {
							list.get(j)[2]+=list.get(k)[2];
							list.remove(k);
						}
					}
				}
				
				// 약품처리 구간 만나면 방향 바꾸고 개수 줄어들기
				for(int j = 0; j<list.size(); j++) {
					if(list.get(j)[0]==0 || list.get(j)[0]==N-1 || list.get(j)[1]==0 || list.get(j)[1]==N-1) {
						list.get(j)[2]/=2;
						if(list.get(j)[3]==1) list.get(j)[3]=2;
						else if(list.get(j)[3]==2) list.get(j)[3]=1;
						else if(list.get(j)[3]==3) list.get(j)[3]=4;
						else if(list.get(j)[3]==4) list.get(j)[3]=3;
						if(list.get(j)[2]==0) list.remove(j);
					}
				}
			}
			
			int ans = 0;
			for(int i = 0; i<list.size(); i++) {
				ans += list.get(i)[2];
			}
			
			System.out.println("#"+test_case+" "+ans);
		}
	}
}
