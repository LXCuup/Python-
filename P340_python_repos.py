import requests
import json

# 执行API调用并存储响应
url = 'https://api.GitHub.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.Status_code)

# 将API响应存储在一个变量中
response_dict = r.json()

# 处理结果
print(response_dict.keys())