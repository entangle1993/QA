a = 1
try:
    a += 1
except:
    a += 1
else:
    a += 1
finally:
    a += 1
print(a)

'''
程序异常执行except
程序正常执行try和else
无论程序正常执行还是出现异常都执行finally
'''