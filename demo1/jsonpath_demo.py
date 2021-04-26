import time
import threading
# 参考地址：https://blog.csdn.net/weixin_33265107/article/details/112240911

class Singleton(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls,*args,**kwargs):
        with cls._instance_lock:
            if not hasattr(Singleton,'_instance'):
                Singleton._instance=Singleton()
                return Singleton._instance
            return Singleton._instance

def task():
    print('执行线程任务\n')
    obj = Singleton.instance()
    print(obj)


for i in range(10):
    t=threading.Thread(target=task)
    print('第{}个线程'.format(i))
    t.start()

