import pygame  # 声明入需要的模块
import time
import API.weather_suggestion
import API.weather_now
import API.weather_daily
import API.saying
import API.network_test
import API.chinese_calendar
from pygame.locals import *
from sys import exit

pygame.init()  # 初始化pygame

global fps
global patch
global screenRect
global patch1

fps = pygame.time.Clock()  # 创建时间对象

COUNT = pygame.USEREVENT + 1  # 定义计时事件
pygame.time.set_timer(COUNT, 900000)  # 设定刷新时间（毫秒）

size = (768, 1360)  # 窗口大小
BLACK = (1, 1, 1)  # 背景颜色 黑
WHITE = (255, 255, 255)  # 文本颜色 白
UItest = (200, 200, 80)  # UI测试颜色
screen = pygame.display.set_mode(size, NOFRAME)  # 创建窗口
screen.fill(BLACK)  # 设置背景
screenRect = screen.get_rect()
patch = '/home/reb/Desktop/My_magic/word stock/苹方黑体-中黑-简.ttf'  # 字体文件路径
patch1 = "/home/reb/Desktop/My_magic/white/"  # 图标路径


pygame.display.set_caption('魔镜')  # 设置窗口的标题


def disconnect():
    disconnect_patch = "/home/reb/Desktop/My_magic/2.png"  # wifi图标位置文件位置
    disconnect = pygame.image.load(disconnect_patch)
    disconnect_rect = disconnect.get_rect()
    disconnect_rect.x = 700
    disconnect_rect.y = 1250
    screen.blit(disconnect, disconnect_rect)
    pygame.display.update()


def imageNow():  # 实时天气图标
    global image_rect
    core1 = API.weather_now.code() + "@2x.png"  # 获取天气图标代码
    image_path = patch1 + core1  # 文件路径
    image = pygame.image.load(image_path)  # 载入实时天气图标
    image_rect = image.get_rect()  # 获取天气图标rect
    image_rect.x = screenRect.x + 480  # 图标位置
    image_rect.y = screenRect.y + 20
    screen.blit(image, image_rect)  # 绘制实时天气图标
    #print(f"天气：{image_rect}")


def temperatreNow():  # 实时气温

    global temperatureNow_imageRect
    path1 = pygame.font.Font(patch, 50)  # 字体路径
    temperatureNow = API.weather_now.temperature()  # 获取实时气温
    temperatureNow_image = path1.render(temperatureNow, True, WHITE, BLACK)  # 生成字体图像
    temperatureNow_imageRect = temperatureNow_image.get_rect()  # 获取rect
    temperatureNow_imageRect.x = image_rect.x + image_rect.width + 10  # 位置
    temperatureNow_imageRect.y = image_rect.y
    screen.blit(temperatureNow_image, temperatureNow_imageRect)

def lunar():
    
    path0 = pygame.font.Font(patch, 25)
    lunarYear = API.chinese_calendar.text1()
    lunarYear_image = path0.render(lunarYear,True,WHITE, BLACK)
    lunarYear_imageRect = lunarYear_image.get_rect()
    lunarYear_imageRect.x = screenRect.x + 20
    lunarYear_imageRect.y = screenRect.y + 20
    screen.blit(lunarYear_image, lunarYear_imageRect)
    
    path4 = pygame.font.Font(patch, 50)
    lunarDay = API.chinese_calendar.text2()
    lunarDay_image= path4.render(lunarDay,True,WHITE, BLACK)
    lunarDay_imageRect =  lunarDay_image.get_rect()
    lunarDay_imageRect.x= screenRect.x + 20
    lunarDay_imageRect.y = lunarYear_imageRect.y + lunarYear_imageRect.height
    screen.blit(lunarDay_image, lunarDay_imageRect )
    
    print(lunarDay_imageRect)
    


