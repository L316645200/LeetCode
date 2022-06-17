#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第 1 天 选择.py
# @Author: Lin
# @Date  : 2022/5/6 17:49
#
# World 表：
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | name        | varchar |
# | continent   | varchar |
# | area        | int     |
# | population  | int     |
# | gdp         | int     |
# +-------------+---------+
# name 是这张表的主键。
# 这张表的每一行提供：国家名称、所属大陆、面积、人口和 GDP 值。
# 如果一个国家满足下述两个条件之一，则认为该国是 大国 ：
# 面积至少为 300 平方公里（即，3000000 km2），或者
# 人口至少为 2500 万（即 25000000）
# 编写一个 SQL 查询以报告 大国 的国家名称、人口和面积。
# 按 任意顺序 返回结果表。
# 查询结果格式如下例所示。
# 示例：
# 输入：
# World 表：
# +-------------+-----------+---------+------------+--------------+
# | name        | continent | area    | population | gdp          |
# +-------------+-----------+---------+------------+--------------+
# | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
# | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
# | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
# | Andorra     | Europe    | 468     | 78115      | 3712000000   |
# | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
# +-------------+-----------+---------+------------+--------------+
# 输出：
# +-------------+------------+---------+
# | name        | population | area    |
# +-------------+------------+---------+
# | Afghanistan | 25500100   | 652230  |
# | Algeria     | 37100000   | 2381741 |
# +-------------+------------+---------+

# Write your MySQL query statement belowS
SQL = """SELECT name,population,area FROM World WHERE area>=3000000 or population>=25000000;"""


# 1757. 可回收且低脂的产品
# 表：Products
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | low_fats    | enum    |
# | recyclable  | enum    |
# +-------------+---------+
# product_id 是这个表的主键。
# low_fats 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品是低脂产品，'N' 表示不是低脂产品。
# recyclable 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品可回收，而 'N' 表示不可回收。
# 写出 SQL 语句，查找既是低脂又是可回收的产品编号。
# 返回结果 无顺序要求 。
# 查询结果格式如下例所示：
# Products 表：
# +-------------+----------+------------+
# | product_id  | low_fats | recyclable |
# +-------------+----------+------------+
# | 0           | Y        | N          |
# | 1           | Y        | Y          |
# | 2           | N        | Y          |
# | 3           | Y        | Y          |
# | 4           | N        | N          |
# +-------------+----------+------------+
# Result 表：
# +-------------+
# | product_id  |
# +-------------+
# | 1           |
# | 3           |
# +-------------+
# 只有产品 id 为 1 和 3 的产品，既是低脂又是可回收的产品。

# Write your MySQL query statement below
SQL = """SELECT product_id  FROM Products WHERE low_fats='Y' and recyclable ='Y';"""


# 584. 寻找用户推荐人
# 给定表 customer ，里面保存了所有客户信息和他们的推荐人。
# +------+------+-----------+
# | id   | name | referee_id|
# +------+------+-----------+
# |    1 | Will |      NULL |
# |    2 | Jane |      NULL |
# |    3 | Alex |         2 |
# |    4 | Bill |      NULL |
# |    5 | Zack |         1 |
# |    6 | Mark |         2 |
# +------+------+-----------+
# 写一个查询语句，返回一个客户列表，列表中客户的推荐人的编号都 不是 2。
# 对于上面的示例数据，结果为：
# +------+
# | name |
# +------+
# | Will |
# | Jane |
# | Bill |
# | Zack |
# +------+

SQL = """SELECT name FROM customer  WHERE referee_id<>2 or referee_id is null;"""


# 183. 从不订购的客户
# 某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。
# Customers 表：
# +----+-------+
# | Id | Name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders 表：
# +----+------------+
# | Id | CustomerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# 例如给定上述表格，你的查询应返回：
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+

# Write your MySQL query statement below

SQL = """SELECT Name as Customers FROM Customers
WHERE Id not in (SELECT DISTINCT CustomerId FROM Orders )"""


