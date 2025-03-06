import matplotlib.pyplot as plt
from collections import Counter
import jieba
import re
import os

# 设置中文字体显示（确保系统中存在SimHei字体）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 1. 加载停用词列表
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        stopwords = set(line.strip() for line in f)  # 使用集合提高查询效率
    return stopwords

stopwords = load_stopwords('cn_stopwords.txt')

# 2. 预处理中文文本
def preprocess_chinese_text(text):
    # 去除空格、标点符号和非中文字符
    text = re.sub(r'\s+', '', text)  # 去空格
    text = re.sub(r'[^\u4e00-\u9fff]', '', text)  # 仅保留汉字
    return text

# 3. 分块处理文件（带进度显示）
def process_text_in_chunks(file_path, chunk_size=1024 * 1024 * 5):  # 默认块大小为1MB
    word_freq = Counter()  # 全局词频统计
    total_size = os.path.getsize(file_path)  # 文件总大小
    processed_size = 0  # 已处理的字节数

    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)  # 读取一块内容
            if not chunk:  # 如果读取完毕，退出循环
                break

            # 更新已处理的字节数
            processed_size += len(chunk.encode('utf-8'))  # 按字节计算

            # 预处理文本
            cleaned_text = preprocess_chinese_text(chunk)

            # 分词并过滤停用词
            words = list(jieba.cut(cleaned_text))
            filtered_words = [word for word in words if word not in stopwords]

            # 更新全局词频统计
            word_freq.update(filtered_words)

            # 计算并显示进度
            progress = (processed_size / total_size) * 100
            print(f"处理进度: {progress:.2f}%", end='\r')  # 覆盖当前行

    print("\n处理完成！")  # 换行显示完成信息
    return word_freq

# 4. 处理文件并统计词频
file_path = "wiki_texts_all.txt"  # 文件路径
word_freq = process_text_in_chunks(file_path)

# 5. 获取前50个高频词
top_50_words = word_freq.most_common(50)

# 6. 绘制直方图
plt.figure(figsize=(12, 8))
x = [word[0] for word in top_50_words]  # 词汇
y = [word[1] for word in top_50_words]  # 频率

plt.bar(x, y, color='skyblue')
plt.title("中文词频分布（Top 50）", fontsize=16)
plt.xlabel("词汇", fontsize=14)
plt.ylabel("出现次数", fontsize=14)
plt.xticks(rotation=45, fontsize=12)  # 旋转x轴标签
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加网格线
