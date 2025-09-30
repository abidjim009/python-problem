#print current date and time

import datetime

now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print ("Current year:",now.year)
print ("Current month:",now.month)
print ("Current day:",now.day)
print ("Current hour:",now.hour)
print ("Current minute:",now.minute)
print ("Current second:",now.second)
print ("Current microsecond:",now.microsecond)
