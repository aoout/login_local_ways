import os

mode='r+' if os.path.exists('user.txt') else 'w+'

with open('user.txt',mode) as f:
    name_input=input('请输入用户名')
    password_input=input('请输入密码')

    for name,password in [line[:-1].split('|') for line in f.readlines()]:
        if name==name_input:
            if password==password_input:
                    print('登陆成功')
                    break
            else:
                    print('密码错误')
                    break
    else:
            print('账户新建成功')
            f.write(f'{name_input}|{password_input}\n')

