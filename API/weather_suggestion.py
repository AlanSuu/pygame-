import requests


def suggestion():
    params = {
        "key": "SNkNmj-mzUNBsc1OU",
        "location": "ip",  # 查询地点设置为访问IP所在地
        "language": "zh-Hans",
        "unit": "c",
    }

    url = "https://api.seniverse.com/v3/life/suggestion.json?"

    # 获取数据
    r = requests.get(url, params=params)

    # # 解析数据
    tem = r.json()["results"]

    data = tem[0]

    tem_message = data["suggestion"]
    tem_key = "brief"

    # # #获取所需数据
    message = {
        "穿衣": tem_message["dressing"][tem_key],
        "感冒": tem_message["flu"][tem_key],
        "运动": tem_message["sport"][tem_key],
        "紫外线": tem_message["uv"][tem_key]
    }

    return message


if __name__ == '__main__':
    print(suggestion())
    print(type(suggestion()))
