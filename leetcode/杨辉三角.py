# 第i行有i个数字，j表示列边界，二维数组运算

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(0, numRows):
            single_array = []
            for j in range(0, i + 1): 
                if i - 1 < 0 or j - 1 < 0 or j + 1 > i:
                    single_array.append(1)
                else:
                    single_array.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(single_array)
        return res   
