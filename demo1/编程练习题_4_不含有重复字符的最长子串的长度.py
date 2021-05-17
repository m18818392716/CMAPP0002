'''
原文链接：https://blog.csdn.net/shiki99/article/details/107870533

'''


'''
方法一：暴力破解

遍历并找出所有无重复的最长连续子串
缺点：时间复杂度、空间复杂度都很高
'''


'''
方法二：滑动窗口法
如：abcadsfd:窗口到(abc)adsfd时，遇到a，窗口右移(abc)adsfd -> a(bca)dsfd
记录每个窗口的长度，大的放入max里。
'''
def lengthOfSubstring2(s):
    max_length = 0
    lst = []

    if not s:
        return 0

    for x in s:
        if x not in lst:
            lst.append(x)
        else:
            max_length = max(len(lst), max_length)
            lst.append(x)
            lst = lst[lst.index(x) + 1:]  # 发现重复，从重复的右边开始计算
        max_length = max(len(lst), max_length)
    return max_length

s = 'abcadsfd'
a = lengthOfSubstring2(s)
print(a)



'''
方法三：双指针法
#如果字符不在滑动窗口中，则直接扩展窗口
    # 如果字符在滑动窗口中，则
    # 1. 从窗口中移除重复字符及之前的字符串部分
    # 2. 再扩展窗口
    # 在滑动窗口范围内中找出对应的首个字符的索引X，对应的新的左指针位置为X + 1
    # 左指针右移 索引X增一 位
'''
def lengthOfSubstring3(s):
    # 字符串为空则返回零
    if not s:
        return 0
    max_length = 0  # 滑动窗口数组
    left, right = 0, 0  # 双指针
    for c in s:
        if c not in s[left:right]:
            # 右指针右移一位
            right += 1
        else:
            left += s[left:right].index(c) + 1  # 只要是在滑动窗口内找索引，就不用担心三个以上的相同元素了
            # 右指针右移一位
            right += 1
        max_length = max(right - left, max_length)  # 更新最大长度
    # 如果最大长度不为零，返回最大长度
    # 如果最大长度仍为零，则说明遍历整个字符串都没有发现重复字符，最大长度即为字符串本身的长度
    return max_length if max_length != 0 else len(s)
