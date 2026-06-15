#!/bin/bash
# 执行文本分词与词频统计
echo "===== 开始执行文本分词 & 词频统计 ====="
cd ../etl
python3 wordcount.py
echo "===== 词频统计任务执行完成 ====="
