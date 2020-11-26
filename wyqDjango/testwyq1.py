# from datetime import datetime
# from datetime import timedelta
#
# # 1) 获取当前日期和时间
# today = datetime.today()    # 返回当前时间时分秒都为0
# print("当前时间")
# print(today)

# import sys
# list1 = []
# while True:
#     line = sys.stdin.readline().strip()
#     if line is '\n':
#             break
#
#     a = line.split()
#     print(a)
#     for i in a:
#         list1.append(int(i))
#     print(list1)
#
import sys
#
# for line in sys.stdin:
#     print(line, end="")
#     print('王彦青')

# a=int(input("请输入正整数"))
# b=int(input("请输入正整数"))
#
# try:
#     t=a/b
# except Exception as  e:
#     print(e)
# else:
#     print(111)
# finally:
#     print(222)
#
# print(t)


str="\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04name\x94\x8c\awyqtest\x94s."
print(str.encode('utf-8'))