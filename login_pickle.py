import pickle
import os

mode='rb+' if os.path.exists('user.data') else 'wb+'

with open('user.data',mode) as f:
    name_input=input('请输入用户名')
    password_input=input('请输入密码')
    try:
        data=pickle.load(f)
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
            with open('user.data','wb+') as f:
                pickle.dump(data,f)