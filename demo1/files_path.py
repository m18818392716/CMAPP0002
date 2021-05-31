'''
os.path.dirname()操作
os.path.abspath(__file__)
os.walk()操作
'''

'''
os.walk(top, topdown=True, onerror=None)需要三个参数
其中top是必须给的路径变量，后两个可以不给，但是系统默认的有值，就是上面 写的那种
它的返回值是元组的形式，包括每次遍历的路径名，文件夹名，文件名（其中文件路径是字符串形式，文件夹是列表，文件名也是列表）
os.walk(top, func, arg)：需要三个参数，top是路径，func是迭代函数，arg是参数，他们都是必须给出的系统不会默认初始值


两者都能实现达到同一个效果：
    1、在python3中， os.path.walk要被os.walk取代了，大家尽量用os.walk
    2、os.walk明显比os.path.walk要简洁些，起码它不需要回调函数，遍历的时候一目了然：root, sundirs, files
    3、当os.path.walk()赋值给arg的时候，你就可以在第二个参数对应的func中用arg了
'''
import os
'''
文件路径：

'''
current_path = os.path.dirname(os.path.abspath(__file__))
print('当前操作文件路径为：{}'.format(current_path)) # 输出：当前操作文件路径为：D:\software\githubRespository\CMAPP0002\demo1

path = os.path.join(current_path)
print(path) # 输出：D:\software\githubRespository\CMAPP0002\demo1

'''
方式1：
    下面的代码在扫描子目录和文件的时候，是采用自顶向下的方式进行扫描。
    如果想要自底向上地扫描子目录和文件，可以添加上topdown=False参数：
'''
# 使用os.walk自顶向下扫描目录
# for curDir, dirs, files in os.walk("."):
#     print("====================")
#     print("现在的目录：" + curDir)
#     print("该目录下包含的子目录：" + str(dirs))
#     print("该目录下包含的文件：" + str(files))
# 输入结果：
'''
====================
现在的目录：.
该目录下包含的子目录：['data_files']
该目录下包含的文件：['dict_muldemo.py', 'erfen_find.py', 'factory_method.py', 'files_path.py', 'find_index_end_withs_starts_with.py', 'format_list_to_dict.py', 'jsonpath_demo.py', 'lambda匿名函数.py', 'read_data_file_demo.py', 'selection_sort.py', 'sort_list.py', 'string_reverse.py', 'tuple_list_dict_demo.py', '__init__.py', '列表_字典_集合之间的相互转化.py', '可迭代对象_迭代器_生成器.py', '编程练习题_1_提取公共的字符串前缀.py', '编程练习题_2_斐波那契数列求和.py', '编程练习题_3_调整数组顺序使奇数位于偶数前面.py', '编程练习题_4_不含有重复字符的最长子串的长度.py']
====================
现在的目录：.\data_files
该目录下包含的子目录：[]
该目录下包含的文件：['dict_json.txt', 'kaka复制.txt', 'kaka附件.txt', 'one_dict_json.txt', 'one_list_json.txt', 'one_tuple_json.txt', 'test.txt', '__init__.py']
'''




'''
方式2：
    使用os.walk自底向上扫描目录：
'''
# 使用os.walk自底向上扫描目录
# for curDir, dirs, files in os.walk(".", topdown=False):
#     print("====================")
#     print("现在的目录：" + curDir)
#     print("该目录下包含的子目录：" + str(dirs))
#     print("该目录下包含的文件：" + str(files))
# 输入结果：
'''
====================
现在的目录：.\data_files
该目录下包含的子目录：[]
该目录下包含的文件：['dict_json.txt', 'kaka复制.txt', 'kaka附件.txt', 'one_dict_json.txt', 'one_list_json.txt', 'one_tuple_json.txt', 'test.txt', '__init__.py']
====================
现在的目录：.
该目录下包含的子目录：['data_files']
该目录下包含的文件：['dict_muldemo.py', 'erfen_find.py', 'factory_method.py', 'files_path.py', 'find_index_end_withs_starts_with.py', 'format_list_to_dict.py', 'jsonpath_demo.py', 'lambda匿名函数.py', 'read_data_file_demo.py', 'selection_sort.py', 'sort_list.py', 'string_reverse.py', 'tuple_list_dict_demo.py', '__init__.py', '列表_字典_集合之间的相互转化.py', '可迭代对象_迭代器_生成器.py', '编程练习题_1_提取公共的字符串前缀.py', '编程练习题_2_斐波那契数列求和.py', '编程练习题_3_调整数组顺序使奇数位于偶数前面.py', '编程练习题_4_不含有重复字符的最长子串的长度.py']

'''





'''
方式3：
    我们还可以利用os.walk输出test文件夹下所有的文件：
'''
# 使用os.walk输出某个目录下的所有文件
# for curDir, dirs, files in os.walk("."):
#     for file in files:
#         print(os.path.join(curDir, file))
# 输入结果：
'''
.\dict_muldemo.py
.\erfen_find.py
.\factory_method.py
.\files_path.py
.\find_index_end_withs_starts_with.py
.\format_list_to_dict.py
.\jsonpath_demo.py
.\lambda匿名函数.py
.\read_data_file_demo.py
.\selection_sort.py
.\sort_list.py
.\string_reverse.py
.\tuple_list_dict_demo.py
.\__init__.py
.\列表_字典_集合之间的相互转化.py
.\可迭代对象_迭代器_生成器.py
.\编程练习题_1_提取公共的字符串前缀.py
.\编程练习题_2_斐波那契数列求和.py
.\编程练习题_3_调整数组顺序使奇数位于偶数前面.py
.\编程练习题_4_不含有重复字符的最长子串的长度.py
.\data_files\dict_json.txt
.\data_files\kaka复制.txt
.\data_files\kaka附件.txt
.\data_files\one_dict_json.txt
.\data_files\one_list_json.txt
.\data_files\one_tuple_json.txt
.\data_files\test.txt
.\data_files\__init__.py
'''


'''
方式4：
    使用os.walk输出某个特定后缀(比如.txt)的文件
'''
# 使用os.walk输出某个特定后缀(比如.txt)的文件
# for curDir, dirs, files in os.walk("."):
#     for file in files:
#         if file.endswith(".txt"):
#             print(os.path.join(curDir, file))
# 输入结果：
'''
.\data_files\dict_json.txt
.\data_files\kaka复制.txt
.\data_files\kaka附件.txt
.\data_files\one_dict_json.txt
.\data_files\one_list_json.txt
.\data_files\one_tuple_json.txt
.\data_files\test.txt
'''



'''
方式5：
    使用os.walk输出所有的目录
'''
# 使用os.walk输出所有的目录
for curDir, dirs, files in os.walk("."):
    for dir in dirs:
        print(dir)

# 输入结果：
'''
data_files
'''