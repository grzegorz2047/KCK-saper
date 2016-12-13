/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.util.Arrays;

/**
 *
 * @author Mikołaj Balcerek
 */
public class JavaApplication2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException, InterruptedException {
       
        
        ProcessBuilder processBuilder = new ProcessBuilder("C:\\Program Files (x86)\\swipl\\bin\\swipl-win.exe","-s","E:\\Users\\Ewe\\Desktop\\pro.pl","-t","rozkaz(A,B,[Chwyc,bomba],[]).");
        Process process = processBuilder.start();
    
        
    InputStream is = process.getInputStream();
InputStreamReader isr = new InputStreamReader(is);
BufferedReader br = new BufferedReader(isr);
String line;

System.out.printf("Output of running %s is:", Arrays.toString(args));

while ((line = br.readLine()) != null) {
  System.out.println(line);
}
    }
}
        /*
        Process process = new ProcessBuilder(
"C:\\Program Files (x86)\\swipl\\bin\\swipl-win.exe consult('E:\\Users\\Ewe\\Desktop\\KCK-saper-master\\Zadania_Domowe\\saper.pl').","listing.").start(); */
//utputStream gz = process.getOutputStream();
   
    

