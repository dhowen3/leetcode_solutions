// citation? if other sols. aren't cited assume original.
// for this one - looked at others' solutions and came back 3 days later to write it up from memory
// very slick bitwise-stuff

class Solution {
    public int singleNumber(int[] nums) {
        int toReturn = 0;
        int mask = 1;
        for (int i = 0; i < 32; ++i) {
            int sum = 0;
            for (int num : nums) {
                if ((num & mask) != 0) {
                    ++sum;
                }
            }
            if (sum % 3 == 1) {
                toReturn |= mask;
            }
            mask <<= 1;
        }
        return toReturn;
    }
}
