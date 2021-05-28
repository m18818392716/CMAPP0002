"""

"""

"""

"""

s = "I am Susanna，I Like China， I live in Guanghzou Susanna"

print(s.index('Susanna'))
print(s.index('S'))
print(s.index('Susanna', 40))
print(s.index('Susanna', 40, len(s)))
# print(s.index('X'))   # ValueError: substring not found

print(s.find('Susanna'))
print(s.find('S'))
print(s.find('Susanna', 40))
print(s.find('Susanna', 40, len(s)))
# print(s.find('X'))  #  没有找到  返回-1

print(s.rfind('Susanna'))  #  从右边开始找，找到第一个匹配的内容的index

"""

"""

from collections import Counter

print(Counter(s))
print(dict(Counter(s)))

m = 2
lst = []

#

# 列表推导式
print('----------')
# 列表推导式进行处理
lst1 = [i for i, j in dict(Counter(s)).items() if j == 2]
print(lst1[m-1])

# for循环进行处理
for i, j in dict(Counter(s)).items():
    print(i, j)
    if j == 2:
        lst.append(i)
print(lst[m-1])


# for x in range(0,10):
#     print(x)
print(x for x in range(0,10))
print('打印数组：', [x for x in range(0,10)])

# for x in range(0,10,2):
#     print(x)

print(x for x in range(0,10,2))
print('打印数组：', [x for x in range(0,10,2)])


print('请输入一个数：')
s = input()
print(type(s))
print(int(s), type(int(s)))


a = 5
b = 2

print(a+b) #7
print(a/b) #2.5
print(a*b) #10
print(a-b) #3
print(a%b) #1
print(a//b) #2
print(a**b)  #25






