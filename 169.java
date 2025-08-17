class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int num : nums) {
            if (map.containsKey(num))  {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        int max = -1;
        int maxElt = -1;
        for (int key : map.keySet()) {
            if (map.get(key) > max) {
                maxElt = key;
                max = map.get(key);
            }
        }
        return maxElt;
    }
}
