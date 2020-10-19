from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from car.shopping_car import Car
from user.models import TUser, TCart, TAddress, TOrder, TBook
from datetime import datetime


def car(request):
    car = request.session.get('car')
    user = request.COOKIES.get('username')
    if user:
        user_id = TUser.objects.get(username=user).id
        if car:
            for book in car.book_list:
                TCart.objects.create(user_id=user_id, count=book.count, book_id=book.book_id)
            del request.session['car']
        car = TCart.objects.filter(user_id=user_id)  # 查出当前登陆者的所有图书的属性(id和count 在TCart表中)
        book = Car()
        for i in car:
            book.add_book(id=i.book_id, count=i.count)
        return render(request, 'car.html', {'car': book.book_list, 'user': user})
    car1 = request.session.get('car')
    if car1:  # 如果存在session则返回car.book_list,不存在返回"",前端提示"购物车为空,逛逛"
        return render(request, 'car.html', {'car': car.book_list, 'user': user})
    else:
        return render(request, 'car.html', {'car': ""})


def add_car(request):  # 书籍详情页面,加入购物车
    book_id = request.GET.get('id')
    count = request.GET.get('count')
    username = request.COOKIES.get('username')
    if username:
        user_id = TUser.objects.get(username=username).id
        res = TCart.objects.filter(book_id=int(book_id), user_id=int(user_id))
        if res:
            res[0].count = res[0].count + int(count)
            res[0].save()
        else:
            TCart.objects.create(user_id=user_id, count=int(count), book_id=book_id)

    else:
        car = request.session.get('car')
        if not car:
            car = Car()
        car.add_book(id=book_id, count=int(count))
        request.session['car'] = car
    return JsonResponse({'ok': "添加购物车成功"})


def add(request):  # 购物车页面,"+"按钮
    id = request.GET.get('id')
    count = request.GET.get('count')
    username = request.COOKIES.get('username')
    if username:
        user_id = TUser.objects.get(username=username).id
        res = TCart.objects.filter(book_id=int(id), user_id=int(user_id))
        if res:
            res[0].count = res[0].count + int(count)
            res[0].save()
        else:
            TCart.objects.create(user_id=user_id, count=int(count), book_id=id)

    else:
        car = request.session.get('car')
        car.add_book(id=id, count=int(count))
        request.session['car'] = car
    return JsonResponse({'ok': "1"})


def modify_book(request):  # 购物车页面,"-"按钮和文本框
    id = request.GET.get('id')
    count = request.GET.get('count')
    username = request.COOKIES.get('username')
    if username:
        user_id = TUser.objects.get(username=username).id
        res = TCart.objects.filter(book_id=int(id), user_id=int(user_id))
        if res:
            res[0].count = int(count)
            res[0].save()
        else:
            TCart.objects.create(user_id=user_id, count=int(count), book_id=id)

    else:
        car = request.session.get('car')
        car.modify_book(id=id, count=int(count))
        request.session['car'] = car
    return JsonResponse({'ok': "1"})


def del_car(request):       # 删除购物车项
    id = request.GET.get('id')
    username = request.COOKIES.get('username')
    if username:
        user_id = TUser.objects.get(username=username).id
        res = TCart.objects.filter(book_id=int(id), user_id=int(user_id))
        if res:
            res.delete()
    else:
        car = request.session.get('car')
        car.del_book(id)
        request.session['car'] = car
    return JsonResponse({'ok': "1"})


