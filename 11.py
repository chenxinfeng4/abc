#this is a test module
##a='a'
##b='b'
##if a=='a':
##    print('eex')
##else:
##    print('yyy')
##print(33)

##b=range(2,10)
##for a in b:
##    print(-a)
##    if a==4:continue
##    print(a)
##
def foo(arg1,arg2='cxf',*tr):
    'display 2 regular ,and key value'
    print(arg1,arg2)
    for namei in tr:
        print('±ä³¤: %s= %s' % (namei,'+++'))

a=foo(3)
a=foo(3,'34')
