import pygame
#初始化
pygame.init()
print('初始化成功')
#创建一个窗口 第一个参数的形式是一个元组
screen=pygame.display.set_mode((480,852)) #有返回值可以返回
# 加载背景图片
bg =pygame.image.load('./feiji/background.png') #有返回值可以返回
bg2 =pygame.image.load('./feiji/background.png') #设置两张背景图片循环播放产生自然的飞机移动效果
# 在屏幕上面画图片
#screen.blit(bg,(0,0))#(x,y)正向：向右偏移，向下偏移

# #获取图片的位置和大小
# rect =bg.get_rect()
# print('rect:',rect)
# # 获取图片具体的值
# print(rect.top)
# print(rect.right)

#加载飞机的图片
hero2 =pygame.image.load('./feiji/hero2.png')



# bg_y =0
# bg2_y =-852
hero2_y =852

#让程序一直运行
while True:
    # 实时在屏幕上面画图片
    #screen.blit(bg, (0, bg_y))  # (x,y)正向：向右偏移，向下偏移
    #screen.blit(bg2, (0, bg2_y))
    screen.blit(bg, (0, 0))
    # bg_y +=1    #bg y轴向下变换
    # bg2_y+=1
    hero2_y-=1
    #两张背景循环
    # if bg_y>852:
    #     bg_y =-852
    # if bg2_y > 852:
    #     bg_y = -852
    if hero2_y<-112:
        hero2_y=852
    # 实时画飞机
    screen.blit(hero2, (200, hero2_y))
    # 对窗口进行实时更新
    pygame.display.update()
#关闭python
pygame.quit()