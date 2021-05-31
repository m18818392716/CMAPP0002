'''
选择排序
1、针对无序的列表进行排序
    1）升序
    2）降序

'''

# 定义选择排序方法，传入一个alist列表
def selection_sort_desc(alist):
    # 第一层for循环表示用来遍历要整体执行的次数
    for i in range(len(alist) - 1):
        # 将alist里面的第一个元素设置为最大元素，用的是索引来标记
        max_index = i
        # 第二层for循环表示是进行alist列表中的数据两两比较
        for j in range(i + 1, len(alist)):
            # 第一循环判断alist[1]>alist[0]时
            if (alist[j] > alist[max_index]):
                # 就将大值的索引值赋值给max_index
                max_index = j
        # 将最大值与alist列表里面的元素进行逐个互换排序
        alist[max_index], alist[i] = alist[i], alist[max_index]
    return alist  # 返回最后排序后的alist列表

def selection_sort_asc(alist):
    # 第一层for循环表示用来遍历要整体执行的次数
    for i in range(len(alist) - 1):
        # 将alist里面的第一个元素设置为最大元素，用的是索引来标记
        min_index = i
        # 第二层for循环表示是进行alist列表中的数据两两比较
        for j in range(i + 1, len(alist)):
            # 第一循环判断alist[1]>alist[0]时
            if (alist[j] < alist[min_index]):
                # 就将大值的索引值赋值给max_index
                min_index = j
        # 将最大值与alist列表里面的元素进行逐个互换排序
        alist[min_index], alist[i] = alist[i], alist[min_index]
    return alist  # 返回最后排序后的alist列表


if __name__ == '__main__':
    alist = [449, 333, 441, 555, 666, 777, 888, 999, 332, 222, 111]
    print("the init of list is:", alist)
    print("the desc sorted of list is:", selection_sort_desc(alist))
    print("the asc sorted of list is:", selection_sort_asc(alist))