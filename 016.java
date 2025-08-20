import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int closestSum = nums[0] + nums[1] + nums[2];
        int smallestDiff = Math.abs(target - closestSum);
        int n = nums.length;
        Arrays.sort(nums);
        for (int i = 0; i < n - 2; ++i) {
            int lPtr = i + 1;
            int rPtr = n - 1;
            while (lPtr < rPtr) {
                int currentSum = nums[i] + nums[lPtr] + nums[rPtr];
                if (currentSum == target) {
                    return currentSum;
                } else if (currentSum < target) {
                    lPtr += 1;
                } else {
                    rPtr -= 1;
                }
                if (Math.abs(target - currentSum) < smallestDiff) {
                    smallestDiff = Math.abs(target - currentSum); 
                    closestSum = currentSum;
                }
            }
        }
        return closestSum;
    }
}
