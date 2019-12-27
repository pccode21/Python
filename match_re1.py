import re
def main():
    username=input('请输入用户名：')
    qq=input('请输入QQ号：')
    m1=re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    '''
    上面在书写正则表达式时使用了“原始字符串”的写法（在字符串前面加上了r），
    所谓“原始字符串”就是字符串中的每个字符都是它原始的意义，
    说得更直接一点就是字符串中没有所谓的转义字符。
    '''
    if not m1:
        print('请输入有效的用户名.')
    m2=re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')
if __name__=='__main__':
    main()