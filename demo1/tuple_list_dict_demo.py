'''
1、在列表前加*号，会将列表拆分成一个一个的独立元素，不光是列表、元组、字典，由numpy生成的向量也可以拆分；
2、函数中*args和**kwargs的人应该知道，这两个形参都接收若干个参数，通常我们将其称为参数组
3、*args：接收若干个位置参数，转换成元组tuple形式
4、**kwargs：接收若干个关键字参数，转换成字典dict形式
5、ps:需要注意的是位置参数*args，一定要在关键字参数**kwargs前

6、zip是将一个或多个可迭代对象进行包装压缩，返回将结果是列表；
通俗的说：zip()压缩可迭代对象，*号解压可迭代对象；

7、参考地址：https://blog.csdn.net/qq_39852676/article/details/102486546
'''

_list = [1,3,5,2]
_tuple = (1,2,4,5)
_dict = {'1':'a','2':'b','3':'c'}

print(_list, "=======", *_list)
print(_tuple, "=======", *_tuple)
print(_dict, "=======", *_dict)

import numpy as np

_range = np.arange(1,3)
print(_range, "=======", *_range)


def add(*args):
    print(type(args))
    for item in args:
        print(item)

list = [1,2,3,4]
add(list)
add(*list)


# *号也可以作用于二维的列表
# 这么一看，这个带*变量的作用，就仿佛是把列表解开一层似的，而python中有一个zip函数，功能与之相反。
list1 = [[1,2,3,4], [5,6,7,8]]
print(*list1)
add(list1)
add(*list1)

# 最后需要注意的是：
# 可迭代对象才可以使用*号拆分；
# 带*号变量严格来说并不是一个变量，而更应该称为参数，它是不能赋值给其他变量的，但可以作为参数传递；


# 1、*args的使用方法
# 例子1
def function1(*args):
    print(args, type(args))
function1(1)

# 例子2
def function2(x, y, *args):
    print(x, y, args)
function2(1, 2, 3, 4, 5)


# 2、**kwargs的使用方法
# **kwargs 打包关键字参数成dict给函数体调用
# 例子1
def function3(**kwargs):
    print( kwargs, type(kwargs))
function3(a=2)


# 例子2
def function4(**kwargs):
    print(kwargs)
function4(a=1, b=2, c=3)


# 例子3
# 注意点：参数arg、*args、**kwargs三个参数的位置必须是一定的。必须是(arg,*args,**kwargs)这个顺序，否则程序会报错。
def function5(arg,*args,**kwargs):
    print(arg,args,kwargs)
function5(6,7,8,9,a=1, b=2, c=3)