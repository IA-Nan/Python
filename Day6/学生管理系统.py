def print_info():
 print('-' * 20)
 print('欢迎登录学员管理系统')
 print('1: 添加学员')
 print('2: 删除学员')
 print('3: 修改学员信息')
 print('4: 查询学员信息')
 print('5: 显示所有学员信息')
 print('6: 退出系统')
 print('-' * 20)
info = []
def add_info():
    """添加学员"""
    new_id = (input('学号:'))
    new_name = (input('姓名:'))
    new_tel = (input('电话:'))
    global info
    if info.count('new_name'):
        print('姓名存在!')        
        return
    else:
        info_dict = {}
        info_dict['id'] = new_id
        info_dict['name'] = new_name
        info_dict['tel'] = new_tel        
        info.append(info_dict)
        print(info)
        print('添加成功')
        
    

print_info()
user_num = input('请输入功能序号:')
if user_num == '1':
    print('添加学员')
    add_info()
elif user_num == '2':
    print('删除学员')
elif user_num == '3':
    print('修改学员信息')
elif user_num == '4':
    print('查询学员信息')
elif user_num == '5':
    print('显示所有学员信息')
elif user_num == '6':
    print('退出系统')
else:
 print('输⼊错误，请重新输⼊!!!')




