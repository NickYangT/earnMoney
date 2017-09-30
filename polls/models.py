# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.html import format_html
from earnMoney.settings import STATIC_IMAGE

# Create your models here.


class UsersModel(models.Model):
    SEX = {('B', '男'), ('G', '女')}
    PROVINCE = {('000001', u'北京'),
                ('000002', u'上海'),
                ('000003', u'广东'),
                ('000004', u'重庆'),
                ('000005', u'天津'),
                ('000006', u'浙江'),
                ('000007', u'天津'),
                ('000008', u'湖南'),
                ('000009', u'湖北'),
                ('000010', u'福建'),
                ('000011', u'江西'),
                ('000012', u'四川'),
                ('000013', u'贵州'),
                }
    alisa = models.CharField(max_length=50, verbose_name=u'昵称')
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    sex = models.CharField(max_length=4, choices=SEX, default='B', verbose_name=u'性别')
    age = models.IntegerField(verbose_name=u'年龄')
    cellphones = models.CharField(max_length=11, verbose_name=u'手机')
    image = models.FileField(upload_to='../earnMoney/static', blank=True, default='../earnMoney/static/defualt.jpg', verbose_name=u'头像')
    address = models.CharField(max_length=100, verbose_name=u'家庭住址')
    birthday = models.DateField(verbose_name=u'出生日期')
    profession = models.CharField(max_length=30, verbose_name=u'职业')
    rvenue = models.IntegerField(verbose_name=u'年收入(万)')
    province = models.CharField(max_length=10, choices=PROVINCE, verbose_name=u'省份')
    blog = models.URLField(max_length=50, verbose_name=u'网址', null=True)
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')

    def colored_status(self):
        return format_html(
            '<span style="color: #FF0000;"><strong>{}</strong></span>',
            self.rvenue,
        )
    colored_status.short_description = u'年收入(万)'

    def goto_url(self):
        return format_html(
            '<a href="{0}" style="color:  #0000FF;"><strong>{0}</strong></a>'.format(self.blog)
        )
    goto_url.short_description = u'博客地址'


    def __unicode__(self):
        return self.alisa

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name


class Publisher(models.Model):
    Star = {('★', '一星'),
            ('★★', '二星'),
            ('★★★', '三星'),
            ('★★★★', '四星'),
            ('★★★★★', '五星')
    }
    name = models.CharField(max_length=100, verbose_name=u'出版社')
    rank = models.CharField(max_length=10, choices=Star, verbose_name=u'出版社等级')
    address = models.CharField(max_length=200, verbose_name=u'出版社地址')

    def get_rank(self):
        return format_html(
            '<span style="color: #FF0000;"><strong>{}</strong></span>',
            self.rank,
        )
    get_rank.short_description = u'出版社星级'

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'出版社'
        verbose_name_plural = verbose_name



class BookModel(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'书名')
    author = models.ForeignKey(UsersModel, verbose_name=u'作者')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u'价格')
    profile = models.CharField(max_length=200, null=False, verbose_name=u'简介')
    publisher = models.ForeignKey(Publisher, verbose_name=u'出版社')
    publisher_date = models.DateField(auto_now_add=True, verbose_name=u'出版日期')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'书'
        verbose_name_plural = verbose_name















class ShareModel(models.Model):
    Type = (('H', 'SH'), ('S', 'SZ'))
    name = models.CharField(max_length=10, verbose_name=u'名称')
    types = models.CharField(max_length=5, choices=Type, default='SH', verbose_name=u'类型')
    code = models.PositiveIntegerField(verbose_name=u'编号')

    def __unicode__(self):
        return '{0}{1}'.format(self.types, self.name)

    class Meta:
        verbose_name = u'股票'
        verbose_name_plural= verbose_name



class ShareDailyDetailModel(models.Model):
    name = models.ForeignKey(ShareModel, verbose_name=u'名称')
    SOQ = models.DecimalField(max_length=5, max_digits=5, decimal_places=2, null=True, verbose_name=u'开盘价')
    SCQ = models.DecimalField(max_length=5, max_digits=5, decimal_places=2, null=True, verbose_name=u'收盘价')


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'股票详细数据'
        verbose_name_plural = verbose_name