def suggestion():  # 生活指数

    suggestion = API.weather_suggestion.suggestion()  # 建议
    pygame.draw.aaline(screen, WHITE, (20, 127), (300, 127), 1)
    
    path0 = pygame.font.Font(patch, 18)  # 字体大小
    dressing = "穿衣：" + suggestion["穿衣"]
    dressing_image = path0.render(dressing, True, WHITE, BLACK)
    dressing_imageRect = dressing_image.get_rect()
    dressing_imageRect.x = screenRect.x + 20  # 第一列信息位置
    dressing_imageRect.y = screenRect.y + 135
    screen.blit(dressing_image, dressing_imageRect)

    sport = "运动：" + suggestion["运动"]
    sport_image = path0.render(sport, True, WHITE, BLACK)
    sport_imageRect = sport_image.get_rect()
    sport_imageRect.x = screenRect.x + 180  # 第二列信息位置
    sport_imageRect.y = screenRect.y + 135
    screen.blit(sport_image, sport_imageRect)

    global flu_imageRect
    flu = "感冒：" + suggestion["感冒"]
    flu_image = path0.render(flu, True, WHITE, BLACK)
    flu_imageRect = flu_image.get_rect()
    flu_imageRect.x = dressing_imageRect.x
    flu_imageRect.y = dressing_imageRect.y + dressing_imageRect.height
    screen.blit(flu_image, flu_imageRect)

    UV = "U V ：" + suggestion["紫外线"]
    UV_image = path0.render(UV, True, WHITE, BLACK)
    UV_imageRect = UV_image.get_rect()
    UV_imageRect.x = sport_imageRect.x
    UV_imageRect.y = flu_imageRect.y
    screen.blit(UV_image, UV_imageRect)


def daily():

    pygame.draw.aaline(screen, WHITE, (480, 150), (728, 150), 1)  # 天气分割线
    patch3 = pygame.font.Font(patch, 25)

    text1 = "今天"
    text1_image = patch3.render(text1, True, WHITE, BLACK)
    text1_imageRect = text1_image.get_rect()
    text1_imageRect.x = 480  # 天气预报位置
    text1_imageRect.y = 155
    screen.blit(text1_image, text1_imageRect)

    text2 = "明天"
    text2_image = patch3.render(text2, True, WHITE, BLACK)
    text2_imageRect = text2_image.get_rect()
    text2_imageRect.x = text1_imageRect.x + text1_imageRect.width + 50  # 天气预报间隔 50
    text2_imageRect.y = 155
    screen.blit(text2_image, text2_imageRect)

    text3 = "后天"
    text3_image = patch3.render(text3, True, WHITE, BLACK)
    text3_imageRect = text3_image.get_rect()
    text3_imageRect.x = text2_imageRect.x + text2_imageRect.width + 50  # 天气预报间隔 50
    text3_imageRect.y = 155
    screen.blit(text3_image, text3_imageRect)

    daily1 = API.weather_daily.daily1()  # 今天天气预报
    core1 = daily1["code_day"] + "@1x.png"  # 图标
    image_path1 = patch1 + core1
    image1 = pygame.image.load(image_path1)
    image_rect1 = image1.get_rect()
    image_rect1.midtop = text1_imageRect.midbottom
    screen.blit(image1, image_rect1)

    daily2 = API.weather_daily.daily2()  # 明天天气预报
    core2 = daily2["code_day"] + "@1x.png"  # 图标
    image_path2 = patch1 + core2
    image2 = pygame.image.load(image_path2)
    image_rect2 = image2.get_rect()
    image_rect2.midtop = text2_imageRect.midbottom
    screen.blit(image2, image_rect2)

    daily3 = API.weather_daily.daily3()  # 后天天气预报
    core3 = daily3["code_day"] + "@1x.png"  # 图标
    image_path3 = patch1 + core3
    image3 = pygame.image.load(image_path3)
    image_rect3 = image3.get_rect()
    image_rect3.midtop = text3_imageRect.midbottom
    screen.blit(image3, image_rect3)

    tempLow1 = daily1["low"]  # 今天最低温度
    tepmLow1_image = patch3.render(tempLow1, True, WHITE, BLACK)
    tempLow1Rect = tepmLow1_image.get_rect()
    tempLow1Rect.midtop = image_rect1.midbottom
    screen.blit(tepmLow1_image, tempLow1Rect)

    tempLow2 = daily2["low"]  # 明天最低温度
    tepmLow2_image = patch3.render(tempLow2, True, WHITE, BLACK)
    tempLow2Rect = tepmLow2_image.get_rect()
    tempLow2Rect.midtop = image_rect2.midbottom
    screen.blit(tepmLow2_image, tempLow2Rect)

    tempLow3 = daily3["low"]  # 后天最低温度
    tepmLow3_image = patch3.render(tempLow3, True, WHITE, BLACK)
    tempLow3Rect = tepmLow3_image.get_rect()
    tempLow3Rect.midtop = image_rect3.midbottom
    screen.blit(tepmLow3_image, tempLow3Rect)

    tempHigh1 = daily1["high"]  # 最高温度
    tepmHigh1_image = patch3.render(tempHigh1, True, WHITE, BLACK)
    tempHigh1Rect = tepmHigh1_image.get_rect()
    tempHigh1Rect.midtop = tempLow1Rect.midbottom
    screen.blit(tepmHigh1_image, tempHigh1Rect)

    tempHigh2 = daily2["high"]  # 最高温度
    tepmHigh2_image = patch3.render(tempHigh2, True, WHITE, BLACK)
    tempHigh2Rect = tepmHigh2_image.get_rect()
    tempHigh2Rect.midtop = tempLow2Rect.midbottom
    screen.blit(tepmHigh2_image, tempHigh2Rect)

    tempHigh3 = daily3["high"]  # 最高温度
    tepmHigh3_image = patch3.render(tempHigh3, True, WHITE, BLACK)
    tempHigh3Rect = tepmHigh3_image.get_rect()
    tempHigh3Rect.midtop = tempLow3Rect.midbottom
    screen.blit(tepmHigh3_image, tempHigh3Rect)


