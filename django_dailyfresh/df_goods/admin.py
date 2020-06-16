from django.contrib import admin
from df_goods.models import *

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gclick', 'gbrief', 'gstock', 'gcontent', 'gtype']
# Register your models here.
admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)