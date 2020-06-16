#导入pygame
import random
import time
import pygame

class GameSprite(pygame.sprite.Sprite):#超级父类是Sprite的子类
    '''定义一个超级父类'''
    def __init__(self,image,speed):
        #调用父类的初始化方法
        pygame.sprite.Sprite.__init__(self)#将自身传递给父类
        #属性1:加载图片
        self.image = pygame.image.load(image)   #需要传参image
        #属性2:获取精灵的坐标
        self.rect = self.image.get_rect()   #不需要参数
        #属性3:运动的速度
        self.speed =speed   #需要参数speed
        # 定义子弹的组（弹夹）
        self.bullets = pygame.sprite.Group()  # 不需要传参
    def event(self):#方法1
        events = pygame.event.get()  # 监听输入设备在画面的操作
        if len(events):  # 长度不为空，即表示有操作
            for event in events:
                # 判断鼠标摁右上角退出
                if event.type == pygame.QUIT:
                    pygame.quit()  # 退出程序，会继续执行语句（报错找不到文件）
                    exit()  # 结束程序，不再执行下面的语句
                if event.type ==SMALL_EVENT:
                    emeny0 =EmenySprite(emeny0_image,emeny0_speed )
                    emenys_group.add(emeny0)
                   # print(emenys_group.sprites())
                if  event.type ==MIDLLE_EVENT:
                    emeny =Emeny1Sprite(emeny1_image,emeny1_speed)
                    emenys_group.add(emeny)
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_SPACE:
                        x = hero2.rect.x + hero2.rect.width // 2 - 5
                        y = hero2.rect.y - 20
                        bullet = BulletSprite(bullet_image, bullet_speed, x, y)
                        hero2.bullets.add(bullet)
    def move(self):#方法2
        pass
    def update(self):#方法3
        self.move()
        self.event()
class BackGroundSprite(GameSprite):
    '''背景类'''
    def move(self):
        self.rect.y +=self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y  = -SCREEN_HEIGHT

class HeroSprite(GameSprite):
    '''英雄飞机类'''
    def __init__(self,image,speed):
        super().__init__(image=image,speed=speed)
        #获取飞机的位置，初始化操作
        self.rect.x =(SCREEN_WIDTH - self.rect.width)//2
        self.rect.y =SCREEN_HEIGHT - self.rect.height
        self.heroHP =10

    def move(self):
        keys =pygame.key.get_pressed()#连续键盘
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.rect.y  <= 0:
                self.rect.y  = 0
        if keys[pygame.K_DOWN]:
            self.rect.y  += self.speed
            if self.rect.y  >= SCREEN_HEIGHT - self.rect.height:
                self.rect.y  = SCREEN_HEIGHT - self.rect.height
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x  <= 0:
                self.rect.x = 0
        if keys[pygame.K_RIGHT]:
            self.rect.x  += self.speed
            if self.rect.x  >= SCREEN_WIDTH- self.rect.width:
                self.rect.x  = SCREEN_WIDTH -self.rect.width
        # if keys[pygame.K_SPACE]:
        #     x =self.rect.x+self.rect.width//2-5
        #     y =self.rect.y-20
        #     bullet =BulletSprite(bullet_image,bullet_speed,x,y)
        #     self.bullets.add(bullet)
    def event(self):
        heroHert = pygame.sprite.spritecollide(hero2, emenys_group, False)  # 返回列表  如果发生碰撞，列表中有返回值
        if len(heroHert):  # 列表不为空，说明发生了碰撞
            self.heroHP -= 1
        if 7>=self.heroHP >4:
            image = './feiji/hero_blowup_n1.png'
            self.image = pygame.image.load(image)
        elif 4>=self.heroHP >2:
            image = './feiji/hero_blowup_n2.png'
            self.image = pygame.image.load(image)
        elif 2>=self.heroHP >0:
            image = './feiji/hero_blowup_n3.png'
            self.image = pygame.image.load(image)
        elif self.heroHP == 0:
            image = './feiji/hero_blowup_n4.png'
            self.image = pygame.image.load(image)
            self.heroHP-=1
        elif self.heroHP < 0:

            pygame.quit()
            exit()

