#!/usr/bin/env python3   #！/usr/bin/env python3
# -*- coding: utf-8 -*-# -*-编码：utf-8 -*-
# 词频数据可视化：柱状图 + 中文词云

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import sys   导入系统
sys.path.append("../config")sys.path.append("../config")

from config import (
    LOCAL_WORDCOUNT_RESULT,
    BAR_CHART_PATH,
    WORDCLOUD_PATH,
    CHINESE_FONT,
    IMAGE_DPI,
    TOP_N
)

def draw_bar_chart(df):
    # 绘制Top20词频柱状图
    top_data = df.head(TOP_N)
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(top_data)), top_data["count"])
    plt.title("Top 20 Word Frequency Statistics")
    plt.xlabel("Word Serial Number")
    plt.ylabel("Occurrence Frequency")
    plt.xticks(range(len(top_data)))
    plt.tight_layout()
    plt.savefig(BAR_CHART_PATH, dpi=IMAGE_DPI)
    plt.close()
    print("柱状图生成成功")

def create_word_cloud(df):
    # 生成中文词云
    full_text = ""
    for _, row in df.iterrows():
        full_text += (row["word"] + " ") * row["count"]

    wc = WordCloud(
        font_path=CHINESE_FONT,
        width=800,
        height=400,
        background_color="white"
    )
    wc.generate(full_text)
    wc.to_file(WORDCLOUD_PATH)
    print("词云图生成成功")

def main():
    # 读取词频结果文件
    df = pd.read_csv(LOCAL_WORDCOUNT_RESULT, names=["word", "count"])
    draw_bar_chart(df)
    create_word_cloud(df)
    print("===== 全部可视化任务完成 =====")

if __name__ == "__main__":   如果__name__ == "__main__"；
    main()
