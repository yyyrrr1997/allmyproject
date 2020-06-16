from django.db import models
from df_goods.models import *
from df_user.models import *
# Create your models here.
class OrderInfo(models.Model):
    user =models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    goods=models.ForeignKey(GoodsInfo,on_delete=models.CASCADE)
    count=models.IntegerField()
