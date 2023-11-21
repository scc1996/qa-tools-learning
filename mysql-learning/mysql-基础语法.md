# 基础语法
1. DML和DDL的区别
DML(Data Manipulation Language)数据操纵语言：适用范围：对数据库中的数据进行一些简单操作，如insert,delete,update,select等.
DDL(Data Definition Language)数据定义语言：适用范围：对数据库中的某些对象(例如，database,table)进行管理，如Create,Alter和Drop
DML是可以手动控制事务的开启、提交和回滚的；DDL提交是隐性的，不能rollback

3. 创建数据库
```
create database <数据库名>;
```

3. 删除数据库
```
drop database <数据库名>;
```

4. 选择数据库
```
use <数据库名>;
```

5. 查看所有数据库
```
show databases;
```

5. 查看所有表
```
show tables;
```

6. 使用数据表
```
use Table
```

7.查看建表语句
```
Show create table Table_Name;
```

8. 创建数据表
```
create table Tbl_TotalAdValidCheck
(
    AdIndex bigint(20),
    CrtSize bigint(20),
    AdType bigint(20),
    DirectType bigint(20),
    DestType bigint(20),
    ProductType bigint(20),
    Valid bigint(20),
    MaterialValid bigint(20),
    ProductValid bigint(20)
);

```

9. 建立联合索引
```
alter table Tbl_TotalAdValidCheck add constraint pk_name primary key (AdIndex,CrtSize)

add constraint是增加约束，这里add constraint pk_name表示，约束名称是pk_name，后面的primary key，表示约束类型是主键类型，括号内是生效的字段

其他的类型例如：
alter table Tbl_TotalAdValidCheck add constraint uni_key unique (AdIndex)
表示对table的adindex字段，增加了不重复（unique）的约束
```
参考：https://blog.csdn.net/u010237107/article/details/40392169

10. 查看表结构
```
desc table_name;
```

11. 删除数据表
```
drop table table_name;
```

12. 表插入数据
```
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```

13. 查询表数据
```
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```
查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。
SELECT 命令可以读取一条或者多条记录。
你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据
你可以使用 WHERE 语句来包含任何条件。
你可以使用 LIMIT 属性来设定返回的记录数。
你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。

14. 数据库查询条件
```
select column_name from table_1,table_2 where options;

执行顺序：
FROM, including JOINs
WHERE
GROUP BY
HAVING
WINDOW functions
SELECT
DISTINCT
UNION
ORDER BY
LIMIT and OFFSET
```

15. 更新数据库
```
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]
```

16. 数据删除
```
DELETE FROM table_name [WHERE Clause]
```
delete，drop，truncate 都有删除表的作用，区别在于：

1、delete 和 truncate 仅仅删除表数据，drop 连表数据和表结构一起删除
2、delete 是 DML 语句，操作完以后如果没有不想提交事务还可以回滚，truncate 和 drop 是 DDL 语句，操作完马上生效，不能回滚
3、执行的速度上，drop>truncate>delete

17. like关键字
```
like 匹配/模糊匹配，会与 % 和 _ 结合使用。

'%a'     //以a结尾的数据
'a%'     //以a开头的数据
'%a%'    //含有a的数据
'_a_'    //三位且中间字母是a的
'_a'     //两位且结尾字母是a的
'a_'     //两位且开头字母是a的
查询以 java 字段开头的信息。

SELECT * FROM position WHERE name LIKE 'java%';
查询包含 java 字段的信息。

SELECT * FROM position WHERE name LIKE '%java%';
查询以 java 字段结尾的信息。

SELECT * FROM position WHERE name LIKE '%java';
```

18. union关键字
union关键字，会把从表a和表b查询出来的字段，进行去重展示
```
mysql> SELECT * FROM Websites;
+----+--------------+---------------------------+-------+---------+
| id | name         | url                       | alexa | country |
+----+--------------+---------------------------+-------+---------+
| 1  | Google       | https://www.google.cm/    | 1     | USA     |
| 2  | 淘宝          | https://www.taobao.com/   | 13    | CN      |
| 3  | 菜鸟教程      | http://www.runoob.com/    | 4689  | CN      |
| 4  | 微博          | http://weibo.com/         | 20    | CN      |
| 5  | Facebook     | https://www.facebook.com/ | 3     | USA     |
| 7  | stackoverflow | http://stackoverflow.com/ |   0 | IND     |
+----+---------------+---------------------------+-------+---------+

mysql> SELECT * FROM apps;
+----+------------+-------------------------+---------+
| id | app_name   | url                     | country |
+----+------------+-------------------------+---------+
|  1 | QQ APP     | http://im.qq.com/       | CN      |
|  2 | 微博 APP | http://weibo.com/       | CN      |
|  3 | 淘宝 APP | https://www.taobao.com/ | CN      |
+----+------------+-------------------------+---------+
3 rows in set (0.00 sec)


SELECT country FROM Websites UNION SELECT country FROM apps ORDER BY country;
+---------+
| country |
+---------+
| USA     |
| IND     |
| CN      |
+---------+
```
如果想要从两个表读出全部的country信息且不去重，使用union all
```
SELECT country FROM WebsitesUNION ALLSELECT country FROM apps ORDER BY country;
+---------+
| country |
+---------+
| USA     |
| USA     |
| IND     |
| CN      |
| CN      |
| CN      |
| CN      |
| CN      |
| CN      |
| CN      |
+---------+
```

