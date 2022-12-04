package Java;

import java.io.File; // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;

public class day03 {
    public static void main(String[] args) {
        String inputFileName = "./Inputs/03 Input.txt";
        ArrayList<String> rucksackList = readFile(inputFileName);
        part1(rucksackList);
        //part2(rucksackList);
    }

    static void part1(ArrayList<String> rucksackList) {
        int prioSum = 0;
        for (String rucksack : rucksackList) {
            prioSum += getValue(getDuplicateLetter(rucksack));
        }
        System.out.print("Prio of duplicate letters: " + prioSum);
    }

/*
    static void part2(ArrayList<String> rucksackList) {
        int prioSum = 0;
        for (int i=0; i<rucksackList.size(); i+=3) {
            String[] elfGroup = {"", "", ""};
            for (int j=0; j<3; j++) {
                elfGroup[j] = rucksackList.get(i+j);
            }
            for 
        }
    }
*/
    static char getDuplicateLetter(String rucksack) {
        String comp1 = (rucksack.substring(0, (int) rucksack.length() / 2));
        String comp2 = rucksack.substring((int) rucksack.length() / 2);
        for (int i = 0; i < comp1.length() + 1; i++) {
            if (comp2.indexOf(comp1.charAt(i)) != -1) {
                return comp1.charAt(i);
            }
        }
        return comp1.charAt(1); // Unclean - try catch?
    }

    static int getValue(char character) {
        if (Character.isUpperCase(character)) {
            return ((int) character - 64) + 26;
        } else if (Character.isLowerCase(character)) {
            return (int) character - 96;
        } else
            return 0;
    }

    static ArrayList<String> readFile(String inputFileName) {
        ArrayList<String> inputList = new ArrayList<String>();
        try {
            File myObj = new File(inputFileName);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                inputList.add(myReader.nextLine());
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return inputList;
    }
}