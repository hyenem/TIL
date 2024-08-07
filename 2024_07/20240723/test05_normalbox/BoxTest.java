package test05_normalbox;

class Box{
	private Object obj;
	public Object getObj() {
		return obj;
	}
	public void setObj(Object obj) {
		this.obj = obj;
	}
}

public class BoxTest {
	public static void main(String[] args) {
		Box box = new Box(); // 아무거나 다 들어갈 수 있는 박스
		
		box.setObj(11);
		box.setObj("Hello");
		box.setObj(41.22);
		
		Object obj = box.getObj();
		// 값을 사용하기 위해서는 일일이 형 변환 해줘야한다.
		if (obj instanceof Double) {
			System.out.println("실수형의 값입니다: "+box.getObj());
			Double d = (Double) box.getObj();
		}
	}
}
