import requests

params = {
    "key": "SaLNBYLfQGUvVe76B",
    "location": "ip",
    "language": "zh-Hans",
    "unit": "c",
}
url = "https://api.seniverse.com/v3/life/chinese_calendar.json?"

r = requests.get(url, params=params)

tem = r.json()["results"]
tem1 = tem['chinese_calendar'][0]

#print(tem1)


def text1():
    text = tem1['ganzhi_month'] + tem1['ganzhi_day']
    return text


def text2():
    text = tem1['lunar_month_name'] + tem1['lunar_day_name']
    return text




if __name__ == '__main__':
    print(text1())
    print(text2())
