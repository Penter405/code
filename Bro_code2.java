//this should be marged with Bro_code.java
//the initailized java struct
/*
public class Main{
    public static void main(String[] args){


    }
}
*/
/*
private class Human{
    public static void main(String[] args) {
        int kg=50;
        int tall_cm=160;
        System.out.println(kg+' '+tall_cm);
    }
}
*/
import java.util.Scanner;
import java.util.ArrayList;
public class Bro_code2{
    public static void main(String[] args){
        //data type
        //Primitive (stack)
        int x=5;
        double d = 3.12f;
        char c = 'a';
        boolean is= false;

        //Reference (heap)
        String s="Hello World";
        String Smart_guy= "Penter";

        //Output
        System.out.println(x);
        System.out.println(d);
        System.out.println(c);
        System.out.println(is);
        System.out.println(s);
        //Output mutiple data
        System.out.println("Hello " + Smart_guy);

        //initialize easy input
        Scanner sc= new Scanner(System.in);

        //input a data to variable
        int age;
        System.out.println("how old are you?");
        age=sc.nextInt();

        System.out.println("You are "+age+" years old");

        //choosing sturct
        if(age>=18){
            System.out.println("you can drive cars");
            
        }else{
            System.out.println("you can not drive cars");
        }
        //continuous struct
        for(int i=0;i<5;++i){
            System.out.println(i);
        }
        //ArrayList--pyhton list--dymanic array
        ArrayList my_list=new ArrayList<>();

    }
}