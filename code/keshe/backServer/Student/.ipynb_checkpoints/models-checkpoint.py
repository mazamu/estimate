from django.db import models

'''
学号 
姓名（如有隐私考虑代号）、
四级成绩、
六级成绩、
用户创建时间
测试时间、
测试结果。
'''


# Create your models here.
class UserProfile(models.Model):
    sid = models.CharField(max_length=11, verbose_name="学号")
    username = models.CharField(max_length=11, verbose_name='姓名')
    cet4 = models.IntegerField(verbose_name="四级成绩")
    cet6 = models.IntegerField(verbose_name="六级成绩")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="用户创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="测试时间")
    result = models.IntegerField(verbose_name="测试结果")
