
import requests

params = {
        "key": "SaLNBYLfQGUvVe76B",
        "location": "ip",
        "language": "zh-Hans",
        "unit": "c",
    }

url = "https://api.seniverse.com/v3/weather/hourly.json?"

s = requests.session()
s.keep_alive = False  # 关闭多余连接

r = requests.get(url, params=params)

tem = r.json()["results"]
tem1 = tem[0]["hourly"]

print(tem1)

# for i in tem1:
#     for key in i:




