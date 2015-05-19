import java.util.*;
import java.io.*;

public class FileRead {

	public static void main(String[] args) throws IOException {
		try(BufferedReader br = new BufferedReader(new FileReader(
			new String("/tmp/bla"))))  {
			List<String> allLines = new ArrayList<>();

			String line = br.readLine();
			while(line!=null) { 
				allLines.add(line);
				line = br.readLine();
			}

			int lineCount = 1;
			for(String line2 : allLines) { 
				System.out.println(String.valueOf(lineCount++) +
					 "->" + line2);
			}
		}
    }
}

