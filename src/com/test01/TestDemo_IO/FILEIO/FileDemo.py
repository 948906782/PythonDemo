# -*- coding: utf-8 -*-
"""这里测试IO文件流-读入中文不显示为Unicode编码
http://www.runoob.com/python/python-files-io.html
"""
import sys
import codecs
"""读文件"""
print(sys.getdefaultencoding())
with codecs.open('D:\\A\\a.xml','r', encoding='utf-8') as fo:
    value=fo.read()
    print(value)
    fo.close()

"""方式二"""
f=open('D:\\A\\a.xml','r',encoding='utf-8')
text=f.read()
print(text)
f.close()


"""写"""
fw=open('D:\\A\\a.txt','w',encoding='utf-8')
insert='这是一个新的我'
fw.write(insert)
fw.close()

"""不去除原来的记录"""
fa=open('D:\\A\\a.txt','a+',encoding='utf-8')
newins='\n 保持原来的我，添加一条记录'
fa.write(newins)
fa.close()