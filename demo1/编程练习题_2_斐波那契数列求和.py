"""
斐波那契数列： 1,1,2,3,5,8......

"""

def feibo_sum(s):

    a = 0
    b = 1
    n = 1
    print(b)

    while n <= s:
        n = a + b
        a, b = b, n
        if n >100:
            break
        else:
            print(n)

# feibo_sum(100)

'''
求和：3+33+333+3333+33333
'''
m = 5
n = 3
next_a = 0

sum = 0

for i in range(m):
    next_a+=n*10**i
    print(next_a)
    sum+=next_a
    # print(sum)

print(sum)


'''
求和：1！+2！+3！+4！+5！+...+10!
'''

m = 10
a = 1
sum = 0

for i in range(1, m+1):
    a*=i
    print(a)
    sum+=a

print(sum)




