import requests


def now():
    params = {
        "key": "SNkNmj-mzUNBsc1OU",
        "location": "ip",  # 查询地点设置为访问IP所在地
        "language": "zh-Hans",
        "unit": "c",
    }

    url = "https://api.seniverse.com/v3/weather/now.json"

    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    # 获取数据
    r = requests.get(url, params=params)

    # # 解析数据
    tem = r.json()["results"]

    data = tem[0]  # 数据转化为字典

    global message
    message = data["now"]
    return message

def text():
    tem_text = now()
    text = tem_text["text"]
    return text


def code():
    tem_code = now()
    code = tem_code["code"]
    return code


def temperature():
    tem_temperature = now()
    temperature = tem_temperature["temperature"] + " °c"
    return temperature


if __name__ == '__main__':
    print(now())
    print(text())
    print(code())
    print(temperature())
