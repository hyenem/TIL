package swea3499;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		end: for(int test_case = 1; test_case <= T; test_case++)
		{
			String str = sc.next();
            int S = str.length()/3;
            boolean[] s1 = new boolean[13];
            boolean[] s2 = new boolean[13];
            boolean[] s3 = new boolean[13];
            boolean[] s4 = new boolean[13];
            for (int i =0; i<S; i++){
                char shape = str.charAt(i*3);
                int num = (str.charAt(i*3+1)-'0')*10 + (str.charAt(i*3+2)-'0')-1;
				if(shape=='S') {
                    if(s1[num]){
                        System.out.println("#"+test_case+" ERROR");
                        continue end;
                    } else {
	                    s1[num]=true;
                    }
                }
               if(shape=='D') {
                    if(s2[num]){
                        System.out.println("#"+test_case+" ERROR");
                        continue end;
                    } else {
	                    s2[num]=true;
                    }
                }
                if(shape=='H') {
                    if(s3[num]){
                        System.out.println("#"+test_case+" ERROR");
                        continue end;
                    } else {
	                    s3[num]=true;
                    }
                }
                if(shape=='C') {
                    if(s4[num]){
                        System.out.println("#"+test_case+" ERROR");
                        continue end;
                    } else {
	                    s4[num]=true;
                    }
                }
            }
            
            int sum1 =0;
            int sum2 =0;
            int sum3 =0;
            int sum4 = 0;
            
            for(int i = 0; i<13; i++){
                if(!s1[i]) sum1++;
                if(!s2[i]) sum2++;
                if(!s3[i]) sum3++;
                if(!s4[i]) sum4++;
            }
            System.out.println("#"+test_case+" "+sum1+" "+sum2+" "+sum3+" "+sum4);
		}

	}
}
