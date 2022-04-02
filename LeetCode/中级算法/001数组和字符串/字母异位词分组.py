#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字母异位词分组.py
# @Author: Lin
# @Date  : 2021/8/16 17:59
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        [dic[''.join(sorted(list(s)))].append(s) for s in strs]

        return [v for v in dic.values()]