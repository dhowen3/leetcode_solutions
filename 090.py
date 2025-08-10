class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = {num:nums.count(num) for num in nums}
        sets = []
        for num in counts:
            for i in range(counts[num]):
                current = []
                for j in range(i+1):
                    current.append(num)
                sets.append(current)
        to_return = []
        for i in range(2**len(sets)):
            mapping = str(bin(i))[2:][::-1]
            current = []
            current_set = set()
            should_append = True
            for j,char in enumerate(mapping):
                if char == '1' and sets[j][0] in current_set:
                    should_append = False
                    break
                elif char == '1':
                    current += sets[j]
                    current_set.add(sets[j][0])
            if should_append: to_return.append(current)
        return to_return
