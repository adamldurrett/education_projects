import java.util.*;
import java.io.*;

public class FileManager {

    ArrayList<File> fileList;
    private int current_file;
    private Scanner fileScanner;

    public FileManager(){
        fileList = new ArrayList<File>();
    }

    public boolean openFile(String fileName){
        try{
            File newFile = new File(fileName);
            Scanner newScan = new Scanner(newFile);
            fileList.add(newFile);
            return true;
        }
        catch(FileNotFoundException e){
            System.out.println(e.toString());
            return false;
        }
    }

    private void changeFileIndex(String fileName){
        File found_file = null;

        for(File file : fileList){
            if(file.getName() == fileName){
                found_file = file;
            }
        }

        if(found_file != null){
            current_file = fileList.indexOf(found_file);
            System.out.println("Changed focus to file :" + ((Integer)current_file).toString() + " named " + fileName);
        }
        else{
            System.out.println("Unable to find file named " + fileName);
        }
    }
    public String getNextLine(){
        return("");
    }
}
