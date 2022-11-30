import random
"""
随机返回谚语

"""
f = open("/home/reb/Desktop/My_magic/saying.txt", "r", encoding="UTF-8")

for line in f:
    # print(f"{line}")
    saying = []
    saying.extend(f.readlines())

f.close()


def saying_ran():
    sum = len(saying)
    r = random.randint(0, sum - 1)
    tem_saying = saying[r]
    tem_saying = tem_saying.split("\n")
    saying_ran = tem_saying[0]
    #print (r)
    return saying_ran


if __name__ == '__main__':
    #print(type(saying_ran()))
    print(saying_ran())
