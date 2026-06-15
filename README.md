# 大数据计算框架下自然语言处理的应用分析
学生：朱淑乔 学号：20233001549 班级：2023-3 指导教师：周腾 完成时间：2026.06.14

## 项目简介
在大数据技术快速发展的当下，网络中产生了大量非结构化中文文本数据，包括用户评论、社交言论、行业资讯等内容。传统单机模式下的自然语言处理程序受限于硬件资源，不仅存储容量有限、数据容错能力较差，而且串行计算方式处理效率低下，难以应对大批量文本分析、网络舆情监测等实际业务场景。

为解决以上问题，本项目结合主流大数据分布式计算框架与自然语言处理技术，搭建一套完整的分布式文本分析实验系统。项目基于 Hadoop 与 Spark 集群环境开展实验，使用真实多领域中文评论数据集，完整实现分布式数据存储、文本清洗、中文分词、停用词过滤、词频统计以及数据可视化等一系列功能。

在完成系统开发与功能测试的基础上，本项目进一步对比 Hadoop、Spark、Flink 三大主流大数据框架的架构特点、运行机制与适用场景，分析不同框架在自然语言处理任务中的优势与不足。通过理论结合实践的方式，探究大数据架构与自然语言处理技术融合的可行性与应用价值，顺利完成本次大数据编程课程设计的全部研究与实践任务。

## 技术栈
### 运行环境
操作系统：Ubuntu 24.04.3 LTS
Java 环境：JDK 1.8.0_202
分布式框架：Hadoop 2.7.7、Spark 2.4.8

### 开发环境
开发语言：Python 3.12.3

### 第三方依赖库
```
jieba==0.42.1
pandas==2.2.2   2.2.2熊猫= =
matplotlib==3.8.4
wordcloud==1.9.3   1.9.3 wordcloud = =
```

## 项目结构
本项目采用模块化分层设计思路，将配置文件、原始数据、业务代码、可视化程序、运行脚本进行拆分，各模块职责清晰、相互独立，降低代码耦合度，方便日常调试、后期维护与功能拓展。
```
BigData-NLP-Code/
├── config/   ├──problem /
│   └── config.py
├── data/
│   └── paper_text_data.csv
├── etl/
│   └── wordcount.py
├── visualization/   ├──可视化/
│   └── visual.py
├── scripts/   ├──脚本/
│   ├── run_etl.sh
│   └── run_visual.sh
├── requirements.txt
└── README.md
```

## 环境部署
### 1. 配置系统环境变量
集群运行前需要配置 Java、Hadoop、Spark 全局环境变量，保证系统可以在任意目录识别相关命令。
```bash   ”“bash
vim ~/.bashrc
```
在配置文件末尾添加如下内容：
```bash   ”“bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64出口JAVA_HOME = / usr / lib / jvm / java-8-openjdk-amd64
export HADOOP_HOME=/usr/local/hadoop出口HADOOP_HOME = / usr /地方/ hadoop
export SPARK_HOME=/usr/local/spark出口SPARK_HOME = / usr /地方/火花
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SPARK_HOME/bin导出路径= $路径:$ JAVA_HOME / bin: $ HADOOP_HOME / bin: $ HADOOP_HOME / sbin: $ SPARK_HOME / bin
```
保存文件后执行命令，使环境变量立即生效。
```bash   ”“bash
source ~/.bashrc   源~ / . bashrc
```

### 2. 安装 Python 依赖包
进入项目根目录，根据依赖清单批量安装项目运行所需要的第三方库。
```bash   ”“bash
cd ~/BigData-NLP-Code
pip3 install -r requirements.txtPip3 install -r requirements.txt
```

### 3. 集群启动与数据集上传
依次启动 HDFS 和 YARN 集群服务，查看集群运行进程确认启动正常。由于集群启动后会默认进入安全模式，需要手动退出安全模式才能进行文件写入操作。之后在 HDFS 中创建对应目录，并将本地数据集上传至分布式文件系统中。
```bash   ”“bash   “bash”;“bash
start-dfs.sh
start-yarn.sh
jps

hdfs dfsadmin -safemode leaveHDFS dfsadmin -safemode leave
hdfs dfs -mkdir -p /input/text_dataHDFS DFS -mkdir -p /input/text_data . txt
hdfs dfs -put ./data/paper_text_data.csv /input/text_data/HDFS DFS -put ./data/paper_text_data.csv /input/text_data/
hdfs dfs -ls /input/text_data/HDFS DFS -ls /input/text_data/
```

## 项目运行方式
本项目提供两种运行方式，分别为脚本一键运行和手动分步运行，可根据实际使用场景自由选择。

### 方式一：脚本一键执行
项目编写了自动化 Shell 脚本，无需切换多个目录，直接执行脚本即可完成词频统计与可视化全部流程，操作简单高效。
```bash   ”“bash
cd ~/BigData-NLP-Code/scriptscd ~ / BigData-NLP-Code /脚本
bash run_etl.sh
bash run_visual.sh
```

### 方式二：分步手动运行
手动进入对应模块目录执行代码，适合代码调试、分步查看运行状态与输出结果。
```bash   ”“bash
cd ~/BigData-NLP-Code/etl
python3 wordcount.py
```
```bash   ”“bash
cd ~/BigData-NLP-Code/visualizationcd ~ / BigData-NLP-Code /可视化
python3 visual.py
```

