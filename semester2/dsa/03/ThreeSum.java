import java.util.*;
import edu.princeton.cs.algs4.In;

public class ThreeSum {
    public static int count(int[] a) {
        int n = a.length;
        int count = 0;

        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                for (int k=j+1; k<n; k++) {
                    if (a[i] + a[j] + a[k] == 0 ) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        int[] a = in.readAllInts();

        /*
        System.out.println("Running...");
        Scanner scanner = new Scanner(System.in);
        
        List<Integer> temp = new ArrayList<>(); 

        while (scanner.hasNext()) {
            temp.add(scanner.nextInt());
        }
        scanner.close();
        System.out.println("Read input...");

        int[] a = temp.stream().mapToInt(i -> i).toArray();
        */

        System.out.println(count(a));
    }
}