带有where的union语句
```
SELECT country, name FROM WebsitesWHERE country='CN'UNION ALL
	SELECT country, app_name FROM appsWHERE country='CN'ORDER BY 
	country;
+--------------+---------+
| name         | country |
+--------------+---------+
| QQ APP       | CN      |
| 淘宝          | CN      |
| 菜鸟教程       | CN      |
| 微博          | CN      |
| 微博 APP      | CN      |
| 淘宝 APP      | CN      |
+--------------+---------+

```

19. 排序 order by
```
如果字符集采用的是 gbk(汉字编码字符集)，直接在查询语句后边添加 ORDER BY：
SELECT * 
FROM runoob_tbl
ORDER BY runoob_title;

如果字符集采用的是 utf8(万国码)，需要先对字段进行转码然后排序：
SELECT * 
FROM runoob_tbl
ORDER BY CONVERT(runoob_title using gbk);
```

20. 分组group by
```
SELECT name, COUNT(*) FROM   employee_tbl GROUP BY name;
```
使用 WITH ROLLUP
WITH ROLLUP 可以实现在分组统计数据基础上再进行相同的统计（SUM,AVG,COUNT…）。

例如我们将以上的数据表按名字进行分组，再统计每个人登录的次数：
```
mysql> SELECT name, SUM(signin) as signin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
+--------+--------------+
| name   | signin_count |
+--------+--------------+
| 小丽 |            2 |
| 小明 |            7 |
| 小王 |            7 |
| NULL   |           16 |
+--------+--------------+
4 rows in set (0.00 sec)
```
with rollup，前面执行的是sum操作，所以最后会再执行一次sum，计算总数

其中记录 NULL 表示所有人的登录次数。

我们可以使用 coalesce 来设置一个可以取代 NUll 的名称，coalesce 语法：
```
select coalesce(a,b,c);
参数说明：如果a==null,则选择b；如果b==null,则选择c；如果a!=null,则选择a；如果a b c 都为null ，则返回为null（没意义）。

以下实例中如果名字为空我们使用总数代替：

mysql> SELECT coalesce(name, '总数'), SUM(signin) as signin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
+--------------------------+--------------+
| coalesce(name, '总数') | signin_count |
+--------------------------+--------------+
| 小丽                   |            2 |
| 小明                   |            7 |
| 小王                   |            7 |
| 总数                   |           16 |
+--------------------------+--------------+
4 rows in set (0.01 sec)
```

21. as 和 coalesce
SELECT name, SUM(signin) as signin_count FROM  employee_tbl GROUP BY name WITH ROLLUP; -- sum as signin_count修改的是列名
SELECT coalesce(name, '总数'), SUM(signin) as signin_count FROM  employee_tbl GROUP BY name WITH ROLLUP; -- coalesce修改的是属性的名称，具体到单元格的内容

22. 连接
JOIN 按照功能大致分为如下三类：
（1）INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。
（2）LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
（3）RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。
（4）FULL JOIN（全连接）：只要一个表里有，就读出
（5）CROSS JOIN（笛卡尔连接）：求两表的笛卡尔积 -- A表的每一个元素，叉乘B表的每一个元素 -- A.1,A.2,B.01,B.02 = 1:01,1:02,2:01,2:02
写sql语句的时候，写在join关键字前面的，就是左表，写在后面的就是右表
```
SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a INNER JOIN tcount_tbl b ON a.runoob_author = b.runoob_author;

table a -- 表示给table重命名为a
join的条件使用on

上面的select语句，等价于
SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a, tcount_tbl b WHERE a.runoob_author = b.runoob_author;
```
join和union的区别：
join用于表的联合；union用于对表联合结果的处理 -- 需要不同表但同名同数据类型的数据的整理，union会去重，不去重使用union all