## 数据集说明
本次实验所使用的数据集为 paper_text_data.csv，数据集整体规范完整，数据来源为真实网络评论文本，能够有效模拟实际场景下的自然语言处理任务。

数据集基本信息如下：
数据总条数共计 1201 条中文评论，内容覆盖生活、职场、科技、娱乐、教育五大常见领域。数据集包含四个字段，分别为文本编号 text_id、评论文本 comment、所属领域 domain、情感标签 sentiment。

程序完整运行结束后，项目 data 目录下会生成三类输出文件，分别为词汇词频统计文本、高频词汇分布柱状图以及中文文本词云图，所有分析结果统一归档存放。

## 核心功能介绍
### 文本预处理
程序在读取数据集后，首先完成数据清洗工作，自动过滤 CSV 文件表头、空白行以及字段缺失的异常数据。随后调用 jieba 分词工具对中文文本进行分词处理，并过滤掉无实际语义的单字、助词、虚词等内容，保留有效词汇，提升后续统计与分析的准确性。

### 词频统计
在文本分词与过滤完成后，程序遍历全部词汇，统计每一个词汇在所有文本中出现的频次，并按照出现次数由高到低进行排序，最终将统计结果写入本地文本文件，形成完整的词频统计报表。

### 数据可视化
基于词频统计结果，使用绘图工具生成可视化图表。选取出现频率最高的二十个词汇绘制柱状图，直观展示高频词汇的分布情况；同时生成中文词云图，利用字体大小区分词汇出现频次，更加形象地呈现整体文本特征。

### 模块化管理
项目采用模块化开发思想，将全局配置、数据处理、可视化、运行脚本相互分离，结构清晰。在后期需要修改路径、调整分词规则、新增分析功能时，可以单独对应模块进行修改，不会影响其他功能正常运行，具备良好的拓展性与可维护性。

## 主流大数据框架应用场景分析
结合本次实验实践与相关理论知识，对目前三款主流大数据计算框架在自然语言处理领域的应用场景进行总结。

Hadoop 拥有成熟的分布式文件系统 HDFS 和离线批处理计算模型，系统稳定性强、容错性高、部署与运维难度低，更加适合海量历史文本、归档语料的存储与离线批量分析，是传统离线文本挖掘任务的主流选择。

Spark 采用内存计算模式，有效减少磁盘反复读写带来的性能损耗，在多轮迭代计算场景中优势明显，运行速度远高于 Hadoop，适用于精细化文本挖掘、特征筛选、准实时文本分析等场景。

Flink 主打低延迟流式计算，能够持续接收并处理不间断的数据流，主要应用在实时评论分析、网络动态舆情监控、在线内容识别等对时效性要求较高的自然语言处理业务中。

三款框架技术定位各不相同，优势互补，在实际工程中可以根据数据规模、任务时效要求进行组合使用。

## 常见问题与解决方案
### HDFS 无法创建目录、上传文件
集群启动后默认开启安全模式，该模式下禁止所有文件写入操作。执行以下命令退出安全模式即可。
```bash   ”“bash   “bash”;“bash
hdfs dfsadmin -safemode leaveHDFS dfsadmin -safemode leave
```

### 运行代码提示缺少第三方库
程序运行依赖 jieba、pandas、matplotlib 等工具库，若环境未完整配置则会报错，重新批量安装依赖即可。
```bash   ”“bash   “bash”;“bash
cd ~/BigData-NLP-Code
pip3 install -r requirements.txtPip3 install -r requirements.txtPip3安装-r要求。txtPip3 install -r requirements.txt
```

### 图表中文显示乱码
柱状图与词云出现中文方框乱码，原因为系统缺少对应中文字体，或是代码内字体路径与本机实际路径不匹配。解决方式为安装中文字体，并修改 config.py 文件中的字体路径参数。

### 程序提示文件路径不存在
读取数据集或写入结果时提示路径错误，一般是相对路径书写错误、HDFS 目录未创建导致。仔细核对 config.py 中所有本地路径与分布式路径，缺失目录则重新创建。

### Spark 与 Python 版本不兼容
当前使用的 Spark 版本对高版本 Python 兼容性较差，直接混用会导致启动报错。建议使用 Python 虚拟环境进行版本隔离，不改动系统全局默认环境。

## 项目总结
本次课程设计围绕大数据计算框架下自然语言处理的应用分析这一主题展开，完整完成了分布式集群环境搭建、环境变量配置、数据集部署、文本分词、词频统计、可视化展示等全部实验流程。

通过本次实践可以明显看出，基于分布式大数据架构的自然语言处理系统，在存储能力、数据安全、并行计算效率等方面，相比传统单机程序有着巨大优势，能够很好地解决海量文本处理过程中遇到的各类问题。同时在实验过程中，逐步排查并解决了集群安全模式、依赖缺失、中文乱码、路径错误、版本兼容等一系列典型问题，积累了大数据集群运维与 Python 文本开发的实践经验。

本项目目前主要实现了离线文本词频分析功能，整体架构具备良好的拓展空间。在后续优化中，可以进一步结合 Spark 实现真正的分布式并行计算，扩充停用词库优化文本清洗效果，新增文本情感分析、文本分类等高级自然语言处理功能，也可以对接 Flink 框架实现实时文本流分析，不断丰富系统功能，让项目更加完善。
