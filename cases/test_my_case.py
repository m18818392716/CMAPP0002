import allure
import pytest

from pages.my_page import MyPage
from pages.topic_page import TopicPage
from utils import run_case
from utils.read_data_from_excel import read_data_from_excel


@allure.feature("测试TestMy测试用例")
class TestMy(object):
    @allure.step("执行Excel数据驱动")
    @pytest.mark.android
    @pytest.mark.parametrize("test_my_case",read_data_from_excel('./data/data_excel/test_login.xlsx', 'my_case', 'my_step'))
    # @pytest.mark.parametrize("args", readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step())
    # @pytest.mark.parametrize("args", readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step(), ids=['test1', 'test2'], name="测试登录流程")
    # @pytest.mark.parametrize(readExcel('./data/data_excel/test_login.xlsx', 'login_case').get_case_step(), name="测试登录流程")
    def test_001(self, start_app, test_my_case):

        self.driver = start_app
        self.mp = MyPage(self.driver)

        # 执行测试用例下面的每一个操作步骤
        run_case.run_case_step(self.mp, test_my_case)