import java.util.Scanner;

public class menu {
        
    // Method for add two numbers
    public static void add(int a, int b) {
    System.out.println(a + b);
    }

    // Method for subtract two numbers
    public static void subtract(int a, int b) {
    System.out.println(a - b);
    }

    // Method for double a Number
    public static void doubled(int a) {
    System.out.println(a + a);
    }

    public static void main(String[] arguments) {

        // taking the user input ....
        Scanner sc = new Scanner(System.in);
        String input_args = sc.nextLine();
        String args[]= input_args.split(" ");
        sc.close();

        if (args[0].equals("+")) {
            int x = Integer.parseInt(args[1]);
            int y = Integer.parseInt(args[2]);
            add(x, y); //it will take value from comand line
        }

        else if (args[0].equals("-")) {
            int x = Integer.parseInt(args[1]);
            int y = Integer.parseInt(args[2]);
            subtract(x, y); //it will take value from comand line
        }

        else if (args[0].equals("&")) {
            int x = Integer.parseInt(args[1]);
            doubled(x); //it will take value from comand line
        }

        else{
            System.out.println("Please provide the valid arguments!");
        }

    }
}


