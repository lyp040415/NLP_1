import matplotlib.pyplot as plt
from collections import Counter
import jieba
import re

# 设置中文字体显示（确保系统中存在SimHei字体）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 

with open("wiki_texts.txt", "r", encoding="utf-8") as f:
    chinese_text = f.read()

import re

def preprocess_chinese_text(text):
    text = re.sub(r'\s+', '', text)
    text = re.sub(r'[^\w\s\u4e00-\u9fff]', '', text)
    text = re.sub(r'[^\u4e00-\u9fff]', '', text)
    return text

cleaned_text = preprocess_chinese_text(chinese_text)

chinese_chars = [char for char in cleaned_text if '\u4e00' <= char <= '\u9fff']  # 仅保留汉字
char_freq = Counter(chinese_chars).most_common(50)

chinese_words = list(jieba.cut(cleaned_text))
word_freq = Counter(chinese_words).most_common(50)

plt.figure(figsize=(20, 15))

x = [char[0] for char in char_freq]
y = [char[1] for char in char_freq]
plt.bar(x, y, color='skyblue')
plt.title("中文字符频率分布（Top 50）")
plt.xlabel("汉字")
plt.ylabel("出现次数")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(20, 15))

x = [word[0] for word in word_freq]
y = [word[1] for word in word_freq]
plt.bar(x, y, color='lightgreen')
plt.title("中文词汇频率分布（Top 50）")
plt.xlabel("词汇")
plt.ylabel("出现次数")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
