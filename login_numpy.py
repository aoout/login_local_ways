import numpy as np

info=np.dtype({'names':['name','password'],'formats':['S32','S32']})

name_input=input('请输入用户名')
password_input=input('请输入密码')

try:
    data=np.load('user.npy')
except:
    data=np.array([],dtype=info)

for name,password in [[str(x)[2:-1] for x in i] for i in data]:
    if name==name_input:
        if password==password_input:
                print('登陆成功')
                break
        else:
                print('密码错误')
                break
else:
        print('账户新建成功')
        temp=np.array([(name_input,password_input)],dtype=info)
        data=np.append(data,temp)
        np.save('user.npy',data)