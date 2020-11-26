from celery import Celery

wyq_app = Celery('wyqapp',broker="redis://127.0.0.1:6379/0")

@wyq_app.task()
def add():
    return 1+1




import json
def is_json():
 try:
   json_object = json.loads('123124')
 except ValueError as e:
   return False
 return True


if __name__ == '__main__':
    print(is_json())