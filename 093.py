class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        dot_locations = []
        # remark on set cardinality of dot locations:
        # s.len <= 20 which implies 
        # |{dot locations}| <= 18 * 17 * 16
        for i in range(1,n-2):
            for j in range(i+1, n-1):
                for k in range(j+1,n):
                    dot_locations.append((i,j,k))
        to_return = []
        for (i,j,k) in dot_locations:
            all_valid = True
            for substr in s[:i],s[i:j],s[j:k],s[k:]:
                if (len(substr) > 1 and substr[0] == '0') or int(substr) > 255:
                    all_valid = False
                    break
            if all_valid:
                to_return.append(f"{s[:i]}.{s[i:j]}.{s[j:k]}.{s[k:]}") 
        return to_return
