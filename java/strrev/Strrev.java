import java.util.*;

public class Strrev {

	public static void main(String[] args) {
		String s = "Hello World";
		System.out.println(reverseString(s));

	}


	public static String reverseString(String s) {
		char[] charArr = s.toCharArray();
		for(int i = 0 ; i < s.length()/2 ; i++) {
			char temp = charArr[i];
			charArr[i] = charArr[s.length()-i-1];
			charArr[s.length()-i-1] = temp;
		}
		return new String(charArr);
	}
}
