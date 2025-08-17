class Solution {
    public int maxProduct(int[] nums) {
        int maxFound = nums[0];
        for (int i = 0; i < nums.length; ++i) {
            int currentProduct = 1;
            for (int j = i; j < nums.length; ++j) {
                currentProduct *= nums[j];
                if (currentProduct >= maxFound) {
                    maxFound = currentProduct;
                }
                if (currentProduct == 0) {
                    break;
                }
            }
        }
        return maxFound;
    }
}