23. null的处理
mysql判断是否为null，使用is null和is not null来判断

24. 正则表达式
使用REGEXP为关键字
```
SELECT name FROM person_tbl WHERE name REGEXP '^st';
```

25. 事务
事务(Transaction)是并发控制的基本单位。所谓的事务呢，它是一个操作序列，这些操作要么都执行，要么都不执行，它是一个不可分割的工作单位。为什么?因为事务是数据库维护数据一致性的单位，在每一个事务结束的时候都能保持数据的一致性，如像积分表和积分详情表一起更新要么就成功，要么就失败。
事务的四大特性ACID
「原子性(Atomicity)：」 原子性是指整个数据库的事务是一个不可分割的工作单位，在每一个都应该是原子操作。当我们执行一个事务的时候，如果在一系列的操作中，有一个操作失败了，那么需要将这一个事务中的所有操作恢复到执行事务之前的状态，这就是事务的原子性。
「一致性(Consistency):」 一致性呢是指事务将数据库从一种状态转变成为下一种一致性的状态，也就是说是在事务的执行前后，这两种状态应该是一样的，也就是在数据库的完整性约束不会被破坏。另外的话，还需要注意的是一致性不关注中间的过程是发生了什么。
「隔离性(lsolation)：」 Mysql数据库可以同时的话启动很多的事务，但是呢，事务跟事务之间他们是相互分离的，也就是互不影响的，这就是事务的隔离性。
「持久性(Durability)：」 事务的持久性是指事务一旦提交，就是永久的了。说白了就是发生了问题，数据库也是可以恢复的。因此持久性保证事务的高可靠性。

26. 修改关键字alter
使用alter可以修改数据表的结构，例如添加外键等

27. 索引
https://cloud.tencent.com/developer/article/1543335
底层架构是红黑树，当节点不平衡时，会自动左旋或右旋并变色
哈希不适合做底层架构，是因为哈希会遇到数据碰撞，映射的地址是相同的，导致变成链表，数据很多的话链表会变长，降低查询效率
B树：B树相对于平衡二叉树，每个节点存储了更多的键值(key)和数据(data)，并且每个节点拥有更多的子节点，子节点的个数一般称为阶，上述图中的B树为3阶B树，高度也会很低。 
B+树：B+树非叶子节点上是不存储数据的，仅存储键值，而B树节点中不仅存储键值，也会存储数据。之所以这么做是因为在数据库中页的大小是固定的，innodb中页的默认大小是16KB。如果不存储数据，那么就会存储更多的键值，相应的树的阶数（节点的子节点树）就会更大，树就会更矮更胖，如此一来我们查找数据进行磁盘的IO次数有会再次减少，数据查询的效率也会更快。

总结来说，B树的叶子节点和非叶子节点，都可以储存数据；B+树的非叶子节点，只存储索引，叶子节点才会存储数据；大数查询只要两次IO -- 每个节点中，会存页的数据，读第一个节点，可以知道下一次读哪个节点中的页 -- 有点类似页码的功能。

29. 主键和索引的区别
主键和索引都是键，不过主键是逻辑键，索引是物理键，意思就是主键不实际存在，而索引实际存在在数据库中，主键一般都要建，主要是用来避免一张表中有相同的记录，索引一般可以不建，但如果需要对该表进行查询操作，则最好建，这样可以加快检索的速度。

30. having的用法
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
参数说明：

column1：要检索的列。
aggregate_function(column2)：一个聚合函数，例如SUM、COUNT、AVG等，应用于column2的值。
table_name：要从中检索数据的表。
GROUP BY column1：根据column1列的值对数据进行分组。
HAVING condition：一个条件，用于筛选分组的结果。只有满足条件的分组会包含在结果集中。

----- 注意：where后面加的是某一列的条件。having后面写的是行列表达式，需要计算的，计算的语句有比如sum、avr等
where 和having之后都是筛选条件，但是有区别的：
1.where在group by前， having在group by 之后
2.聚合函数（avg、sum、max、min、count），不能作为条件放在where之后，但可以放在having之后

31. distinct的用法
用于返回唯一不同的值，即去重。
SELECT DISTINCT country FROM Websites;

32. 常用语句
```
查询一组数中，出现一次的最大的数
select max(num) as num from (select num from table_name group by num having count(num) = 1);

首先找到只出现一次 -- group by num having count(num) = 1
再找到最大的 -- max（num）
```
