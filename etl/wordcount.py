#!/usr/bin/env python3   #！/usr/bin/env python3
# -*- coding: utf-8 -*-# -*-编码：utf-8 -*-
# 文本分词、清洗与词频统计

import jieba
import sys
sys.path.append("../config")
from config import LOCAL_CSV_DATA, LOCAL_WORDCOUNT_RESULT

def main():
    word_frequency = dict()

    # 读取原始数据集
    with open(LOCAL_CSV_DATA, "r", encoding="utf-8") as f:
        lines = f.readlines()
        # 跳过表头，逐行处理数据
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            # 按逗号分割字段，避免文本内逗号干扰
            parts = line.split(",", 3)
            if len(parts) < 2:
                continue
            content = parts[1]

            # 中文分词
            words = jieba.lcut(content)
            # 过滤单字，只保留有效词汇
            for word in words:
                if len(word) > 1:
                    word_frequency[word] = word_frequency.get(word, 0)+1

    # 按词频从高到低排序
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    # 写入统计结果
    with open(LOCAL_WORDCOUNT_RESULT, "w", encoding="utf-8") as f:
        for k, v in sorted_words:
            f.write(f"{k},{v}\n")

    print("词频统计完成，结果已输出至data目录")

if __name__ == "__main__":
    main()
