import os
import json

mode='r+' if os.path.exists('user.txt') else 'w+'

with open('user.txt',mode) as f:
    name_input=input('请输入用户名')
    password_input=input('请输入密码')
    try:
        data=json.load(f)
    except:
        data={'info':{}}
    for name,password in data['info'].items():
        if name==name_input:
            if password==password_input:
                    print('登陆成功')
                    break
            else:
                    print('密码错误')
                    break
    else:
            print('账户新建成功')
            data['info'][name_input]=password_input
            with open('user.txt','w+') as f:
                json.dump(data,f)