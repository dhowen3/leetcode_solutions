class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split("/")
        # remove all empty strings, which handles 
        # a. problem of combining slashes (first pass)
        # b. problem of removing ending slash
        # c. problem of removing periods
        split = list(filter(lambda x : x != "" and x != ".", split)) 

        # now fix .. 's
        backwards_count = 0
        for i in range(len(split) - 1, -1,-1):
            if split[i] == "..":
                backwards_count += 1
                split[i] = ""
            elif split[i] != ".." and backwards_count > 0:
                split[i] = ""
                backwards_count -= 1

        # 2nd pass, fix combining slashes
        split = list(filter(lambda x : x != "", split)) 

        # build to_return
        to_return = "/"
        n = len(split)
        for i,s_bar in enumerate(split):
            if i == n - 1:
                to_return += s_bar
            else:
                to_return += s_bar + "/"
        
        return to_return
