# 一行一行读取文件
# 参考地址：https://blog.csdn.net/qq_40690208/article/details/102918763
def read_txt():
    file = open('./data_files/test.txt', 'r', encoding='utf-8')
    while True:
        text = file.readline()
        if not text:
            break
        print(text)
    file.close()

# 小文件的复制
# 读取完整的内容，并写入另一个文件
def read_and_copy_small_file():
    # 1.打开文件
    file1 = open('./data_files/test.txt', 'r', encoding='utf-8')
    file2 = open('./data_files/kaka附件.txt', 'w', encoding='utf-8')
    # 2.读写文件
    text = file1.read()
    file2.write(text)
    # 3.关闭文件
    file1.close()
    file2.close()

# 大文件的复制：
# 打开一个已有的文件逐行的读取内容，并按顺序写入到另一个文件
def read_and_copy_big_file():
    # 打开文件
    file1 = open('./data_files/test.txt', 'r', encoding='utf-8')
    file2 = open('./data_files/kaka复制.txt', 'w', encoding='utf-8')
    while True:
        test = file1.readline()
        if not test:
            break
        file2.write(test)
    # 关闭文件
    file1.close()
    file2.close()


read_txt()
read_and_copy_small_file()
read_and_copy_big_file()