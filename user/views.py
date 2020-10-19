import random
import string

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from captcha.image import ImageCaptcha
from user.models import TUser


def register(request):          # 从某个页面点击"立即注册",a标签携带对应url(id和level等)到达register函数,接收并返回前端
    if request.method == "GET":
        url = request.GET.get('url')
        if url == "booklist":
            id = request.GET.get('id')
            level = request.GET.get("level")
            return render(request, 'register.html', {'url': url, 'id': id, 'level': level})
        elif url == 'book_details':
            id = request.GET.get('id')
            return render(request, 'register.html', {'url': url, 'id': id})
        else:
            return render(request, 'register.html', {'url': url})
    else:
        name = request.POST.get('txt_username')
        pwd = request.POST.get('txt_password')
        repwd = request.POST.get('txt_repassword')
        captcha = request.POST.get('txt_vcode')
        code = request.session.get('code')
        agree = request.POST.get('chb_agreement')
        # if res:
        #     return JsonResponse({'error': "0", "msg": "用户名已存在"})
        # if pwd != repwd:
        #     return JsonResponse({'error': '1', 'msg': '密码错误'})
        # if name is None or pwd is None or repwd is None or captcha is None or agree is None:
        #     return JsonResponse({'error': '2', 'msg': '信息未填写完整'})
        if captcha.lower() == code.lower():
            if agree == 'on':
                with transaction.atomic():
                    TUser.objects.create(username=name, password=pwd)
                    res = JsonResponse({'msg': '成功'})
                    res.set_cookie('username', name, max_age=10000)
                    res.set_cookie('password', pwd, max_age=10000)
                    return res
            else:
                return JsonResponse({'error': '2', 'msg': '请同意服务条款'})
        else:
            return JsonResponse({'error': '3', 'msg': '验证码错误'})


def register_ok(request):       # 由注册页面前端的ajax跳转到,携带对应url,传给前端,前端跳转到对应页面
    username = request.GET.get('username')
    url = request.GET.get('url')
    if url == "booklist":
        id = request.GET.get('id')
        level = request.GET.get("level")
        return render(request, 'register ok.html', {'url': url, 'id': id, 'level': level, "username": username})
    elif url == 'book_details':
        id = request.GET.get('id')
        return render(request, 'register ok.html', {"username": username, 'url': url, 'id': id})
    else:
        return render(request, 'register ok.html', {"username": username, 'url': url})


def user_name(request):     # 判断数据库中是否已经存在此用户名
    username = request.POST.get('txt_username')
    msg = TUser.objects.filter(username=username)
    if msg:
        return JsonResponse({'error': '1', 'msg': '此手机号已注册，请更换其它手机号或邮箱'})
    else:
        return JsonResponse({'msg': '成功'})


def get_captcha(request):       # 生成验证码图片
    codelist = random.sample(string.ascii_letters + string.digits, 4)
    code = ''.join(codelist)
    img = ImageCaptcha()
    data = img.generate(code)
    request.session['code'] = code
    return HttpResponse(data, 'image/png')


def login(request):  # 登录view函数

    if request.method == 'GET':
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        res = TUser.objects.filter(username=username, password=password)
        if res:
            request.session['is_login'] = True  # 如果匹配,登录成功,置session为True,不设置会导致一直重定向
            return redirect('/index')
        url = request.GET.get('url')
        if url == "booklist":
            id = request.GET.get('id')
            level = request.GET.get("level")
            return render(request, 'login.html', {'url': url, 'id': id, 'level': level})
        elif url == 'book_details':
            id = request.GET.get('id')
            return render(request, 'login.html', {'url': url, 'id': id})
        elif url == "car":
            return render(request, 'login.html', {'url': url})
        else:
            return render(request, 'login.html', {'url': url})
    else:
        username = request.POST.get('txtUsername')
        password = request.POST.get('txtPassword')
        captcha = request.POST.get('txt_vcode')
        autologin = request.POST.get('autologin')
        code = request.session.get('code')
        print(code)
        res = TUser.objects.filter(username=username, password=password)
        if res:
            if captcha.lower() == code.lower():
                request.session['is_login'] = True
                res = JsonResponse({'ok': '1'})
                if autologin:
                    res.set_cookie('username', username, max_age=10000)
                    res.set_cookie('password', password, max_age=10000)
                    return res
                return res
            else:
                return JsonResponse({'error': '2', 'msg': '验证码错误'})
        else:
            return JsonResponse({"error": '1', 'msg': '用户名或密码错误'})


def exit(request):      # 退出登录状态,返回登录页面,清除对应cookie和session/
    request.session['is_login'] = False
    request.session.flush()
    res = redirect('user:login')
    res.set_cookie('username', 'None', max_age=0)
    return res
