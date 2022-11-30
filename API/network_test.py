import requests
import time


def test():
    url = 'https://www.seniverse.com/dashboard'
    response = requests.get(url)


time.sleep(0.5)

if __name__ == '__main__':
    test()
    print("网络连接正常")
    # except:
    #     print("网络异常")
