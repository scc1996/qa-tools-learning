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


"""
s[i:j+1][::-1] = 子串的倒序，s[i][j + 1] = [1,2,3,4],s[i:j+1][::-1] = [4,3,2,1]
s[3::-1] = 从下标3截止的前半段子串的倒序，s = [1,2,3,4,5]  s[3::-1] = [4,3,2,1]
"""
