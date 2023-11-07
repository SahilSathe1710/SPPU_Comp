import java.util.*;

public class fibo{
    public static int FibRecursion(int count){
        if(count == 0){
            return 0;
        }
        if(count == 1){
            return 1;
        }
        return FibRecursion(count-1) + FibRecursion(count-2);
    }


    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEnter the length of the fibonacci using recursion: ");
        // System.out.println("\nEnter the length of the fibonacci using iteration: ");
        int fib_len = sc.nextInt();
        System.out.println("\nThe fibonacci series of " + fib_len + " numbers using recursion is: ");
        // System.out.println("\nThe fibonacci series of " + fib_len + " numbers using iteration is: ");
        long start = System.nanoTime();
        for(int i=0; i<fib_len; i++){
            System.out.print(FibRecursion(i) + " ");
        }
        long end = System.nanoTime();
        double duration = (end-start)/1e9;
        System.out.println("\n\nTotal time taken using recursion: " + duration + "s\n");

        // code for iterative approach
        // int firstTerm = 0, secondTerm = 1;
        // int nextTerm;
        // long start = System.nanoTime();
        // for (int i = 0; i < fib_len; i++) {
        //     System.out.print(firstTerm + " ");
      
        //     nextTerm = firstTerm + secondTerm;
        //     firstTerm = secondTerm;
        //     secondTerm = nextTerm;
        // }
        // long end = System.nanoTime();
        // double duration = (end-start)/1e9;
        // System.out.println("\n\nTotal time taken using iteration: " + duration + "s\n");
    }
}