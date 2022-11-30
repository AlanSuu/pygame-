import requests



params = {
    "key": "SNkNmj-mzUNBsc1OU",
    "location": "ip",  # 查询地点设置为访问IP所在地
    "language": "zh-Hans",
    "unit": "c",
}

url = "https://api.seniverse.com/v3/weather/daily.json?"

s = requests.session()
s.keep_alive = False  # 关闭多余连接
# 获取数据
r = requests.get(url, params=params)

# # 解析数据

tem = r.json()["results"]

 


def locadtion():  # 获取位置
    location = tem[0]["location"]["name"]
    return location


def daily1():  # 获取今天预报
    tem_daily1 = tem[0]["daily"][0]
    daily1 = {
            "code_day": tem_daily1["code_day"],
            "low": tem_daily1["low"] + "°c",
            "high": tem_daily1["high"] + "°c"
    }
    return daily1


def daily2():  # 获取明天预报
    tem_daily2 = tem[0]["daily"][1]
    daily2 = {
        "code_day": tem_daily2["code_day"],
        "low": tem_daily2["low"] + "°c",
        "high": tem_daily2["high"] + "°c"
    }
    return daily2


def daily3():  # 获取后天预报
    tem_daily3 = tem[0]["daily"][2]
    daily3 = {
        "code_day": tem_daily3["code_day"],
        "low": tem_daily3["low"] + "°c",
        "high": tem_daily3["high"] + "°c"
    }
    return daily3


if __name__ == '__main__':
    print(locadtion())
    print(daily1())
    print(daily2())
    print(daily3())
