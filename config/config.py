#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 项目全局路径与参数配置

# 本地文件路径
LOCAL_CSV_DATA = "../data/paper_text_data.csv"
LOCAL_WORDCOUNT_RESULT = "../data/word_count_result.txt"
BAR_CHART_PATH = "../data/top20_bar.png"
WORDCLOUD_PATH = "../data/wordcloud.png"

# 可视化相关参数
CHINESE_FONT = "/home/zsq/.local/share/fonts/wqy/wqy-microhei.ttc"
IMAGE_DPI = 300
TOP_N = 20

# HDFS 分布式路径
HDFS_INPUT_DIR = "/input/text_data"
HDFS_OUTPUT_DIR = "/output/wordcount"
