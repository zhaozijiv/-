import requests
from bs4 import BeautifulSoup

# 设置请求的URL
url = 'https://en.wikipedia.org/wiki/Web_scraping'

# 发送HTTP请求
response = requests.get(url)

# 确认请求成功
if response.status_code == 200:
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 定位到页面的第一个段落
    first_paragraph = soup.find('p')
    
    # 打印段落的文本内容
    print(first_paragraph.text)
else:
    print(f"Error: Status code {response.status_code}")

