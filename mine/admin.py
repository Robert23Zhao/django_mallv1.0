from django.contrib import admin

from mine.models import Order, Cart, Comments


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ 订单后台管理 """
    list_display = ('sn', 'user', 'to_user', 'to_area', 'to_phone')
    # 按照用户名、昵称来搜索
    search_fields = ('user__username', 'user__nickname', 'to_user')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """ 购物车管理 """
    list_display = ('name', 'user', 'price', 'img')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """ 商品评论 """
    list_display = ('user', 'product', 'score', 'desc')



