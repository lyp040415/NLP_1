import matplotlib.pyplot as plt
from collections import Counter
import jieba

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 1. 加载数据（示例数据）
# 英文文本（以Gutenberg语料库中的《爱玛》为例）
from nltk.corpus import gutenberg
english_text = gutenberg.raw("austen-emma.txt")
english_words = gutenberg.words("austen-emma.txt")


# 2. 统计频率
# 英文字母频率（全部26个）
english_letters = [char.lower() for char in english_text if char.isalpha()]
letter_freq = sorted(Counter(english_letters).items(), key=lambda x: x[1], reverse=True)

# 英文词汇频率（前50）
english_words = [word.lower() for word in english_words if word.isalpha()]
english_word_freq = Counter(english_words).most_common(50)

# 3. 绘制直方图
plt.figure(figsize=(20, 15))

# 英文字母直方图（全部26个）
x = [letter[0].upper() for letter in letter_freq]
y = [letter[1] for letter in letter_freq]
plt.bar(x, y, color='orange')
plt.title("英文字母频率分布（全部26个）")
plt.xlabel("字母")
plt.ylabel("出现次数")
plt.show()

plt.figure(figsize=(20, 15))

# 英文词汇直方图（前50）
x = [word[0] for word in english_word_freq]
y = [word[1] for word in english_word_freq]
plt.bar(x, y, color='pink')
plt.title("英文词汇频率分布（Top 50）")
plt.xlabel("单词")
plt.ylabel("出现次数")
plt.xticks(rotation=45)

# 调整布局
plt.show()