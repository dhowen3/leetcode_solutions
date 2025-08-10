class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        num_subsets = 2**n
        to_return = []
        for i in range(num_subsets):
            current_subset = []
            mapping = r""+str(bin(i))[2:]
            for j in range(len(mapping)):
                if mapping[-(j+1)] == '1':
                    current_subset.append(nums[j])
            to_return.append(current_subset)
        return to_return
