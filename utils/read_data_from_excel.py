import os

from openpyxl import load_workbook


def read_data_from_excel(excel_file, sheeet_case, sheet_step):
    return_value = []
    # 判断文件是否存在
    if not os.path.exists(excel_file):
        raise ValueError("File not exists")

    # 打开指定的sheet
    wb = load_workbook(excel_file)
    sheet_case = wb[sheeet_case]
    sheet_step = wb[sheet_step]

    cases = []  # 新建一个空列表，用于存放读取出的数据
    titles = []  # 新建一个空列表，用于存放读取到的表头，也就是1,2,3,4,5这一行
    rows = list(sheet_case.rows)  # 这里是将指定的sheet页中所有存在数据的行全都读取出来，转换成列表类型存放，方便我们进行遍历
    for row in rows[0]:
        titles.append(row.value)  # 将每一个表格的value值，也就是我们需要的数据，添加的空列表中。
    # 这里是遍历除了表头一行，剩下的所有行
    for row in rows[1:]:
        data = []
        for r in row:  # 遍历每一行的每一个表格
            data.append(r.value)
        data_zip = dict(zip(titles, data))  # 然后将每一行读取到的测试数据，和表头进行打包成一个字典的形式存放。
        cases.append(data_zip)  # 将所有测试数据添加到一个空列表中

    case_list_name = []
    for value in cases:
        if type(value) is dict:
            if value['is_run'] == 'Yes':
                case_list_name.append(value['case_id'])
            else:
                pass
        else:
            pass
    print('case list name is {}'.format(case_list_name))

    case_list_carry = []
    rows_step = list(sheet_step.rows)
    # print('rows_step is {}'.format(rows_step))
    step_titles = []
    step_cases = []

    for value in rows_step[0]:
        step_titles.append(value.value)

    for i in rows_step[1:]:
        data_1 = []
        for j in i:
            data_1.append(j.value)
        step_zip = dict(zip(step_titles, data_1))
        step_cases.append(step_zip)

    for value in case_list_name:
        case_list = []
        for i in step_cases:
            if type(i) is dict:
                if i['用例编号'] == value:
                    case_list.append(i)
                    # print(i)
                else:
                    pass
            else:
                pass
        case_list_carry.append(case_list)
    else:
        pass

    print('case list carry is {}'.format(case_list_carry))
    wb.save(excel_file)
    wb.close()
    return case_list_carry