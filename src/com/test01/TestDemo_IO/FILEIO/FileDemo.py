#coding:utf-8
"""这里测试IO文件流-读入中文不显示为Unicode编码"""
import sys
import codecs
"""读文件"""
print(sys.getdefaultencoding())
with codecs.open('D:\\A\\a.xml', encoding='utf-8') as fo:
    value=fo.read()
    print(value)
    fo.close()

"""方式二"""
f=open('D:\\A\\a.xml',encoding='utf-8')
text=f.read()
print(text)
f.close()


"""写"""
