import json, jsonpath

x = {'a': 1, 'b': 2}
y = {'c': 1, 'd': 2}
z = {'a': 1, 'b': 2}

c = {**x, **y, **z}
print(c)

t1 = ('a', 'b')
t2 = ('c', 'd')
t3 = ('a', 'b')
t4 = (1, 2)

t = t1+t2+t3
print(t)

d = dict(zip(t1,t4))
print(d)
print(len(d))

print(d.items())
print(type(d.items()))

print(d.keys())
print(type(d.keys()))

print(d.values())
print(type(d.values()))


l1 = ['a', 1, ('c', 'd'), {'a': 1, 'b': 2}]
l2 = ['e', 1, ('c1', 'd1'), {'a1': 1, 'b1': 2}]
l3 = ['f', 1, ('c2', 'd2'), {'a2': 1, 'b2': 2}]

l = l1+l2+l3

print(l)
print(len(l))


ff = None
gg = None
if ff:
    print('is not None')
if not gg:
    print('is None')


json_data = {
    "code": 0,
    "message": "0",
    "ttl": 1,
    "data": {
        "isLogin": True,
        "email_verified": 0,
        "face": "http://i1.hdslb.com/bfs/face/17061e541785832b44426c51429ddfee39.jpg",
        "level_info": {
            "current_level": 0,
            "current_min": 0,
            "current_exp": 0,
            "next_exp": 1
        },
        "mid": 377206,
        "mobile_verified": 1,
        "money": 0,
        "moral": 70,
        "official": {
            "role": 0,
            "title": "",
            "desc": "",
            "type": -1
        },
        "officialVerify": {
            "type": -1,
            "desc": ""
        },
        "pendant": {
            "pid": 0,
            "name": "",
            "image": "",
            "expire": 0
        },
        "scores": 0,
        "uname": "洒脱喽",
        "vipDueDate": 0,
        "vipStatus": 0,
        "vipType": 0,
        "vip_pay_type": 0,
        "vip_theme_type": 0,
        "wallet": {
            "mid": 377206,
            "bcoin_balance": 0,
            "coupon_balance": 0,
            "coupon_due_time": 0
        },
        "has_shop": False,
        "shop_url": "",
        "allowance_count": 0,
        "answer_status": 1
    }
}

print(type(json_data))
# 将字典dict--》转化为--》str  json字符串   称之为序列化
str_json = json.dumps(json_data)
print(str_json, type(str_json))

# 将str  json字符串--》转化为--》字典dict   称之为反序列化
dict_json = json.loads(str_json)
print(dict_json, type(dict_json))

data1 = jsonpath.jsonpath(json_data, '$.data')
print(data1, type(data1))

# 将json字符串--》转化成--》dict   称之为反序列化
# 将json文件读取出来，写入到dict字典中
with open('./data_files/dict_json.txt', mode='r', encoding='utf-8') as file:
    data_dict = json.load(file)
print(data_dict, type(data_dict))

# 将python数据类型-字典 写入到文件中
one_dict = {'name': 'zhangsan', 'age': 18, 'city': 'guangzhou'}
with open('./data_files/one_dict_json.txt', mode='a', encoding='utf-8') as file1:
    one_dict_dict = json.dump(one_dict, file1, ensure_ascii=False)

# 将python数据类型-元祖 写入到文件中
one_tuple = ('zhangsan', '18', 'guangzhou')
with open('./data_files/one_tuple_json.txt', mode='a', encoding='utf-8') as file2:
    one_tuple_dict = json.dump(one_tuple, file2, ensure_ascii=False)

# 将python数据类型-列表 写入到文件中
one_list = ['zhangsan', 18, 'guangzhou']
with open('./data_files/one_list_json.txt', mode='a', encoding='utf-8') as file3:
    one_list_dict = json.dump(one_list, file3, ensure_ascii=False)


