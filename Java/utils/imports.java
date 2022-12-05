package Java.utils;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.ArrayList;

public class imports {

    public static List<String> import1d(Path path) {
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            e.printStackTrace();
        }
        throw new RuntimeException();
    }

    public static List<String[]> import2d(Path path, String separator) {
        try {
            List<String> list1d = import1d(path);
            List<String[]> list2d = new ArrayList<String[]>();
            for (String item : list1d) {
                String[] splitItem = item.split(separator);
                list2d.add(splitItem);
            }
            return list2d;

        } finally {
            System.out.print("An error occured");
        }
    }
}