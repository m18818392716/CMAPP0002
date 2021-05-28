# CMAPP0002
基于Pytest+Appium+Excel数据驱动的自动化测试框架，实现Jenkins可持续集成，实现测试报告的打包的自动发送

安装生成requirements.txt依赖命令：pip install -r requirements.txt

生成requirements.txt：pip freeze > requirements.txt


项目结构：
    1、base（基类）
    2、page（页面对象类）
    3、case（测试用例）
    4、data（测试数据）
    5、config（配置类）
    6、Logs（日志类）
    7、utils（工具类）
    8、apk（安装包文件类）
    9、demo（H5切换原生和webview测试类）
    10、demo1（编程基础类）
    11、conftest.py(配置文件，设定前置和后置操作，记住：名字不可以修改)
    12、pytest.ini（pytest运行命令配置文件，记住：名字不可以修改）
    13、run_all_cases.py
    
 配置类：
    1、conf_files
    2、conf_web
    3、conf_excel

