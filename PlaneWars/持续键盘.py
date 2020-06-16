import pygame
#初始化
pygame.init()
print('初始化成功')

# 加载背景图片
bg =pygame.image.load('./feiji/bg.png') #有返回值可以返回
bg2 =pygame.image.load('./feiji/bg.png') #设置两张背景图片循环播放产生自然的飞机移动效果
bg_height =bg.get_rect().height
bg_width =bg.get_rect().width

#创建一个窗口 第一个参数的形式是一个元组
screen=pygame.display.set_mode((bg_width,bg_height)) #有返回值可以返回
# #获取图片的位置和大小
# rect =bg.get_rect()
# print('rect:',rect)
# # 获取图片具体的值
# print(rect.top)
# print(rect.right)


#加载飞机的图片
hero2 =pygame.image.load('./feiji/hero2.png')
hero2_height =hero2.get_rect().height
hero2_width =hero2.get_rect().width
#初始化飞机位置
hero2_x =200
hero2_y =500

bg_y =0
bg2_y =-bg_height

clock =pygame.time.Clock() #通常使用time ；pygame使用time.Clock()
#让程序一直运行
while True:
    # 创建一个一个可以一直摁下键盘的事件
    keys = pygame.key.get_pressed()
    #print(keys)
    if keys[pygame.K_UP]:
        hero2_y-=5
        if hero2_y <= 0:
            hero2_y = 0
    if keys[pygame.K_DOWN]:
        hero2_y+=5
        if hero2_y >= bg_height - hero2_height:
            hero2_y = bg_height - hero2_height
    if keys[pygame.K_LEFT]:
        hero2_x-=5
        if hero2_x <= 0:
            hero2_x = 0
    if keys[pygame.K_RIGHT]:
        hero2_x+=5
        if hero2_x >= bg_width - hero2_width:
            hero2_x = bg_width - hero2_width
    #创建一个监听事件
    events =pygame.event.get() #监听输入设备在画面的操作
    #print(events)
    if len(events): #长度不为空，即表示有操作
        for event in events:
            #判断鼠标摁右上角退出
            if event.type ==pygame.QUIT:
                pygame.quit() #退出程序，会继续执行语句（报错找不到文件）
                exit() #结束程序，不再执行下面的语句



    # 实时在屏幕上面画图片
    screen.blit(bg, (0, bg_y))  # (x,y)正向：向右偏移，向下偏移
    screen.blit(bg2, (0, bg2_y))
    bg_y +=1    #bg y轴向下变换
    bg2_y+=1
    #两张背景循环
    if bg_y>bg_height:
        bg_y =-bg_height
    if bg2_y > bg_height:
        bg_y = -bg_height
    # 实时画飞机
    screen.blit(hero2, (hero2_x, hero2_y))

    # 对窗口进行实时更新
    pygame.display.update()
#关闭python
pygame.quit()