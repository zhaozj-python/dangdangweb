from user.models import TBook


class Book:
    def __init__(self, id, count):
        book = TBook.objects.get(book_id=id)
        self.book_id = id
        self.count = int(count)
        self.book_name = book.book_name
        self.dang_price = book.dang_price
        self.book_cover = book.book_cover
        self.price = book.price
        self.store = book.store
        self.discount = round(self.dang_price / self.price * 10, 2)
        self.money = round(self.dang_price * self.count, 2)


class Car:
    def __init__(self):
        self.book_list = []  # 设置空列表,用于存储选中的book对象

    def add_book(self, id, count=1):
        book = self.get_book(id)
        if book:
            book.count += count
        else:
            book = Book(id=id, count=count)
            self.book_list.append(book)

    def modify_book(self, id, count):
        for book in self.book_list:
            if book.book_id == id:
                book.count = count

    def del_book(self, id):
        book = self.get_book(id)
        self.book_list.remove(book)

    def get_book(self, id):  # 根据id判断book_list(购物车)中是否存在这本书,存在则只增加count
        for book in self.book_list:
            if book.book_id == id:
                return book