def textNow():  # 位置 + 天气文本
    path2 = pygame.font.Font(patch, 20)  # 字体路径
    text = API.weather_daily.locadtion() + " " + API.weather_now.text()
    text_image = path2.render(text, True, WHITE, BLACK)
    text_imageRect = text_image.get_rect()
    text_imageRect.x = image_rect.x + image_rect.width + 10
    text_imageRect.y = image_rect.y + temperatureNow_imageRect.height
    screen.blit(text_image, text_imageRect)


def showTime(fontObj, text, x, y):  # 显示时间
    global textRectObj
    textSurfaceObj = fontObj.render(text, True, WHITE, BLACK)  # 配置要显示的文字
    textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
    textRectObj.center = (x, y)  # 设置显示对象的坐标
    screen.blit(textSurfaceObj, textRectObj)  # 绘制字体


fontbigObj = pygame.font.Font(patch, 48)  # 时间字体文件路径


def date():  # 日期
    global date_imageRec
    path3 = pygame.font.Font(patch, 20)
    date = time.strftime("%B %d, %Y %A", time.localtime())
    date_image = path3.render(date, True, WHITE, BLACK)
    date_imageRect = date_image.get_rect()
    date_imageRect.midtop = textRectObj.midbottom
    screen.blit(date_image, date_imageRect)


def saying():  # 格言
    path4 = pygame.font.Font(patch, 30)
    saying = API.saying.saying_ran()
    saying_image = path4.render(saying, True, WHITE, BLACK)
    saying_imageRect = saying_image.get_rect()
    saying_imageRect.midbottom = (384, 1072)  # 文本位置
    screen.blit(saying_image, saying_imageRect)


try:
    API.network_test.test()
    imageNow()
    temperatreNow()
    temperatreNow()
    textNow()
    saying()
    suggestion()
    daily()
    lunar()
    print("信息已更新")
except:
    disconnect()
    print("网络异常")


# except:
#     disconnect()
#     print("网络异常1")


def showTime(fontObj, text, x, y):  # 显示时间
    global textRectObj
    textSurfaceObj = fontObj.render(text, True, WHITE, BLACK)  # 配置要显示的文字
    textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
    textRectObj.center = (x, y)  # 设置显示对象的坐标
    screen.blit(textSurfaceObj, textRectObj)  # 绘制字体


fontbigObj = pygame.font.Font(patch, 48)  # 时间字体文件路径

while True:  # 程序主循环
             
    fps = pygame.time.Clock()
    fps.tick(60)  # 控制刷新频率（帧率）

    now = time.ctime()[11:20]  # 获得系统当前时间
    clock = now  # 格式化形式
    showTime(fontbigObj, clock, 400, 1130)
    date()

    for event in pygame.event.get():  # 获取事件

        if event.type == pygame.KEYDOWN :  # 判断事件是否为退出事件
            if event.key == pygame.K_DELETE:

                pygame.quit()  # 退出pygame

                exit()  # 退出系统
   

   
        if event.type == COUNT:  # 计时刷新

            try:
                screen.fill(BLACK)  # 填冲背景以覆盖旧元素
                API.network_test.test()
                daily()
                textNow()
                date()
                suggestion()
                imageNow()
                temperatreNow()
                lunar()
                saying()
                print("信息已更新")
               
            
            except:
            
                now = time.ctime()[11:20]  # 获得系统当前时间
                clock = now  # 格式化形式
                showTime(fontbigObj, clock, 400, 1130)
                date()
                disconnect()
                print("网络异常")

    pygame.display.update()  # 绘制屏幕内容
