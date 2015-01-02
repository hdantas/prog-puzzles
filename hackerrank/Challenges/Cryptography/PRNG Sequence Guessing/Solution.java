import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Random;

// 2
// 1374037200 1374123600
// 643
// 953
// 522
// 277
// 464
// 366
// 321
// 409
// 227
// 702
// 1374037299 1374143600
// 877
// 654
// 2
// 715
// 229
// 255
// 712
// 267
// 19
// 832

public class Solution {

    public static void main(String[] args) {
        Scanner stdin     = new Scanner(System.in);
        int testCaseCount = 2;
        int[][] reference = {{643, 953, 522, 277, 464, 366, 321, 409, 227, 702}, {877, 654, 2, 715, 229, 255, 712, 267, 19, 832}};
        int[] startTime   = {1374037200, 1374037299};
        int[] endTime     = {1374123600, 1374143600};
        
        long t1, t2, t3, t4, t5, t6;
        for (int testCaseIndex = 0; testCaseIndex < testCaseCount; testCaseIndex += 1) {
            t1 = System.currentTimeMillis();
            for (int seed = startTime[testCaseIndex]; seed < endTime[testCaseIndex]; seed += 1) {
                Random rand = new Random(seed);
                boolean valid = true;

                for (int i = 0; i < 10; i++){
                    valid &= rand.nextInt(1000) == reference[testCaseIndex][i];
                }

                if (valid) {
                    System.out.print(seed + " ");
                    for (int i = 0; i < 10; i++)
                        System.out.print(rand.nextInt(1000) + " ");
                    System.out.println();
                    break;
                }
            }
            t2 = System.currentTimeMillis();
            System.out.println("Test case: " + testCaseIndex + "\tdelta: " + (t2 - t1));
        }

    }
}