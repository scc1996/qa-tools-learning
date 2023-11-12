如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。

 

示例 1：

输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串


# 暴力解法
# 先将字符串转为小写，使用lower()方法，然后判断是否为数字或字母'a' <= i <= 'z' or '0' <= i <= '9'
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for i in s:
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                new_s = new_s + i
        
        reverse_s = new_s[::-1]
        return new_s == reverse_s
