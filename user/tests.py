import os, django
from random import choice

from django.test import TestCase
from django.db import transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dangdang.settings")
django.setup()
from user.models import TBook

# Create your tests here.


book_name = ['高等数学', '概率论与数理统计', '星火英语', '肖四肖八', '恋恋有词','儿童绘本','童话']
intro = ['高等数学习题解全解指南（上册）(同济 第七版)》是由高等教育出版社出版，同济大学数学系编写的《高等数学（第七版）》(上册)的配套学习辅导书，是教育部考试中心研究生入学考试指定参考教材标准辅导用书。 《高等数学','本书是浙大版《概率论与数理统计》（第四版）的配套辅导书，按照主教材的要求和章节顺序进行编排，与主教材习题一致。本书对教材的全部300多道题目都给出了解答，少数题目是一题多解，有些作了题目分析、解题思路分析和']
comment = ['123','213','2342','12312','5456','6789','9867']
author = ['李四','王五','赵柳','田七']
publish = ['上海交大出版社','中国人民出版社','童话出版社','绘本出版社','考研出版社']
inventory = ['本地仓','京东仓','当当仓']
category_id = [6,7,8,9,10,19,21,18]
paper = ['轻型纸','胶版纸','印刷纸']
recommend = '不会争抢，只能努力；不愿辜负，只有前行；生性内向，却活在光下；逆流而上，也有别样人生——维吾尔语境下长大，却有令人惊叹的汉语写作功底。20余万字细数成长点滴，一气读完，书中画面犹在眼前。'
author_intro = '假设的名字，常与张三、王五一起指代不特定的某个人，揶揄或者概括常用；李实为中国之大姓，由古至今均如此，百家姓中李在当时排名第四，俗称李四。人们在日常交往中总要说事儿，说事儿就难免不了举例。依常规这例可都应是大家耳熟能详的，也因此就出现了张三、李四、王五、赵六之说。'
menu = '1,<br>2,<br>3,<br>4,<br>5,<br>6,<br>7,<br>8,<br>9'
comments = '这本书不错'
# for i in range(8):
#     TBook.objects.create(book_name=choice(book_name),book_cover=f'img/{i}.png',intro=choice(intro),comment=choice(comment), author=choice(author),publish=choice(publish),store=choice(inventory),category_id= choice(category_id),paper=choice(paper),recommend=recommend,author_intro=author_intro,menu=menu,comments=comments)
