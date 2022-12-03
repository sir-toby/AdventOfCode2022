package Java;

import java.io.File; // Import the File class
import java.io.FileNotFoundException; // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;
import java.util.Comparator;

public class day01 {
  public static void main(String[] args) {
    String inputFileName = "./Inputs/01 Input.txt";
    ArrayList<String> inputFile = readFile(inputFileName);
    ArrayList<Integer> caloryList = getCaloryList(inputFile);
    printMaximumNCalories(caloryList, 1);
    printMaximumNCalories(caloryList, 3);
  }

  static ArrayList<Integer> getCaloryList(ArrayList<String> inputFile) {
    int calSum = 0;
    ArrayList<Integer> calList = new ArrayList<Integer>();

    for (String lines : inputFile) {
      if (lines == "") {
        calList.add(calSum);
        calSum = 0;
      } else {
        calSum += Integer.parseInt(lines);
      }
    }
    if (calSum != 0) {
      calList.add(calSum);
    }
    calList.sort(Comparator.reverseOrder());
    return calList;
  }

  static void printMaximumNCalories(ArrayList<Integer> calList, int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
      sum += calList.get(i);
    }
    System.out.println("Calories of the most carrying " + n + " elves: " + sum);
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