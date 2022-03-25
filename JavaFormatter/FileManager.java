import java.util.*;
import java.io.*;


public class FileManager{

    ArrayList<Scanner> fileList;
    private Scanner inputScanner;

    public FileManager(){
        inputScanner = new Scanner(System.in);
        fileList = new ArrayList<Scanner>();
    }

    // opens a file and loads it into the fileList 
    // return true if works, false otherwise
    public boolean openFile(String fileName){
        try{
            File newFile = new File(fileName);
            Scanner newScan = new Scanner(newFile);
            fileList.add(newScan);
            return true;
        }
        catch(FileNotFoundException e){
            System.out.println(e.toString());
            return false;
        }
    }

    // Gets a file input from user, adds to list of opened files
    public void promptForFile(){
        boolean done = false;
        String input;
        // user is adding files to the list
        while(!done){
            System.out.println("Please type the name of the file you wish to have formatted:\n");
            input = inputScanner.nextLine();
            if(openFile(input)){
                System.out.println("File opened successfully.");
            }
            else{
                System.out.println("File failed to open.");
            }

            // continually add new files until user says no
            System.out.println("Would you like to input another file?");
            input = inputScanner.nextLine();
            // We don't want a new file.
            if(input.equals("no") || input.equals("No") || input.equals("NO") || input.equals("n")){
                done = true;
            }
            
        }   
    }


    // returns next line in file, null if there isn't one
    public String getNextLine(Scanner file){
        if(file.hasNext()){
            return(file.nextLine());
        }
        else{
            return(null);
        }
    }
}
