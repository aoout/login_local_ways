import numpy as np
import pandas as pd

name_input=input('请输入用户名')
password_input=input('请输入密码')

try:
    data=pd.read_csv('user.csv',index_col=0)
except:
    data=pd.DataFrame(columns=['name','password'])

for name,password in zip(data['name'].values,data['password'].values):
    if name==name_input:
        if password==password_input:
                print('登陆成功')
                break
        else:
                print('密码错误')
                break
else:
        print('账户新建成功')
        data = data.append([{'name':name_input,'password':password_input}], ignore_index=True)
        data.to_csv('user.csv')