class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        location_found = -1
        haystack_index = 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        while haystack_index < haystack_len:
            needle_index = 0
            while haystack_index + needle_index < haystack_len \
                        and \
                        needle_index < needle_len \
                        and \
                        haystack[haystack_index + needle_index] == needle[needle_index]:
                needle_index += 1
            if needle_index == needle_len:
                location_found = haystack_index
                break
            else:
                haystack_index += 1
        return location_found