class BulletSprite(GameSprite):
    '''子弹类'''
    def __init__(self,image,speed,x,y):
        super().__init__(image=image,speed=speed)
        self.rect.x =x
        self.rect.y =y

    def move(self):
        self.rect.y -=self.speed
        if self.rect.y<=-SCREEN_HEIGHT:
            self.kill()

class EmenyBulletSprite(GameSprite):
    '''敌方子弹类'''
    def __init__(self,image,speed,x,y):
        super().__init__(image=image,speed=speed)
        self.rect.x =x
        self.rect.y =y

    def move(self):
        self.rect.y +=self.speed
        if self.rect.y>=SCREEN_HEIGHT:
            self.kill()

class EmenySprite(GameSprite):
    '''敌方飞机类0'''
    def __init__(self,image ,speed):
        super().__init__(image=image,speed=speed)
        self.rect.x =random.randint(0,SCREEN_WIDTH-self.rect.width)#随机x坐标出现
        self.rect.y =-self.rect.height
        self.__emeny0HP =4
    def move(self):
        #self.__emenyHert = pygame.sprite.groupcollide(hero2.bullets, emenys_group, True, False)  组与组之间
        self.__emenyHert = pygame.sprite.spritecollide(self, hero2.bullets, True)  # True 碰撞之后消失(kill)
        if len(self.__emenyHert):
            self.__emeny0HP -= 1
        if(self.__emeny0HP>0):
            self.rect.y +=self.speed

        if self.rect.y >=SCREEN_HEIGHT+self.rect.y:
            self.kill()
    def event(self):
        emenyHert = pygame.sprite.collide_mask(hero2,self)  # 返回列表  如果发生碰撞，列表中有返回值
        if emenyHert:  # 列表不为空，说明发生了碰撞
            self.__emeny0HP == 1
        if self.__emeny0HP == 3:
            image = './feiji/enemy0_down1.png'
            self.image = pygame.image.load(image)
            #print('中弹一次')
        elif self.__emeny0HP == 2:
            image = './feiji/enemy0_down2.png'
            self.image = pygame.image.load(image)
            #print('中弹2次')
        elif self.__emeny0HP == 1:
            image = './feiji/enemy0_down3.png'
            self.image = pygame.image.load(image)
            #print('中弹3次')
        elif self.__emeny0HP == 0:
            image = './feiji/enemy0_down4.png'
            self.image = pygame.image.load(image)
            self.__emeny0HP -= 1
        if self.__emeny0HP < 0:
            self.kill()#如何使类的对象延迟1秒而不影响整个进程

       # screen.blit(self.image, (self.rect.x, self.rect.y))
class Emeny1Sprite(GameSprite):
    '''敌方飞机类1'''
    def __init__(self, image, speed):
        super().__init__(image=image, speed=speed)
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)  # 随机x坐标出现
        self.rect.y = -self.rect.height
        self.__emeny1HP = 8
        self.i =TIME_SLEEP-20#第一颗子弹20帧后发射


    def move(self):
        # self.__emenyHert = pygame.sprite.groupcollide(hero2.bullets, emenys_group, True, False)  组与组之间
        self.__emenyHert = pygame.sprite.spritecollide(self, hero2.bullets, True)  # True 碰撞之后消失(kill)
        if len(self.__emenyHert):
            self.__emeny1HP -= 1
        if (self.__emeny1HP > 0):
            self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT + self.rect.y:
            self.kill()
    def event(self):
        '''中弹'''
        if 6>=self.__emeny1HP > 4:
            image = './feiji/enemy1_down1.png'
            self.image = pygame.image.load(image)
            #print('中弹一次')
        elif 4>=self.__emeny1HP >2:
            image = './feiji/enemy1_down2.png'
            self.image = pygame.image.load(image)
            #print('中弹2次')
        elif 4>=self.__emeny1HP >0:
            image = './feiji/enemy1_down3.png'
            self.image = pygame.image.load(image)
            #print('中弹3次')
        elif self.__emeny1HP == 0:
            image = './feiji/enemy1_down4.png'
            self.image = pygame.image.load(image)
            self.__emeny1HP -= 1
        elif self.__emeny1HP < 0:
            self.kill()
        '''发射子弹'''

        if self.i%TIME_SLEEP==0:
            xx = self.rect.x + self.rect.width // 2 - 5
            yy = self.rect.y + 89
            bullet2 = EmenyBulletSprite('./feiji/bullet2.png', self.speed + 1, xx, yy)
            emenys_group.add(bullet2)
            self.i=TIME_SLEEP
            #print(self.i)
        self.i+=1
       # print(self.i)






