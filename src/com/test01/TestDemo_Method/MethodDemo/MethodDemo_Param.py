# -*- coding: utf-8 -*-
"""
    自定义函数实例

    1.刻板参数的自定义函数
    https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000
    2.关键字参数 _在调用该函数时，可以只传入必选参数
    3.命名关键字参数
    4.参数组合

"""
def NormalCalc(number):
    sumnum=0
    for n in number:
        sumnum+=n
    print(sumnum)

def ProfessorCalc(*number):
    sumnum = 0
    for n in number:
        sumnum += n
    print(sumnum)


def NormalKeyword(bh,**value):
    print('bh:',bh,'\n','value:',value)

def NormalNamespace(name,*,size):
    print('name:',name,'\t size:',size)

def ProfessorNamespace(name,*params,size):
    print('name:',name,'\t others:',params,'\t size:',size)

def ParamType1(p1,p2,p3=0,*args,**args2):
    print('p1:',p1,'\t p2:',p2,'\t p3:',p3,'\t args:',args,'\t args2:',args2)

def ParamType2(p1,p2,p3=0,*,args,**args2):
    print('p1:', p1, '\t p2:', p2, '\t p3:',p3,'\t args:', args, '\t args2:', args2)

# 调用
if __name__=="__main__":
    print('普通函数:NormalCalc([1,2,3,4])')
    NormalCalc([1,2,3,4])
    print('可变参数:ProfessorCalc(5,6,7,8)')
    ProfessorCalc(5,6,7,8)
    print("可变参数应用扩展：ProfessorCalc(*param)")
    param=[2,4,6,8]
    ProfessorCalc(*param)
    print('关键字参数:NormalKeyword')
    NormalKeyword(1,name='李白',comefrom='唐朝',age='36+?')
    # ** extra表示把extra这个dict的所有key - value用关键字参数传入到函数的 ** kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
    extra={'name':'杜甫','sex':'男'}
    NormalKeyword(2,**extra)
    print('命名关键字参数:NormalNamespace')
    NormalNamespace('me',size=18)
    print('命名关键字参数:')
    ProfessorNamespace('you',1,2,3 , size=18)
    ProfessorNamespace('you', size=18)
    print("参数组合：ParamType1")
    ParamType1(1,1,1,2,3,key=1,key2=1)
    print("参数组合：ParamType2")
    ParamType2(2,2,args='b',key=2,key2=2)
    print("参数组合：Master用法")
    args=(1,2,3,4)
    ParamType1(*args)
    args2=(1,2,3)
    fill={'args':'123'}
    ParamType2(*args2,**fill)