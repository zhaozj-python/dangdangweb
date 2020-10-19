from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        print("中间件已经初始化完毕")

    def process_request(self, request):
        if "order" in request.path:  # 路径中如果有"order"
            print("登录验证")
            session = request.session  # 获取session
            if session.get("is_login"):  # 判断是否有登录的标记
                print("已登录")
            else:
                print("未登录")
                return render(request, "login.html")  # 未登录则，跳转登录页面
        else:
            print("正在登录")

    def process_response(self, request, response):
        print("response:", request, response)
        return response

    def process_exception(self, request, ex):
        print("exception:", request, ex)
