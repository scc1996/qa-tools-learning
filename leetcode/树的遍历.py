"""
题目：数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

""" 

# 深度优先遍历
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left: 左括号还可以使用的个数
            :param right: 右括号还可以使用的个数
            :return:
            """
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res


# 广度优先遍历
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        ge = GenPairing()
        res = ge.gen(1, 0, n, "(", [])
        return res

class GenPairing:
    def gen(self, left, right, max_num, res_single, res_list):
        if left == max_num:
            res_single = res_single + (max_num - right) * ")"
            res_list.append(res_single)
            return res_list
        else:
            ges1 = GenPairing()
            if left + 1 <= max_num:
                ges1.gen(left + 1, right, max_num, res_single + "(", res_list)
            if right + 1 < left + 1:
                ges1.gen(left, right + 1, max_num, res_single + ")", res_list)

        return res_list
