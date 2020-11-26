# -*- coding: utf-8 -*-
# @Time    : 2020-05-21 20:47
# @Author  : wyq
# @File    : retustr.py
# @Software: PyCharm


class restr():
    Rtr=''

    @classmethod
    def getstr(cls):
        return cls.Rtr


    @classmethod
    def setstr(cls,data):
        cls.Rtr=data
        restr.Rtr



if __name__ == '__main__':
    print(restr.Rtr)
    # print(restr.setstr('23131'))
    # print(restr.Rtr)

    A=restr()
    t=getattr(A,'Rtr')
    tt=setattr(A,'setstr','hhhh')
    ttt=getattr(A,'Rtr')

    print(t)
    print(tt)
    print(ttt)


