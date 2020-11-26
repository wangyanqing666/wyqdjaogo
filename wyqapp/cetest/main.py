# from celery import Celery
# from wyqapp.cetest import config
# from wyqapp.cetest.task import add
# # 定义对象
#
# wyq_app = Celery('wyqapp',include=["wyqapp.cetest.task"])
#
# # # 引入配置
# wyq_app.config_from_object(config)
# # # 自动加载异步任务
# # wyq_app.autodiscover_tasks(['wyqapp.task_sm.sm'])
#
#
#
# if __name__ == '__main__':
#     result = add.delay()
