1. 字符串操作
1.1全部转化为小写字母：s.lower()
1.2判断当前字符是否是数字或字母： 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9'
1.3字符串倒叙或字符串数组倒叙 [::-1]
1.4将字符串排序并生成新的字符串 temp_word = ''.join(sorted(strs[i])) -- 对strs[i]重新排序，排序结果是一个数组，使用.join重新组成一个字符串
1.5sort（）和sorted（） -- sort是对象的成员方法，会改变原对象，sorted()是python的内建函数，不修改原对象，会返回一个新的对象
调用 -- array.sort() 无返回值
result = sorted(array)  返回值用result存储

2. 字典操作
判断字典中是否有该key： if key in dict：
判断字典值中是否有该value： if value in dict.values():

3. 哈希逻辑
哈希实质上就是生成对应关系的dict -- 使用dict解决即可
