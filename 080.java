// have a "trash window" preceding currentIndex, being carried forward until end of nums array
// is reached

class Solution {
    public int getCountOfCurrentNum(int[] nums, int currentIndex, int duplicatesFound, int trashWindowStart) {
        int toReturn = 0;
        int currentNum = nums[currentIndex];
        for (int i = currentIndex; i < nums.length && nums[i] == currentNum; ++i) {
            ++toReturn;
        }
        return toReturn;
    }

    public int removeDuplicates(int[] nums) {
        int currentIndex = 0, duplicatesFound = 0, trashWindowStart = -1, n = nums.length;
        while (currentIndex < n) {
            int countOfCurrentNum = getCountOfCurrentNum(nums, currentIndex, duplicatesFound, trashWindowStart);

            if (duplicatesFound == 0) {
                trashWindowStart = currentIndex;
            }
            
            if (countOfCurrentNum > 2) {
                nums[trashWindowStart] = nums[currentIndex];
                nums[trashWindowStart + 1] = nums[currentIndex];
                trashWindowStart += 2;
                duplicatesFound += countOfCurrentNum - 2;
            } else if (countOfCurrentNum == 2) {
                nums[trashWindowStart] = nums[currentIndex];
                nums[trashWindowStart + 1] = nums[currentIndex];
                trashWindowStart += 2;
            } else if (countOfCurrentNum == 1) {
                nums[trashWindowStart] = nums[currentIndex];
                trashWindowStart += 1;
            } else {
                // all cases should be covered
                assert(false);
            }

            currentIndex = currentIndex + countOfCurrentNum;
        }
        return n - duplicatesFound;
    }
}
