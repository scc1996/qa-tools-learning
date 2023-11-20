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

20. 
