#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 36. 有效的数独.py
# @Author: Lin
# @Date  : 2021/9/17 18:47
# 请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
#
# 注意：
#
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
#  
#
# 示例 1：
#
#
# 输入：board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：true
# 示例 2：
#
# 输入：board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：false
# 解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
#  
#
# 提示：
#
# board.length == 9
# board[i].length == 9
# board[i][j] 是一位数字或者 '.'
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: [] for i in range(9)}
        column = {i: [] for i in range(9)}
        block = {i: [] for i in range(9)}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                n = i // 3 * 3 + j // 3
                if num != '.':
                    if num not in row[i]:
                        row[i].append(num)
                    else:
                        return False
                    if num not in column[j]:
                        column[j].append(num)
                    else:
                        return False
                    if num not in block[n]:
                        block[n].append(num)
                    else:
                        return False
        return True


s = Solution()
res = s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print(res)
