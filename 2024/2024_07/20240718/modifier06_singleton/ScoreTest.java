package modifier06_singleton;

public class ScoreTest {
    public static void main(String[] args) {
    	
//    	ScoreManager sm = new ScoreManager();// 생성자를 private로 막아놨기 때문에 객체를 생성해서 쓸 수 없음
    	
    	// 객체는 getInstance static 메서드를 이용해서 가져온다ㅑ.
    	ScoreManager sm1 = ScoreManager.getInstance();
    	ScoreManager sm2 = ScoreManager.getInstance();

    	System.out.println(sm1==sm2);
    	// 유일한 1개의 객체임을 보장할 수 있다.
    }
}
