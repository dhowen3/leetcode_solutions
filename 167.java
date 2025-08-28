class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] toReturn = new int[]{0,0};
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < n; ++i) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < n; ++i) {
            if (map.get(target - nums[i]) != null) {
                toReturn[0] = i + 1;
                toReturn[1] = map.get(target - nums[i]) + 1;
                break;
            }
        }
        return toReturn;
    }
}
