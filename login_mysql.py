import pymysql

door = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'door', password= '123456',db='USER')
sqli="insert into user values(%s,%s)"

with door.cursor() as cursor:
        try:
                cursor.execute("create table user(name varchar(20),password varchar(20))")
        except :
                pass
        cursor.execute("select * from user")
        data=cursor.fetchall()
        name_input=input('请输入用户名')
        password_input=input('请输入密码')
        
        for name,password in data:
                if name==name_input:
                        if password==password_input:
                                print('登陆成功')
                                break
                        else:
                                print('密码错误')
                                break
        else:
                print('账户新建成功')
                cursor.execute(sqli,(name_input,password_input))
        
door.commit()
door.close()