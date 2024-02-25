
public class Person {
	int birthYear;
	String name;
	String address;
	
	Person() {	
	}
	
	private Person(String newName, String newAddress) {
		name = newName;
		address = newAddress;
	}
	
	public void eat() {
		
	}
	
	public void sleep() {

	}
	
	public int getAge() {
		return 2022 - birthYear;
	}
	
	public String getInfo() {
		return String.format("%s %s", name, address);
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String newName) {
		name = newName;
	}
	
	public String getAddress() {
		return address;
	}
	
	public void setAddress(String newAddress) {
		address = newAddress;
	}
	
	public int getBirthYear() {
		return birthYear;
	}
	
	public void setBirthYear(int newBirthYear) {
		birthYear = newBirthYear;
	}
	
}
