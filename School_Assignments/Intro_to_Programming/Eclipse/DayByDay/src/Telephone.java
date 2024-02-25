
public class Telephone {
    private static String number = "";
    static int quantity = 0;
    static double total = 0;
    
    public static String makeFullNumber (String telephoneNumber, int areaCode) {
        number = areaCode + "-" + telephoneNumber;
        return number;
    }
}
