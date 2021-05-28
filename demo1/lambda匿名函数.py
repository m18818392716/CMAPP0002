L = [1,2,3,4,1,2,3,4,5,6]

for x in L:
    print(str(x))

# print([str(x) for x in L])

print("".join([str(x) for x in L]))


# 列表推导式
L2 = [[1,2],[3,4]]
print([j for i in L2 for j in i])


L3 = [1,2,3,4,1,2,3,4,5,6]
print(max(L3, key= lambda x: L3.count(x)))

L4 = ["张三","李四","王五","张三三"]

print(list(filter(lambda x : not str(x).startswith('张'), L4)))

