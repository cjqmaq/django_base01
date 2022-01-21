from django.shortcuts import render

# Create your views here.
'''
视图:
所谓的视图，其实就是Python函数
视图函数有2个要求：
       1. 视图函数的第一个参数就是接受请求.这个请求其实就是HttpRequest的类对象
       2.必须返回一个响应
       
'''
# request
from django.http import HttpRequest
from django.http import HttpResponse
def index(request):

    # return HttpResponse("ok")
    # render   渲染模板
    # request,  请求
    # template_name,  模板名字
    # context=None,

   #  模拟数据查询
    context={
        'name':'马上双11，点击有惊喜'
    }
    return render(request,'book/index.html',context=context)
