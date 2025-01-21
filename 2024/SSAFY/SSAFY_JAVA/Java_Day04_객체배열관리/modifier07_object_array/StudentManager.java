package modifier07_object_array;

public class StudentManager {
	// Student 의 배열을 가지고 있는 객체
	// => 1개의 객체만 생성하면 됨 => 싱글턴으로 만든다.
	
	private Student[] arr = new Student[100];
	private int size = 0; // 실제 들어있는 개수
	
	private static StudentManager instance = new StudentManager();
	
	private StudentManager() {}
	
	public StudentManager getInstance() {
		return instance;
	}
	
	public void addStudent(Student st) {
		if (size<100) {
			arr[size]=st;
			size++;
		} else {
			System.out.println("더 이상의 학생을 추가할 수 없습니다.");
		}
	}
	
	
    
}
