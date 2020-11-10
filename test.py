# import os
# import django
# # 行是必须的
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djorm_alone.settings")

# # from djorm_alone import migrate, make_migrations
# from wechat import models
# # from demox import do_demo
# # from djorm_alone import urls
# import time
# import random
# import threading
# django.setup()


# from djorm_alone import urls

import os 
import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djorm_alone.settings") 
django.setup()
from wechat.models import *

def update():
    while True:
        try:
            obj = models.User.objects.first()
            obj.name = obj.name + 1
            obj.save()
            print("update:", object)
            # time.sleep(random.random()*0.5)
        except Exception as err:
            print("update:", "-" * 40)
            print(err)
        break


def create():
    while True:
        try:
            obj = models.User.objects.create(name=random.randint(0, 100))
            print("create:", obj)
            # time.sleep(random.random() * 0.5)
        except Exception as err:
            print("create:", "-" * 40)
            print(err)


def select():
    while True:
        try:
            print("select:", models.User.objects.all()[:5])
            # time.sleep(0.5)
        except Exception as err:
            print("select:", "-" * 40)
            print(err)
        break


def delete():
    while True:
        try:
            obj = models.User.objects.first()
            print("delete:", obj)
            obj.delete()
            # time.sleep(0.5)
        except Exception as err:
            print("delete:", "-" * 40)
            print(err)
        break


if __name__ == '__main__':
    # do_demo()
    # make_migrations("app01")
    # migrate("app01")
    u = Wechat.objects.create(title="2")
    u.save()
    print(len(Wechat.objects.all()))
    # # threading.Thread(target=update).start()
    # # threading.Thread(target=create).start()
    # threading.Thread(target=select).start()
    # # threading.Thread(target=delete).start()