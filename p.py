import requests
from bs4 import BeautifulSoup

# 定义要爬取的目标网址
url = 'https://www.runoob.com/'

# 发送HTTP GET请求并获取页面内容
response = requests.get(url)
content = response.content

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(content, 'html.parser')

# 在这里可以根据网页结构和需求进行相应的解析操作
# 例如，查找特定元素、提取数据等
# 这里以提取页面标题为例
title = soup.title.text

# 打印结果
print("页面标题:", title)