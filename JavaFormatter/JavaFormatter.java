import java.io.*;
import java.util.Scanner;


public class JavaFormatter{

    private FileManager fileManager;
    private Scanner inputScanner;

    public JavaFormatter(){
        fileManager = new FileManager();
        inputScanner = new Scanner(System.in);
        fileManager.promptForFile();
        promptForInput();
    }

    // polls user for input, decides next action based on that.
    private void promptForInput(){
        boolean done = false;

        while(!done){
            System.out.println("What would you like to do with your files?");
            System.out.println(" 1. autoformat        -- af");
            System.out.println(" 2. rename variables  -- rfv");
            System.out.println(" -- ");

            String userInput = inputScanner.nextLine();

            switch(userInput){
                case "af":
                    done = true;
                    break;
                case "AF":
                    done = true;
                    break;
                case "autoformat":
                    done = true;
                    break;
                default:
                    System.out.println("Please enter a valid input.");
            }
        }
    }

    public void formatFiles(){
        
    }


}