#初始化pygame
pygame.init()
#给一张背景图，设置背景移动速度
bg_image = './feiji/background.png'
bg_speed =5
#创建背景对象
bg= BackGroundSprite(image=bg_image,speed=bg_speed)
bg2=BackGroundSprite(image=bg_image,speed=bg_speed)
SCREEN_WIDTH =bg.rect.width  #全局变量
SCREEN_HEIGHT =bg.rect.height #全局变量
bg2.rect.y =-SCREEN_HEIGHT#设置第二张背景图起始位置
TIME_SLEEP =150 #子弹间隔帧数
#为了产生更多的飞机，我们可以使用pycharm里面的一个属性pygame.EVENT,其实这个就是一个常量
#创建一个产生小飞机的  自定义事件(使得event.tpye出现我们需要的值)
SMALL_EVENT=pygame.USEREVENT
#创建一个产生中等飞机的自定义事件
MIDLLE_EVENT=pygame.USEREVENT+1

EmenyBullet =pygame.USEREVENT+2
# 为了让自定义事件发生的频率不一样，pycharm中的time类提供了一个set_timer()这个方法进行设置
pygame.time.set_timer(SMALL_EVENT,1000)#让小事件1秒发生一次
pygame.time.set_timer(MIDLLE_EVENT,3000)#让中等事件3秒发生一次
pygame.time.set_timer(EmenyBullet,3000)
#给一张物体图（飞机）
hero2_image='./feiji/hero2.png'
hero2_speed=20
#创建飞机对象
hero2 =HeroSprite(image=hero2_image,speed=hero2_speed)

#给一个物体图（子弹）
bullet_image ='./feiji/bullet.png'
bullet_speed =5
#bullet =BulletSprite(bullet_image,bullet_speed)
#敌方子弹
bullet2_image ='./feiji/bullet2.png'
bullet2_speed =5


#创建敌方飞机0对象
emeny0_speed =5
emeny0_image = './feiji/enemy0.png'
emeny0 =EmenySprite(image=emeny0_image,speed=emeny0_speed)

#创建敌方飞机1对象
emeny1_speed =2
emeny1_image = './feiji/enemy1.png'
emeny1 =Emeny1Sprite(image=emeny1_image,speed=emeny1_speed)


#创建窗口 第一个参数的形式是一个元组
screen =pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#screen2 =pygame.display.set_mode((222,111))

#定义一个敌方飞机的精灵组
emenys_group =pygame.sprite.Group(emeny0,emeny1)
#pygame.sprite里面提供了一个方法，Group()这个方法进行画图
#定义一个组
bg_group =pygame.sprite.Group(bg,bg2,hero2)#把类的对象放进去，打包成组
#定义一个时钟控制代码的刷新频率
clock =pygame.time.Clock()




while True:#实时
#   控制代码刷新的频率  运行快的电脑，执行到speed语句速度非常快，有的电脑反之。此法可以稍微统一速度
    clock.tick(20)
#   实时画图 第一种画法
    #screen.blit(bg.image,(0,0))
#   第二种画法
    bg_group.draw(screen)#调用组的方法在窗口screen画图

#   画子弹
    hero2.bullets.draw(screen)
    hero2.bullets.update()

#   画敌方飞机
    emenys_group.draw(screen)
#     emeny0.move()
#     emeny0.event()
    emenys_group.update()
#   调用类的方法
#     bg.move()
#     bg2.move()
#     bg.event()
#     hero2.move()
#     hero2.event()
    bg_group.update()#以上浓缩成一句

    #判断敌方飞机与子弹进行碰撞
    #为了让程序猿更舒服的开发游戏，pygame中的sprite提供了方法可以判断精灵组之间的距离
    #判断子弹和敌方飞机是否碰撞（组与组之间）



    #判断精灵与精灵组之间是否碰撞

#   实时刷新窗口
    pygame.display.update()
   # print('====')








