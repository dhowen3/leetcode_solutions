class Solution {
    public int find_pivot(int[] nums, int low, int high) {
        int middle = low + (int)((high - low)/2);
        if (high - low == 1 && nums[low] > nums[low+1]) {
            return low + 1;
        } else if (high - low == 1) {
            return 0;
        }
        if (nums[low] > nums[middle]) {
            return find_pivot(nums,low, middle);
        }
        return find_pivot(nums,middle,high);
    }

    public int binSearch(int[] nums, int n, int target, int pivot, int low, int high) {
        int i = (pivot + low) % n;
        int j = (pivot + high)  % n;
        if (high - low <= 1 && nums[i] == target) {
            return i;
        } else if (high - low <= 1) {
            return -1;
        }
        int middle = low + (int)((high - low)/2);
        int k = (pivot + middle) % n;
        if (target < nums[k]) {
            return binSearch(nums, n, target, pivot, low, middle);
        } else {
            return binSearch(nums, n, target, pivot, middle, high);
        }
    }

    public int search(int[] nums, int target) {
        int n = nums.length;
        if (n==1) {
            return nums[0] == target ? 0 : -1;
        }
        int pivot = 0;
        if (nums[0] > nums[n-1]) {
            pivot = find_pivot(nums, 0, n);
        }
        System.out.println(pivot);
        return binSearch(nums, n, target, pivot, 0, n);
    }
}
