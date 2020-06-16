from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uName = models.CharField(max_length=20)    #用户名
    uPWD = models.CharField(max_length=40)     #密码
    uEmail = models.CharField(max_length=30)   #电子邮箱
    uConsignee = models.CharField(max_length=30,default='')   #收件人
    uAddress = models.CharField(max_length=100,default='')    #地址
    uPostcodes = models.CharField(max_length=6,default='')    #邮政编码
    uPhone = models.CharField(max_length=11,default='')   #电话