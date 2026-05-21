//the initailized java struct
/*
public class Main{
    public static void main(String[] args){


    }
}
*/
private class Human{
    public static void main(String[] args) {
        int kg=50;
        int tall_cm=160;
        System.out.println(kg+' '+tall_cm);
    }
}
public class Bro_code{
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


    }
}