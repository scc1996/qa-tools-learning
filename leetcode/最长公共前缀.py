# 暴力解法
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        temp_list = list(strs[0])

        result = ""
        temp_str = ""
        for index in range(0, len(temp_list)):
            temp_str = temp_list[index]

            for index_of_word in range(1, len(strs)):
                single_word = list(strs[index_of_word])
                if len(single_word) < index:
                    return result

                if temp_str != single_word[index]:
                    return result
                
            result = result + temp_str
        
        return result


# zip + set方法
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

"""
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。利用 * 号操作符，可以将元组解压为列表。
zip(*)解压函数，将对象中的每一个元素/元祖/字符串的相同位置的子元素组合成一个新的元祖，并将所有组成的元祖以列表的形式进行展示。
对于一个列表的zip：

#python3:
l = ['flower', 'flow', 'flight']
print(zip(l))
print(zip(*l))
print(list(zip(l))) #转换为list显示
print(list(zip(*l)))
print(tuple(zip(l)))
print(tuple(zip(*l)))

# <zip object at 0x0000018B0BBD4F08>
# <zip object at 0x0000018B0BBD4F08>
# [('flower',), ('flow',), ('flight',)]
# [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
# (('flower',), ('flow',), ('flight',))
# (('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g'))

"""
