def print_info ():
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


def add_info ():
    """添加学员函数"""
    new_id = (input('学号:'))
    new_name = (input('姓名:'))
    new_tel = (input('电话:'))
    global info
    for i in info:
        if new_name == i['name']:
            print('姓名存在, 添加失败!')
            return
    else:
        info_dict = {}
        info_dict['id'] = new_id
        info_dict['name'] = new_name
        info_dict['tel'] = new_tel
        info.append(info_dict)
        # print(info)
        print('添加成功')
def del_info():
    """删除学员"""
    del_name = input('请输入要删除的姓名:')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            print('成功')
        else:
            print('姓名不存在删除失败')
    # info.remove(del_name)
def revise_info():
    """修改学员信息"""
    revise_name = input('请输入要修改的学员姓名')
    global info
    for i in info:
        if revise_name == i['name']:
            print(i)
            new_id = input('请输入修改的学号')
            new_name = input('请输入修改的姓名')
            new_tel = input('请输入修改的电话')
            i['id'] = new_id
            i['name'] = new_name
            i['tel'] = new_tel
            print(i)
        else:
            print('姓名不存在')

def find_info():
    """按姓名查询"""
    find_name = input('请输入查询学生的姓名:')
    global info
    for i in info:
        if find_name == i['name']:
            print(f'''学号:{i['id']}\t姓名:{i['name']}\t电话:{i['tel']}''')
        else:
            print('姓名存在')
    
def find_all_info():
    print('学号\t姓名\t电话\t')
    global info
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")






while True:
    print_info()
    user_num = input('请输入功能序号:')
    if user_num == '1':
        # print('添加学员')
        add_info()
    elif user_num == '2':
        # print('删除学员')
        del_info()
    elif user_num == '3':
        # print('修改学员信息')
        revise_info()

    elif user_num == '4':
        # print('查询学员信息')
        find_info()

    elif user_num == '5':
        # print('显示所有学员信息')
        find_all_info()

    elif user_num == '6':
        print('退出系统')
        break
    else:
        print('输⼊错误，请重新输⼊!!!')





