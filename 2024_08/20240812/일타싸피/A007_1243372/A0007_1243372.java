import java.net.*;
import java.util.HashMap;
import java.util.Map;
import java.io.*;

public class A0007_1243372 {

	// 닉네임을 사용자에 맞게 변경해 주세요.
	static final String NICKNAME = "A0007_1243372";

	// 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
	static final String HOST = "127.0.0.1";

	// 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
	static final int PORT = 1447;
	static final int CODE_SEND = 9901;
	static final int CODE_REQUEST = 9902;
	static final int SIGNAL_ORDER = 9908;
	static final int SIGNAL_CLOSE = 9909;

	// 게임 환경에 대한 상수입니다.
	static final int TABLE_WIDTH = 254;
	static final int TABLE_HEIGHT = 127;
	static final int NUMBER_OF_BALLS = 6;
	static final int[][] HOLES = { { 0, 0 }, { 127, 0 }, { 254, 0 }, { 0, 127 }, { 127, 127 }, { 254, 127 } };

	public static void main(String[] args) {

		Socket socket = null;
		String recv_data = null;
		byte[] bytes = new byte[1024];
		float[][] balls = new float[NUMBER_OF_BALLS][2];
		int order = 0;

		try {
			socket = new Socket();
			System.out.println("Trying Connect: " + HOST + ":" + PORT);
			socket.connect(new InetSocketAddress(HOST, PORT));
			System.out.println("Connected: " + HOST + ":" + PORT);

			InputStream is = socket.getInputStream();
			OutputStream os = socket.getOutputStream();

			String send_data = CODE_SEND + "/" + NICKNAME + "/";
			bytes = send_data.getBytes("UTF-8");
			os.write(bytes);
			os.flush();
			System.out.println("Ready to play!\n--------------------");

			while (socket != null) {
				// Receive Data
				bytes = new byte[1024];
				int count_byte = is.read(bytes);
				recv_data = new String(bytes, 0, count_byte, "UTF-8");
				System.out.println("Data Received: " + recv_data);

				// Read Game Data
				String[] split_data = recv_data.split("/");
				int idx = 0;
				try {
					for (int i = 0; i < NUMBER_OF_BALLS; i++) {
						for (int j = 0; j < 2; j++) {
							balls[i][j] = Float.parseFloat(split_data[idx++]);
						}
					}
				} catch (Exception e) {
					bytes = (CODE_REQUEST + "/" + CODE_REQUEST).getBytes("UTF-8");
					os.write(bytes);
					os.flush();
					System.out.println("Received Data has been currupted, Resend Requested.");
					continue;
				}

				// Check Signal for Player Order or Close Connection
				if (balls[0][0] == SIGNAL_ORDER) {
					order = (int)balls[0][1];
					System.out.println("\n* You will be the " + (order == 1 ? "first" : "second") + " player. *\n");
					continue;
				} else if (balls[0][0] == SIGNAL_CLOSE) {
					break;
				}

				// Show Balls' Position
				for (int i = 0; i < NUMBER_OF_BALLS; i++) {
					System.out.println("Ball " + i + ": " + balls[i][0] + ", " + balls[i][1]);
				}

				float angle = 0.0f;
				float power = 0.0f;

				//////////////////////////////
				// 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
				//
				// 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
				//   - order: 1인 경우 선공, 2인 경우 후공을 의미
				//   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
				//     예) balls[0][0]: 흰 공의 X좌표
				//         balls[0][1]: 흰 공의 Y좌표
				//         balls[1][0]: 1번 공의 X좌표
				//         balls[4][0]: 4번 공의 X좌표
				//         balls[5][0]: 마지막 번호(8번) 공의 X좌표

				// 여기서부터 코드를 작성하세요.
				// 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

				float ballRadius = 2.865f;

				// whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
				float whiteBall_x = balls[0][0];
				float whiteBall_y = balls[0][1];

				// blackBall_x, blackBall_y: 검정 공의 X, Y좌표를 나타내기 위해 사용한 변수
				float blackBall_x = balls[5][0];
				float blackBall_y = balls[5][1];

				// 검정공을 칠 수도 있는 위험반경을 미리 계산함.
				float dangerMinAngle = angle(whiteBall_x, whiteBall_y, blackBall_x, blackBall_y)
						-(float)Math.asin(2*ballRadius/distance(whiteBall_x,whiteBall_y, blackBall_x, blackBall_y));
				float dangerMaxAngle = angle(whiteBall_x, whiteBall_y, blackBall_x, blackBall_y)
						+(float)Math.asin(2*ballRadius/distance(whiteBall_x,whiteBall_y, blackBall_x, blackBall_y));

				// 어떤 공을 우선으로 칠지 결정하기 위한 targetBall 번호 변수
				int targetBallNum = 0;
				//목적구가 결정되었는지를 확인하기 위한 변수

				float targetBall_x=0;
				float targetBall_y=0;
				int holeNum;
				double holeDistance;
				int goalAmount = 0;


				int target1;
				int target2;
				int notarget1;
				int notarget2;
				if(order==1) {
					target1 = 1;
					target2 = 3;
					notarget1 = 2;
					notarget2 = 4;
				} else {
					target1 = 2;
					target2 = 4;
					notarget1 = 1;
					notarget2 = 3;
				}

				float[][] angleArr = new float[6][3];
				for (int i =1 ;i<6; i++) {
					angleArr[i][0]=angle(whiteBall_x, whiteBall_y, balls[i][0], balls[i][1]);
					angleArr[i][1]=angle(whiteBall_x, whiteBall_y, balls[i][0], balls[i][1])
							-(float)Math.asin(2*ballRadius/distance(whiteBall_x,whiteBall_y, balls[i][0], balls[i][1]));
					angleArr[i][2]=angle(whiteBall_x, whiteBall_y, balls[i][0], balls[i][1])
							+(float)Math.asin(2*ballRadius/distance(whiteBall_x,whiteBall_y, balls[i][0], balls[i][1]));
				}

				if(balls[target1][0]==-1) goalAmount++;
				if(balls[target2][0]==-1) goalAmount++;



				// 만약 검정 공만 남았다면 
				if(goalAmount==2) {
					targetBallNum = 5;
					targetBall_x = balls[targetBallNum][0];
					targetBall_y = balls[targetBallNum][1];

					holeDistance = Double.MAX_VALUE;
					for(int searchHole = 0; searchHole<6; searchHole++) {
						float hole_x = HOLES[searchHole][0];
						float hole_y = HOLES[searchHole][1];
						// 같은 사분면에 있는지 판단
						if(((hole_x-whiteBall_x)*(targetBall_x-whiteBall_x)>=0)&&((hole_y-whiteBall_y)*(targetBall_y-whiteBall_y)>=0)){
							// 거리 측정해서 기존 거리보다 더 작으면
							// 맞출 각도를 계산하고
							// 가는 길에 검정공이 있는지 채크
							if(holeDistance>Math.sqrt(Math.pow(targetBall_x - hole_x, 2) + Math.pow(targetBall_y - hole_y, 2))) {
								//각도 계산하기
								//								if(angle(targetBall_x, targetBall_y, hole_x, hole_y)-angle(targetBall_x, targetBall_y, whiteBall_x, whiteBall_y)) {
								//									
								//								}
								float goal_x = (float) (targetBall_x-(((hole_x-targetBall_x)/distance(targetBall_x, targetBall_y, hole_x, hole_y))*2*ballRadius));
								float goal_y = (float) (targetBall_y-(((hole_y-targetBall_y)/distance(targetBall_x, targetBall_y, hole_x, hole_y))*2*ballRadius));
								float tmpangle = angle(whiteBall_x, whiteBall_y, goal_x, goal_y);

//								if(issafe(angle, angleArr[notarget1][1], angleArr[notarget1][2])&&issafe(angle, angleArr[notarget2][1], angleArr[notarget2][2])) {
									//위험 범위 안에 들어 있을때는 값을 업데이트 하지 않음.
									holeNum = searchHole;
									holeDistance = Math.sqrt(Math.pow(targetBall_x - hole_x, 2) + Math.pow(targetBall_y - hole_y, 2));
									angle = tmpangle;
//								}
							}
						}
					}
				}else if(goalAmount == 0) {
					targetBallNum = target1;
					targetBall_x = balls[targetBallNum][0];
					targetBall_y = balls[targetBallNum][1];

					holeDistance = Double.MAX_VALUE;
					for(int searchHole = 0; searchHole<6; searchHole++) {
						float hole_x = HOLES[searchHole][0];
						float hole_y = HOLES[searchHole][1];
						// 같은 사분면에 있는지 판단
						if(((hole_x-whiteBall_x)*(targetBall_x-whiteBall_x)>=0)&&((hole_y-whiteBall_y)*(targetBall_y-whiteBall_y)>=0)){
							// 거리 측정해서 기존 거리보다 더 작으면
							// 맞출 각도를 계산하고
							// 가는 길에 검정공이 있는지 채크
							if(holeDistance>Math.sqrt(Math.pow(targetBall_x - hole_x, 2) + Math.pow(targetBall_y - hole_y, 2))) {
								//각도 계산하기
								float goal_x = (float) (targetBall_x-(((hole_x-targetBall_x)/distance(targetBall_x, targetBall_y, hole_x, hole_y))*2*ballRadius));
								float goal_y = (float) (targetBall_y-(((hole_y-targetBall_y)/distance(targetBall_x, targetBall_y, hole_x, hole_y))*2*ballRadius));
								float tmpangle = angle(whiteBall_x, whiteBall_y, goal_x, goal_y);

//								if(issafe(angle, angleArr[notarget1][1], angleArr[notarget1][2])
//										&&issafe(angle, angleArr[notarget2][1], angleArr[notarget2][2])
//										&&issafe(angle, angleArr[5][1], angleArr[5][2])) {
//									//위험 범위 안에 들어 있을때는 값을 업데이트 하지 않음.
									holeNum = searchHole;
									holeDistance = Math.sqrt(Math.pow(targetBall_x - hole_x, 2) + Math.pow(targetBall_y - hole_y, 2));
									angle = tmpangle;
//								}
							}
						}
					} 
				}else {
					targetBallNum = target2;
					targetBall_x = balls[targetBallNum][0];
					targetBall_y = balls[targetBallNum][1];

					holeDistance = Double.MAX_VALUE;
					for(int searchHole = 0; searchHole<6; searchHole++) {
						float hole_x = HOLES[searchHole][0];
						float hole_y = HOLES[searchHole][1];
						// 같은 사분면에 있는지 판단
						if(((hole_x-whiteBall_x)*(targetBall_x-whiteBall_x)>=0)&&((hole_y-whiteBall_y)*(targetBall_y-whiteBall_y)>=0)){
							// 거리 측정해서 기존 거리보다 더 작으면
							// 맞출 각도를 계산하고
							// 가는 길에 검정공이 있는지 채크
							if(holeDistance>Math.sqrt(Math.pow(targetBall_x - hole_x, 2) + Math.pow(targetBall_y - hole_y, 2))) {
								//각도 계산하기
								//										if(angle(targetBall_x, targetBall_y, hole_x, hole_y)-angle(targetBall_x, targetBall_y, whiteBall_x, whiteBall_y)) {
								//											
								//										}
								float goal_x = (float) (targetBall_x-(((hole_x-targetBall_x)/distance(targetBall_x, targetBall_y, hole_x, hole_y))*2*ballRadius));
								float goal_y = (float) (targetBall_y-(((hole_y-targetBall_y)/distance(targetBall_x, targetBall_y, hole_x, hole_y))*2*ballRadius));
								float tmpangle = angle(whiteBall_x, whiteBall_y, goal_x, goal_y);

//								if(issafe(angle, angleArr[notarget1][1], angleArr[notarget1][2])
//										&&issafe(angle, angleArr[notarget2][1], angleArr[notarget2][2])
//										&&issafe(angle, angleArr[5][1], angleArr[5][2])) {
									//위험 범위 안에 들어 있을때는 값을 업데이트 하지 않음.
									holeNum = searchHole;
									holeDistance = Math.sqrt(Math.pow(targetBall_x - hole_x, 2) + Math.pow(targetBall_y - hole_y, 2));
									angle = tmpangle;
//								}
							}
						}
					}
				}


				// power: 거리 distance에 따른 힘의 세기를 계산
//				power = (float) distance(whiteBall_x, whiteBall_y, targetBall_x, targetBall_y)*2/3 + Math.abs(angleArr[targetBallNum][0]-angle)*1/10;
				power = 80f;




				// 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
				// 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
				//   - angle: 흰 공을 때려서 보낼 방향(각도)
				//   - power: 흰 공을 때릴 힘의 세기
				// 
				// 이 때 주의할 점은 power는 100을 초과할 수 없으며,
				// power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
				//
				// 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
				//////////////////////////////

			
				String merged_data = angle + "/" + power + "/";
				bytes = merged_data.getBytes("UTF-8");
				os.write(bytes);
				os.flush();
				System.out.println("Data Sent: " + merged_data);
			}

			os.close();
			is.close();
			socket.close();
			System.out.println("Connection Closed.\n--------------------");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// 두 점 사이의 거리를 계산하는 메서드
	static double distance(float x1, float y1, float x2, float y2) {
		return Math.sqrt(Math.pow(x1-x2, 2)+Math.pow(y1-y2, 2));
	}

	// y축의 양의 방향을 기준으로 반시계 방향으로 각도 계산하기
	// (x1, y1)을 기준점으로 측정
	static float angle(float x1, float y1, float x2, float y2) {
		double tmpangle = Math.atan((x2-x1)/(y2-y1));
		if((x2-x1>0)&&(y2-y1<0)) tmpangle+=Math.PI;
		else if((x2-x1<0)&&(y2-y1<0)) tmpangle+=Math.PI;
		else if((x2-x1<0)&&(y2-y1>0)) tmpangle+=2*Math.PI;
		return (float) Math.toDegrees(tmpangle);
	}

	static boolean issafe(float now, float min, float max) {
		if(min<0) {
			if(now>min+359 || now<max+1) return false;
		} else if (max>360) {
			if(now<max-361 || now>min-1) return false;
		} else {
			if(now>min-1 && now<max+1) return false;
		}	
		return true;
	}
}
