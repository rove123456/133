#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
辅助工具模块：提供基础工具函数
"""
import os

def get_work_dir():
    """获取当前工作目录"""
    return os.getcwd()

def calc(a, b):
    """简单计算函数"""
    return a + b
