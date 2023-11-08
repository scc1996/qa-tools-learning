# 栈操作
class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for i in range(0, len(s)):
            if len(result) == 0 or s[i] == '(' or s[i] == '[' or s[i] == '{':
                result.append(s[i])
            else:
                top_char = result.pop()
                temp_str = top_char + s[i]
                if temp_str == '()' or temp_str == '[]' or temp_str == '{}':
                    continue
                else:
                    result.append(top_char)
                    result.append(s[i])
        
        if len(result) == 0: return True
        return False
