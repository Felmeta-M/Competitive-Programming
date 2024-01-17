public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
    int res = 0;
    // Using the bitwise AND operation to check each bit
    for (int i = 0; i < 32; i++) {
        // Check if the current bit is set (equals 1)
        if ((n & 1) == 1) {
            res++;
        }
        // Right shift the number to check the next bit
        n >>>= 1;
    }
    return res;
}

}