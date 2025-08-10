from collections import deque
'''
42351
42513
42531
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        q1,q2 = deque(),deque()
        n = len(nums)
        break_index = -1
        for i in range(n-1,-1,-1):
            if len(q1) == 0:
                q1.appendleft(nums[i])
            elif nums[i] >= q1[0]:
                q1.appendleft(nums[i])
            else:
                break_index = i
                break
        break_num = nums[break_index]
        print(break_index)
        if break_index == -1 :
            nums.sort()
            return
        while q1[-1] <= break_num:
            q2.appendleft(q1.pop())
        q2.appendleft(break_num)
        nums[break_index] = q1.pop()
        print(q1,q2)
        i = break_index + 1
        while True:
            if len(q1) == 0 and len(q2) == 0: break
            elif len(q1) == 0 and len(q2) != 0: nums[i] = q2.pop()
            elif len(q1) != 0 and len(q2) == 0: nums[i] = q1.pop()
            elif q1[-1] < q2[-1]: nums[i] = q1.pop()
            else: nums[i] = q2.pop()
            i += 1
