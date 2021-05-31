'''
冒泡排序：
1、
'''
import time


def waste_time(func):  # 计算方法执行时长的装饰器
    def function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        spend = end_time - start_time
        print("函数%s 总共耗时%.3f秒:" % (func.__name__, spend))
        return result

    return function


@waste_time
def bubbleSort(alist):  # 传入一个列表，如果是有序的，则只需要检测一轮，查看是否进行交换，如果没有进行交换，说明是有序列表则直接退出循环
    n = len(alist)
    for i in range(n - 1):
        count = 0  # 用于标记是否有交换的情况
        for j in range(n - 1 - i):
            if (alist[j] > alist[j + 1]):
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        # 判断count是否等于0，如果是0的话表示没有交换
        if (count == 0):
            break

def bubbleSort1(alist):  # 传入一个列表，如果是有序的，则只需要检测一轮，查看是否进行交换，如果没有进行交换，说明是有序列表则直接退出循环
    n = len(alist)
    for i in range(n - 1):
        count = 0  # 用于标记是否有交换的情况
        for j in range(n - 1 - i):
            if (alist[j] > alist[j + 1]):
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        # 判断count是否等于0，如果是0的话表示没有交换
        if (count == 0):
            break
    return alist




if __name__ == '__main__':
    alist = [9, 20, 5, 88, 66, 77, 30]  # 无序列表
    print("the init list is:", alist)
    bubbleSort(alist)
    print("the sorted list is:", alist)
    blist = [5, 9, 20, 30, 66, 77, 88]  # 有序列表
    bubbleSort(blist)
    print(blist)
    print('-'*3)
    print(bubbleSort1(alist))