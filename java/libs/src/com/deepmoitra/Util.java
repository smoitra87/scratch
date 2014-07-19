package com.deepmoitra;


import java.io.*;

public class Util {

        public static String getHostname() {
            String line = null;
            try {
                Runtime r = Runtime.getRuntime();
                Process p = r.exec("hostname");
                p.waitFor();
                BufferedReader b = new BufferedReader(new InputStreamReader(p.getInputStream()));
                line = b.readLine();
                b.close();
            } catch ( IOException|InterruptedException e) {
                e.printStackTrace();
                System.exit(1);
            }
            return line;
        }

        public static void main(String[] args)  {

               getHostname();
        }
}
