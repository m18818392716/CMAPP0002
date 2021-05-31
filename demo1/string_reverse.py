"""
字符转的反转  与  字母大小写的转换   与  单词的分割
"""

# 方法一
a = "MyNameIsTom"
aa = []
s = ""
for i in a:
    if i.isupper():
        # 如果是大写
        if len(s) == 0:
            s += i
        else:
            aa.append(s)
            s = ''
            s += i
    else:
        s += i

if len(s) > 0:
    aa.append(s)

print(aa)  # 得到列表['My', 'Name', 'Is', 'Tom']

# 对列表单词反转并大小写反转
result = []
for j in aa:
    reverse_j = j[::-1]
    result.append(reverse_j)

print("方法一的输出结果如下：")
print("".join(result)) # yMemaNsImoT


# 方法二：采用正则匹配
import re

str1 = "MyNameIsTom"
str_list = re.findall("([A-Z]{1}[a-z]+)", str1)
print(str_list)  # 正则匹配全部单词
str2 = ''.join(i[::-1] for i in str_list)
print("方法二的输出结果如下：")
print(str2)
