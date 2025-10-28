from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
import random

# 设置中文字体
font_path = './正风毛笔体MasaFont-Medium.ttf'

# 加载云形蒙版图片
background_Image = np.array(Image.open(r"C:\Users\calvi\Desktop\cloud.jpg"))

# 自定义颜色函数
def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # 使用中国传统颜色
    colors = ['#8C2318', '#5E8C6A', '#88A550', '#BFB35A', '#F2C45A', 
              '#D9A566', '#D98E4C', '#BF6D4E', '#734044', '#023E73']
    return random.choice(colors)

# 创建词云对象
wc = WordCloud(
    width=1200,
    height=1200,
    background_color='white',
    scale=5,
    mask=background_Image,
    font_path=font_path,
    color_func=custom_color_func,
    max_words=100,
    relative_scaling=0.8,
    prefer_horizontal=0.7,
    min_font_size=10,
    max_font_size=150,
    collocations=False
)

# 读取CSV数据
data = pd.read_csv(r'C:\Users\calvi\Desktop\论语_道cluster.csv')

# 数据清洗和准备
data = data.dropna(subset=['Word'])
data['Word'] = data['Word'].str.strip()

# 创建频率字典
word_freq = dict(zip(data['Word'], data['Frequency']))

# 生成词云
word_cloud = wc.generate_from_frequencies(word_freq)

# 保存和显示词云
output_path = r"C:\Users\calvi\Desktop\论语_道字词云.jpg"
word_cloud.to_file(output_path)

plt.figure(figsize=(16, 12))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.title('《道德经》"道"字词汇云图', fontsize=20, pad=20, fontproperties=plt.matplotlib.font_manager.FontProperties(fname=font_path))
plt.tight_layout()
plt.show()