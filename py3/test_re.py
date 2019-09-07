import re
# 捕获组就是把正则表达式中子表达式匹配的内容，保存到内存中以数字编号或显式命名的组里，方便后面引用。
# 当然，这种引用既可以是在正则表达式内部，也可以是在正则表达式外部。
pattern = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
str = '15.6.7.5'   #非捕获组? 正则都是单字符匹配


i= re.match(pattern,str)
if i:
       print(i)
else:
       print('sakupopo')

p =r'^1([3-9])\d{9}$'
print(re.match(p,'15899999699'))

p1 = 'industr(y|ies)'  #()等价于(?:)
print(re.match(p1,'industries'))

p2 = "Windows(?!95|98|NT|2000)"
print(re.match(p2,'Windows200'))