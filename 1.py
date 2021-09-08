import requests

print(requests.__version__)


url="https://www.google.com"
resp=requests.get(url)
print(resp)

pythonUrl=requests.get("https://github.com/WentaiDu/CMPUT404LAB/blob/main/1.py")
print(pythonUrl)
