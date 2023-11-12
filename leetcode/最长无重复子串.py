# 暴力解法，将最长子串存储下来，依次遍历
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        max_str = ""
        for i in range(0, len(s)):
            temp_str = s[i]
            for j in range(i, len(s)):
                if i == j: continue
                if s[j] not in temp_str:
                    temp_str = temp_str + s[j]
                else:
                    break
            if len(max_str) < len(temp_str):
                max_str = temp_str
        return len(max_str)


# 暴力解法，遍历O(n2)的时间复杂度
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 1
        if len(s) == 0:
            return 0

        s_list = list(s)
        while left < len(s) - 1:
            substr = s_list[left]
            right = left + 1
            while right < len(s):
                if s_list[right] in substr:
                    break
                else:
                    substr = substr + s_list[right]
                    if length <= right + 1 - left: 
                        length = right + 1 - left
                right = right + 1
            left = left + 1
        
        return length


# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
          return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len
