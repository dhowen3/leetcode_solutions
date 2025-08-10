class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = {i:[] for i in range(1,target+1)}
        for i in range(1,target + 1):
            if i in candidates:
                dp[i].append([i])
            bool_arr = [False for x in range(i)]
            for j in range(1,i):
                k = i - j
                if len(dp[j]) == 0 or len(dp[k]) == 0 or bool_arr[j-1] or bool_arr[k-1]:
                    continue
                for l1 in dp[j]:
                    for l2 in dp[k]:
                        dp[i].append(l1 + l2)
                bool_arr[j-1], bool_arr[k-1] = True, True 
            for entry in dp[i]:
                entry.sort()
            '''

            credit for following line - hadn't used this method before
            https://stackoverflow.com/questions/3724551/uniqueness-for-list-of-lists
            
            '''
            dp[i] = [list(x) for x in set(tuple(x) for x in dp[i])] 
        for i in range(1, target + 1):
            print(dp[i])
        return dp[target]
