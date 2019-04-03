# -*- coding:utf-8 -*-
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，
# 当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)  # 转换为list
        count = len(s)
        for i in range(0, count):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)


s = Solution()  # ()不能省
b = s.replaceSpace('we are happy')
print b


# 将**替换为##
def rep0(str, org, theString):
    return str.replace(org, theString)


s = 'we are happy'
print rep0(s, ' ', '%20')
