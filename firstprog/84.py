import calendar
import time
# t=time.localtime()
# print(t)
# i=1
# init=time.time()
# for i in range (10000):
#     print(i)
# t1=time.time()-init
# # print(t1)
#
# init=time.time()
# while i<50000:
#     i=i+1
#     print(i)
# t2=time.time()-init
# print(t2)
# time.sleep(3)
# print(t1)

t=time.localtime()
formattedtime=time.strftime("%Y-%m-%d",t)
print(formattedtime)
formattedtime=time.strftime("%Y-%B-%d %H:%M:%S",t)
print(formattedtime)
abcd = calendar.month_name[int(time.strftime("%m",t))]
print(calendar.month_name[int(time.strftime("%m",t))][0:3])
q=time.clock()
print(q)