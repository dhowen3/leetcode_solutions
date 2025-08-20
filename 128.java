import java.util.HashMap;
import java.util.Arrays;

class Solution {
    // compare : num's current highest range (if num in map)
    // with
    // num's above neighbor's highest range
    // take the larger of the two
    public int getHighNum(HashMap<Integer, Integer[]> map, int num) {
        int highNum = map.get(num + 1)[1];
        if (map.get(num) != null) {
            highNum = Math.max(highNum, map.get(num)[1]);
        } 
        return highNum;

    }
    // compare : num's current lowest range (if num in map)
    // with
    // num's below neighbor's lowest range
    // take the lesser of the two
    public int getLowNum(HashMap<Integer, Integer[]> map, int num) {
        int lowNum = map.get(num-1)[0];
        if (map.get(num) != null) {
            lowNum = Math.min(lowNum, map.get(num)[0]);
        } 
        return lowNum;
    }

    // loop through nums, adding each to a hashmap
    // map - num |-> <lowest in sequence, highest in sequence>
    // 
    // if num's neighbors (i.e. num -1, num + 1) exist, then
    // make connectings, always updating the lowest and highest
    // in the range with the updated range
    // 
    // at each iteration, compare the length of the current range
    // with the greatest range found thus far.
    // return the greatest range found.
    public int longestConsecutive(int[] nums) {
        int longestSeqLen = 0;
        HashMap<Integer, Integer[]> map = new HashMap<Integer, Integer[]>();
        for (int num: nums) {
            Integer[] range;
            
            // below, above, curernt - 
            // answer question:
            // is value or its neighbors already contained in hashmap?
            boolean below = map.get(num - 1) != null; 
            boolean above = map.get(num + 1) != null;
            boolean current = map.get(num) != null;

            if (current && above && below) {
                continue;
            }
            if (!below && !above) { // isolated value
                range = new Integer[]{num, num};
                map.put(num, range);
            } else if (!below && above) { // has neighbor above but not below
                int highNum = getHighNum(map, num);
                range = new Integer[]{num, highNum};
                map.put(num, range);
                map.put(highNum, range); // set high value in map to have lowest range of num
            } else if (below && !above) { // has neighbor below but not above
                int lowNum = getLowNum(map, num);
                range = new Integer[]{lowNum,num};
                map.put(num, range);
                map.put(lowNum, range); // set low value in map to have highest range of num
            } else if (below && above) { // is surrounded by neighbors
                int highNum = getHighNum(map, num);
                int lowNum = getLowNum(map, num);
                range = new Integer[]{lowNum,highNum};
                map.put(num, range);
                map.put(lowNum, range); // set high value in map to have highest range of high num
                map.put(highNum, range); // and vice versa

            } else {
                assert false;
            }
            int currentSeqLen = map.get(num)[1] - map.get(num)[0] + 1; // is range len > exisitng seq len?
            longestSeqLen = Math.max(longestSeqLen, currentSeqLen);
        }
        return longestSeqLen;
    }
}
