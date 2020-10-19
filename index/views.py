from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
from user.models import TBook, TCategory


def index(request):
    cates1 = TCategory.objects.filter(level=1)
    cates2 = TCategory.objects.filter(level=2)
    book = TBook.objects.all().order_by("date")[0:8]
    time = (datetime.now() - timedelta(days=20)).strftime("%Y-%m-%d")
    book1 = TBook.objects.filter(date__gte=time).order_by("-sales")[0:9]
    book2 = TBook.objects.all().order_by("price")[0:8]
    user = request.COOKIES.get('username')
    return render(request, 'index.html',
                  {'cates1': cates1, 'cates2': cates2, 'book': book, "book1": book1, 'book2': book2, 'user': user})


def booklist(request):
    cates1 = TCategory.objects.filter(level=1)
    cates2 = TCategory.objects.filter(level=2)
    cate_id = request.GET.get('id')
    level = request.GET.get('level')
    title = TCategory.objects.filter(id=cate_id)[0]
    user = request.COOKIES.get('username')
    if title.parentid:
        title1 = title.title
        title = TCategory.objects.filter(id=title.parentid)[0]
    else:
        title1 = ''
    num = request.GET.get('num', 1)
    if level == '1':
        cates3 = TBook.objects.filter(category__parentid=cate_id)
    elif level == '2':
        cates3 = TBook.objects.filter(category_id=cate_id)

    paginator = Paginator(cates3, per_page=4)
    page = paginator.page(num)
    return render(request, 'booklist.html',
                  {'cates1': cates1, 'cates2': cates2, 'cates3': cates3, 'cate_id': cate_id, 'level': level,
                   'page': page, 'title': title, 'title1': title1, 'user': user})


def book_details(request):
    id = int(request.GET.get('id'))
    book = TBook.objects.get(book_id=id)
    user = request.COOKIES.get('username')
    title = TCategory.objects.filter(id=book.category_id)[0]
    title1 = TCategory.objects.filter(id=title.parentid)[0]
    return render(request, 'Book_details.html', {'book': book, 'title': title, 'title1': title1, 'user': user})
