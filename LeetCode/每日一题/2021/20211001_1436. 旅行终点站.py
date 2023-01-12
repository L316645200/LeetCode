#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 20211001_1436. 旅行终点站.py
# @Author: Lin
# @Date  : 2021/10/2 11:38
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citiesA = [p[0] for p in paths]
        return [path[1] for path in paths if path[1] not in citiesA][0]


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path = [p[0] for p in paths]
        for p in paths:
            if p[1] not in path:
                return p[1]

