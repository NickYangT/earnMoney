# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from polls.models import ShareModel, ShareDailyDetailModel, UsersModel
# Register your models here.



@admin.register(UsersModel)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('alisa',  'name', 'sex', 'age','email', 'image', 'address', 'profession', 'colored_status', 'province', 'blog', )
    search_fields = ('name',)
    ordering = ('id',)
    list_filter =('province', 'profession')
    date_hierarchy ='birthday'

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