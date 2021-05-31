import json
origin_result_data = [b'*************************** 1. row ***************************\n',
                      b'id: 1\n',
                      b' param_name: enterprise\n',
                      b'param_value: {"name": "", "abbreviation": "", "description": " EditByHS form APIs", "logo_path": ""}\n',
                      b'description:  \n',
                      b'      level: 1\n',
                      b'update_time: 1970-01-01 00:00:00.000000\n',
                      b'  parent_id: NULL\n',
                      b'*************************** 2. row ***************************\n',
                      b'         id: 2\n',
                      b' param_name: init_password\n',
                      b'param_value: 0\n',
                      b'description:   \n',
                      b'      level: 1\n',
                      b'update_time: 0000-00-00 00:00:00.000000\n',
                      b'  parent_id: NULL\n',
                      b'*************************** 3. row ***************************\n',
                      b'         id: 3\n',
                      b' param_name: clear_log_info\n',
                      b'param_value: {"set_time": "2020-08-14", "clear_interval": 0}\n',
                      b'description:  \n',
                      b'      level: 1\n',
                      b'update_time: 0000-00-00 00:00:00.000000\n',
                      b'  parent_id: NULL\n']
#去除\n、空格字符
s = [x.strip() for x in origin_result_data if x.strip() != '']
print('s is {}'.format(s))
for i in s:
    if "****" in str(i):
        #去除字符串中包含***的字符串，即删除掉每一条数据的第一行
        s.remove(i)


def list_of_groups(list_info, per_list_len):
    """
    :param list_info:   列表
    :param per_list_len:  每个小列表的长度
    :return:
    """
    list_of_group = zip(*(iter(list_info),) * per_list_len)
    end_list = [list(i) for i in list_of_group]  # i is a tuple
    count = len(list_info) % per_list_len
    end_list.append(list_info[-count:]) if count != 0 else end_list
    print('end_list is {}'.format(end_list))
    return end_list


def test_ret():
    list_info = s
    # 将大列表中每7个元素组成一个小列表
    ret = list_of_groups(list_info, 7)
    return ret

target_result_data = []
# 大列表中的每一个小列表转化成对应的字典，最终通过一个List进行装起来
for item in test_ret():
    data = {}
    data['id'] = str(item[0]).split(": ")[1].split("'")[0]
    data['param_name'] = str(item[1]).split(': ')[1].split("'")[0]
    if str(item[2]).split(": ")[1].split("'")[0] == '0':
        data['param_value'] = 0
    else:
        data['param_value'] = "{" + str(item[2]).split(": {")[1].split("'")[0]
        data['param_value'] = json.loads(data['param_value'])
    data['description'] = str(item[3]).split(':')[1].split("'")[0]
    data['level'] = str(item[4]).split(': ')[1].split("'")[0]
    data['update_time'] = str(item[5]).split(': ')[1].split("'")[0]
    data['parent_id'] = str(item[6]).split(': ')[1].split("'")[0]
    target_result_data.append(data)
print(target_result_data)

for i in target_result_data:
    print(i)