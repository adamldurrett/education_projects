import java.io.*;
import java.util.Scanner;


public class JavaFormatter{

    private FileManager fileManager;
    private Scanner inputScanner;

    public JavaFormatter(){
        fileManager = new FileManager();
        inputScanner = new Scanner(System.in);
        promptForFile();
    }

    // Gets a file input from user, adds to list of opened files
    public void promptForFile(){
        System.out.println("Please type the name of the file you wish to have formatted:\n");
        if(fileManager.openFile(inputScanner.nextLine())){
            System.out.println("File opened successfully.");
        }
        else{
            System.out.println("File failed to open.");
        }
    }
    


}
