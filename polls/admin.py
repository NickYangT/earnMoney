# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from polls.models import ShareModel, ShareDailyDetailModel, UsersModel,Publisher, BookModel
# Register your models here.



@admin.register(UsersModel)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('alisa',  'name', 'sex', 'age','email', 'image', 'address', 'profession', 'colored_status','province', 'goto_url', )
    search_fields = ('name',)
    ordering = ('id',)
    list_filter =('province', 'profession')
    #date_hierarchy ='birthday'

class MyAdminSite(admin.AdminSite):
    site_header = u'量化分析管理系统'  # 此处设置页面显示标题
    site_title = u'后台管理'  # 此处设置页面头部标题

admin_site = MyAdminSite(name='management')



@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'profile', 'publisher', 'publisher_date')
    search_fields = ('name', 'author')
    ordering = ('id',)
    list_filter = ('author', 'publisher')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_rank', 'address')
    search_fields = ('name', 'rank')
    ordering = ('rank',)
    list_filter = ('name',)







'''
@admin.register(ShareModel)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('name', 'types', 'code')
    search_fields = ('name', 'code')


@admin.register(ShareDailyDetailModel)
class ShareDailyDetailModel(admin.ModelAdmin):
    list_display = ('name', 'SOQ', 'SCQ')
    search_fields = ('name',)
'''