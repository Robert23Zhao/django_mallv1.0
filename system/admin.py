from django.contrib import admin

from system.models import News, Slider, ImageFile
from utils.admin_actions import set_valid, set_invalid


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """ 新闻管理 """
    list_display = ('title', 'types', 'is_valid')
    actions = [set_valid, set_invalid]


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    """ 轮播图管理 """
    list_display = ('name', 'types', 'start_time', 'end_time', 'is_valid')
    actions = [set_valid, set_invalid]


@admin.register(ImageFile)
class ImageFileAdmin(admin.ModelAdmin):
    list_display = ('summary', 'img', 'content_object', 'is_valid')
