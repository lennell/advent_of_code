

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Day1b {

    public static void main(String[] args) throws IOException {
        System.out.println("Day 1b");
        int i = 0;
        List<String> lines = Files.readAllLines(Path.of("src/input1.txt"));
        int pass = 50;
        for (String line : lines) {
            String l = line.substring(0,1);
            int newFigure = Integer.parseInt(line.substring(1,line.length()));

            newFigure = newFigure%100;
            System.out.println("yyy " + newFigure);
           if (l.equals("L")) {
              pass =  pass  - newFigure;
              if (pass < 0) {
                  pass = 100 + pass;
              }
            } else if (l.equals("R")) {
               pass =  pass  + newFigure;
               if (pass >= 100) {
                   pass =  pass  -100;
               }
            }
            System.out.println("a"+pass);

           if (pass==0) {
               i++;
           }
        }

        System.out.println("Final Password: " + i);



    }
}