def order(request):         # 耦合性过高
    user = request.COOKIES.get('username')
    book_id = request.session.get("book_id")
    count = request.session.get("count")
    if request.method == "GET":
        if book_id and count:
            user_id = TUser.objects.get(username=user).id
            user_address = TAddress.objects.filter(user_id=user_id)
            book = Car()
            book.add_book(id=book_id, count=count)
            return render(request, 'indent.html',
                          {"user": user, "user_address": user_address, "book": book.book_list,
                           "sum": book.book_list[0].money})
        else:
            if user:
                user_id = TUser.objects.get(username=user).id
                car1 = TCart.objects.filter(user_id=user_id)  # 查出当前登陆者的所有图书的属性(id和count 在TCart表中)
                book = Car()
                sum = 0
                for i in car1:
                    book.add_book(id=i.book_id, count=i.count)
                for j in book.book_list:
                    sum += j.money
                user_address = TAddress.objects.filter(user_id=user_id)
                return render(request, 'indent.html',
                              {"user": user, "user_address": user_address, "book": book.book_list, "sum": sum})
            else:
                return redirect("user:login")

    else:
        addr_user = request.POST.get("user1")
        # print(addr_user)
        address = request.POST.get("address")
        # print(address)
        postcode = request.POST.get("postcode")
        phone1 = request.POST.get("phone1")
        phone2 = request.POST.get("phone2")
        user_id = TUser.objects.get(username=user).id
        book_count = TCart.objects.filter(user_id=int(user_id))
        book_id = request.session.get("book_id")
        if book_id or book_count:       # 如果购物车存在数据或单独购买,则会产生订单项
            if address:
                res = TAddress.objects.filter(address=address)
                if res:
                    ok = request.session.get("ok")
                    if ok:
                        request.session["ok"] = False
                        user_id = TUser.objects.get(username=user).id
                        address_id = TAddress.objects.get(address=address).id
                        base_code = datetime.now().strftime('%Y%m%d%H%M%S')
                        user_id_str = str(user_id).zfill(8)
                        order_id = base_code + user_id_str
                        create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        # print("order_id=", order_id)
                        # print("create_time=", create_time)
                        if book_id and count:
                            book_price = TBook.objects.filter(book_id=book_id)[0].dang_price
                            sum = round(book_price * int(count), 2)
                            TOrder.objects.create(order_id=order_id, order_name=addr_user, create_time=create_time,
                                                  price=float(sum), address_id=address_id, user_id=user_id)
                            book_book = TBook.objects.filter(book_id=book_id)[0]
                            print(book_book)
                            book_book.sales += count
                            book_book.save()
                            id = TOrder.objects.get(order_id=order_id).id
                            request.session["id"] = id
                            request.session["book_id"] = False
                            request.session["count"] = False
                        else:
                            car1 = TCart.objects.filter(user_id=user_id)  # 查出当前登陆者的所有图书的属性(id和count 在TCart表中)
                            book = Car()
                            sum = 0
                            for i in car1:
                                book.add_book(id=i.book_id, count=i.count)
                            for j in book.book_list:
                                sum += j.money
                            # print(sum)
                            TOrder.objects.create(order_id=order_id, order_name=addr_user, create_time=create_time,
                                                  price=float(sum), address_id=address_id, user_id=user_id)
                            for n in car1:
                                book = TBook.objects.get(book_id=n.book_id)
                                book.sales += n.count
                                book.save()
                            id = TOrder.objects.get(order_id=order_id).id
                            request.session["id"] = id
                            res = TCart.objects.filter(user_id=user_id)
                            if res:
                                res.delete()  # 清空购物车
                        return JsonResponse({"ok": "1"})
                    else:
                        return JsonResponse({"error": "1", "msg": "地址已存在"})
                else:
                    if addr_user:
                        if postcode:
                            TAddress.objects.create(name=addr_user, address=address, postcode=postcode, phone=phone1,
                                                    telephone=phone2, user_id=user_id)
                            user_id = TUser.objects.get(username=user).id
                            address_id = TAddress.objects.get(address=address).id
                            base_code = datetime.now().strftime('%Y%m%d%H%M%S')
                            user_id_str = str(user_id).zfill(8)
                            order_id = base_code + user_id_str
                            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            if book_id and count:
                                book_price = TBook.objects.filter(book_id=book_id)[0].dang_price
                                sum = round(book_price * int(count), 2)
                                print(11111)
                                TOrder.objects.create(order_id=order_id, order_name=addr_user, create_time=create_time,
                                                      price=float(sum), address_id=address_id, user_id=user_id)
                                book_book = TBook.objects.filter(book_id=book_id)[0]
                                print(book_book)
                                book_book.sales += count
                                book_book.save()
                                id = TOrder.objects.get(order_id=order_id).id
                                request.session["id"] = id
                                request.session["book_id"] = False
                                request.session["count"] = False
                            else:
                                car1 = TCart.objects.filter(user_id=user_id)  # 查出当前登陆者的所有图书的属性(id和count 在TCart表中)
                                book = Car()
                                sum = 0
                                for i in car1:
                                    book.add_book(id=i.book_id, count=i.count)
                                for j in book.book_list:
                                    sum += j.money
                                TOrder.objects.create(order_id=order_id, order_name=addr_user, create_time=create_time,
                                                      price=float(sum), address_id=address_id, user_id=user_id)
                                for n in car1:
                                    book = TBook.objects.get(book_id=n.book_id)
                                    book.sales += n.count
                                    book.save()
                                id = TOrder.objects.get(order_id=order_id).id
                                request.session["id"] = id
                                res = TCart.objects.filter(user_id=user_id)
                                if res:
                                    res.delete()
                            return JsonResponse({"ok": "1"})
                        else:
                            return JsonResponse({"error": "4", "msg": "未填写邮箱"})
                    else:
                        return JsonResponse({"error": "3", "msg": "未填写姓名"})  # 没有姓名
            else:
                return JsonResponse({"error": "2", "msg": "未填写地址"})  # 没有地址
        else:
            return JsonResponse({"error": "5", "msg": "订单项为空!"})


def address_1(request):
    id = request.GET.get("address_id")
    res = TAddress.objects.get(id=id)
    request.session["ok"] = True

    def my_json(th):
        if isinstance(th, TAddress):
            return {"id": res.id, "name": res.name, "address": res.address, 'phone': res.phone,
                    'telephone': res.telephone, 'postcode': res.postcode, "user_id": res.user_id}

    return JsonResponse({"res": res}, json_dumps_params={"default": my_json})


def order_ok(request):
    order_id = request.session.get("id")
    user = request.COOKIES.get('username')
    if order_id:
        order = TOrder.objects.get(id=order_id)
        request.session["id"] = False
        return render(request, 'indent ok.html', {"order": order, "user": user})
    else:
        return redirect('index:index')


def buy(request):
    user = request.COOKIES.get('username')
    if user:
        book_id = request.GET.get("id")
        request.session["book_id"] = book_id
        count = request.GET.get("count")
        if count:
            request.session["count"] = int(count)
        else:
            request.session["count"] = 1
        return JsonResponse({"ok": "1"})
    else:
        book_id = request.GET.get("id")
        request.session["book_id"] = book_id
        count = request.GET.get("count")
        if count:
            request.session["count"] = int(count)
        else:
            request.session["count"] = 1
        car = request.session.get('car')
        if not car:
            car = Car()
        car.add_book(id=book_id, count=int(count))
        request.session['car'] = car
        return JsonResponse({"error": "1"})
