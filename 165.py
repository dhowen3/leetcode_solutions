class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = [int(s_i) for s_i in version1.split(".")]
        v2_list = [int(s_i) for s_i in version2.split(".")]
        if len(v1_list) == len(v2_list):
            for i, val in enumerate(v1_list):
                if val > v2_list[i]:
                    return 1
                if val < v2_list[i]:
                    return -1
            return 0
        elif len(v1_list) > len(v2_list):
            for i, val in enumerate(v2_list):
                if val > v1_list[i]:
                    return -1
                if val < v1_list[i]:
                    return 1
            for val in v1_list[len(v2_list):]:
                if val != 0:
                    return 1
            return 0
        else: # v2_list is longer
            for i, val in enumerate(v1_list):
                if val > v2_list[i]:
                    return 1
                if val < v2_list[i]:
                    return -1
            for val in v2_list[len(v1_list):]:
                if val != 0:
                    return -1
            return 0
        return 420_69
