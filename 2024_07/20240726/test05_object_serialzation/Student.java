package test05_object_serialzation;

public class Student extends Person{
	private String major;
	
	public Student() {
		// TODO Auto-generated constructor stub
	}

	public Student(String name, int age, String major) {
		super(name, age);
		this.major = major;
	}

	public String getMajor() {
		return major;
	}

	public void setMajor(String major) {
		this.major = major;
	}

	@Override
	public String toString() {
		return "Student [major=" + major + ", getMajor()=" + getMajor() + "]";
	}
	
	
}
