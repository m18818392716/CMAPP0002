import subprocess

import pytest

from config.myLog import MyLog
import time
def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o

if __name__ == '__main__':
    xml_report_path = './allure-result/xml'
    html_report_path = './allure-report/html'
    tm = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
    logger = MyLog().log()
    # args = ['-s', '-q', "./cases/test_search_case.py", "./cases/test_login_case.py"]
    args = ["run_all_cases.py"]
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    invoke(cmd)
    logger.info("-----------------------------END: %s------------------------------------" % tm)