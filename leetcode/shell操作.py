写一个 bash 脚本以统计一个文本文件 words.txt 中每个单词出现的
频率
。

为了简单起见，你可以假设：

words.txt只包括小写字母和 ' ' 。
每个单词只由小写字母组成。
单词间由一个或多个空格字符分隔。


cat Words.txt| tr -s ' ' '\n' 
- tr 命令用于转换或删除文件中的字符
- -s：缩减连续重复的字符成指定的单个字符

cat Words.txt| tr -s ' ' '\n' | sort
- sort: 排序

uniq 命令用于检查及删除文本文件中重复出现的行列，一般与 sort 命令结合使用。 -- uniq的前提是sort！！！！
- -c：在每列旁边显示该行重复出现的次数。

cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r
- sort -r，-r是倒序排列

cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
- awk '{print $2, $1}': 输出，awk为文本处理工具，特别适用于处理结构化文本。print是awk的内置函数，会把位置2、位置1的数据输出
