import requests

print(requests.__version__)


url="https://www.google.com"
resp=requests.get(url)
print(resp)

pythonUrl=requests.get("https://raw.githubusercontent.com/WentaiDu/CMPUT404LAB/main/1.py")
print(pythonUrl.text)
