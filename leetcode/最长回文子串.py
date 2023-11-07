# 暴力循环 + 剪枝
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_str = s[0]

        for i in range(len(s)):
            if len(s) - i + 1 <= max_len:
                break
            
            for j in range(i+1, len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and j + 1 - i > max_len:
                    max_len = j + 1 - i
                    max_str = s[i:j+1]
            
        return max_str
