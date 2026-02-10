#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python仓库核心执行文件：演示基础功能+调用辅助模块
"""
import sys
import utils  # 导入自定义辅助模块

def main():
    """主执行函数"""
    print("===== Python 仓库执行成功 =====")
    print(f"Python 版本：{sys.version}")
    print(f"当前工作目录：{utils.get_work_dir()}")
    print("执行自定义任务：计算 10+20 =", utils.calc(10, 20))
    print("===== 执行结束 =====")

if __name__ == "__main__":
    main()
