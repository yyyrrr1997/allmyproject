from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)  # 名称
    gpic = models.CharField(max_length=100) # 图片地址
    gprice = models.DecimalField(max_digits=5, decimal_places=2) # 价格 格式：xx.xx
    gunit = models.CharField(max_length=20) # 单价
    gclick = models.IntegerField() # 点击数量
    gbrief = models.CharField(max_length=200) # 简介
    gstock = models.IntegerField() # 库存
    gcontent = HTMLField() # 商品详情 富文本编辑器
    isDelete = models.BooleanField(default=False)
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.gtitle