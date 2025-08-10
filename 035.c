int searchInsertHelper(int* nums, size_t lowBound, size_t highBound, int target) {
    // base case
    if (highBound - lowBound <= 1) {
        if (target == nums[lowBound]) {
            return lowBound;
        } else if (target > nums[lowBound]){
            return lowBound + 1;
        } else {
            return lowBound;
        }
    }
    // recursive case
    size_t middleOfRange = (lowBound + highBound ) / 2;
    if (target < nums[middleOfRange]) {
        return  searchInsertHelper(nums, lowBound, middleOfRange, target);
    } else {
        return searchInsertHelper(nums, middleOfRange, highBound, target);
    }
}

int searchInsert(int* nums, int numsSize, int target){
    return searchInsertHelper(nums, 0, numsSize, target);
}
