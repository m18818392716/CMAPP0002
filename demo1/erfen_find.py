'''
二分查找
前提条件：列表是有序的
1、查找value是否出现在列表中
'''
# 普通方法
#定义一个二分查找的普通方法，传入两个参数，一个是列表list1，一个是要查找的值value
def binary_search_normal(list1,value):
    #拿到列表的长度
    length=len(list1)
    #列表的开始值索引
    start=0
    #列表的结束值索引
    end=length-1
    #while循环遍历
    while start<end:
        #获取列表中间位的索引值
        middle=(end+start)//2
        #判断中间位的值是否等于要查找的值value
        if(list1[middle]==value):
            #找到了匹配的值就返回True
            return True
        #判断中间位的值大于要查找的值value时
        elif(list1[middle]>value):
            #就将列表结束值的索引调整为中间位索引值+1
            end=middle-1
        else:
            #否则就是将列表开始值的索引调整为中间位索引值-1
            start=middle+1
    # 找不到时就返回False
    return False

 # 递归方法
 #定义一个二分查找的递归方法，传入两个参数，一个是列表list2，一个是要查找的值value
def binary_search_recursion(list2,value):
    #获取列表的长度
    length=len(list2)
    #获取列表的中间位索引值
    middle=length//2
    #递归结束的条件
    if length==0:
        return False
    #查找到了就返回True
    if(list2[middle]==value):
        return True
    #如果中间位的值小于value,则递归调用，传入的是中间位到结束位的列表和要查找的值
    elif(list2[middle]<value):
        return binary_search_recursion(list2[middle:],value)
    #如果中间位的值大于value,则递归调用，传入的是从开始位到中间位的列表和要查找的值
    else:
        return binary_search_recursion(list2[0:middle],value)

if __name__ == '__main__':
    # print(9//2)
    print(binary_search_normal([4,5,6,7,8,8,9,0],19))
    print(binary_search_recursion([22,33,55,66,77,88,99],22))