import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Random;


public class Solution {

    public static void main(String[] args) {
        
        long t1, t2;
        t1 = System.currentTimeMillis();
        read_from_file("input06.txt");
        // test();
        t2 = System.currentTimeMillis();
        System.out.println("delta: " + (t2 - t1));
    }

    public static void test() {
        int n = 3;
        int d = 3;
        long[] array_H = {5, 7, 8};
        long[][] array_X = {{1, 2, 3}, {2, 3, 4}, {4, 5, 6}};

        Challenge challenge = new Challenge(n, d, array_H, array_X);
        System.out.println(challenge.solve_problem());

    }

    public static void read_from_file(String filename){
        File file = new File(filename);
        int n, d, i, j;
        long[] array_H;
        long[][] array_X;

        try {
            Scanner input = new Scanner(file);
            n = input.nextInt();
            d = input.nextInt();

            array_H = new long[n];
            array_X = new long[n][d];

            for (i = 0; i < n; i++) {
                array_H[i] = input.nextLong();
                for (j = 0; j < d; j ++) {
                    array_X[i][j] = input.nextLong();
                }
            }

            Challenge challenge = new Challenge(n, d, array_H, array_X);
            System.out.println(challenge.solve_problem());
            input.close();

        } catch (Exception e) {
            System.out.println("Error " + e);

        }
    }
}

class Challenge{

    private int n = 0;
    private int d = 0;
    private long[] array_H;
    private long[][] array_X;

    private static final long limit = 1000000009;

    public Challenge(int n, int d, long[] array_H, long[][] array_X) {
        this.n = n;
        this.d = d;

        this.array_H  = array_H;
        this.array_X  = array_X;
    }

    String solve_problem() {
        long tmp = 0;
        long tmp_result = 0;
        long final_result = 0;
        long hterm_1, hterm_2;
        int i, j, k;

        for(i = 0; i < n; i++) {
            hterm_1 = array_H[i] % limit;

            for(j = i + 1; j < n; j++) {
                hterm_2 = array_H[j] % limit;
                tmp = 0;
                for(k = 0; k < d; k++) {
                    tmp += Math.abs(array_X[i][k] - array_X[j][k]);
                    // System.out.println("array_X[" + i + "][" + k + "] - array_X[" + j + "][" + k + "] = " +
                    //     array_X[i][k] + " - " + array_X[j][k] + " = " + Math.abs(array_X[i][k] - array_X[j][k]));
                }
                tmp_result += (hterm_1 * hterm_2 * (tmp % limit)) % limit;
                tmp_result %= limit;
                // System.out.println("tmp_result += " + hterm_1 + " * " + hterm_2 + " * " + tmp + " = " + tmp_result);
                // System.out.println();
            }
        }

        final_result = tmp_result;
        return Long.toString(final_result);
    }
}

