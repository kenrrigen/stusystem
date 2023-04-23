# encoding=GBK
# 开发时间：2023/4/16 13:26
# 开发人 K a r r i g a n
import os

filename = 'student.txt'


def main():
    while True:
        menu()
        try:
            choice = int(input('请选择'))
        except:
            print('清输入0-7的数字')
            continue

        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or 'Y':
                    print('谢谢您的使用')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息函数
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort()  # 排序
            elif choice == 6:
                total()  # 统计学生总人数
            elif choice == 7:
                show()  # 显示所有学生信息
        else:
            print('清输入0-7的数字')


def menu():
    print('===================学生信息管理系统==========================')
    print('-----------------------功能菜单----------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出系统')
    print('----------------------------------------------------------')


def insert():
    stu_list = []
    while True:
        id = input('请输入学生的ID：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break

        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，请输入整数成绩')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        stu_list.append(student)
        answer = input('是否继续添加？y/n')
        if answer == 'y':
            continue
        else:
            break

    save(stu_list)
    print('学生信息录入完毕！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='GBK')
    except:
        stu_txt = open(filename, 'w', encoding='GBK')
    for i in lst:
        stu_txt.write(str(i) + '\n')
    stu_txt.close()


def search():#获取学生信息并写入列表
    stu_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            try:
                mode = int(input('请选择查找方式：1.ID；2.姓名'))
            except:
                print('请选择1或者2!')
                continue
            if mode == 1:
                id=input('请输入学生的ID：')
            elif mode == 2:
                name=input('请输入学生的姓名:')
            else:
                print('请选择1或者2!')
                search()
            with open(filename,'r',encoding='GBK') as rfile:
                student=rfile.readlines()
                for i in student:
                    d=dict(eval(i))
                    if id!='':
                        if d['id']==id:
                            stu_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            stu_query.append(d)
            #显示查询结果
            show_student(stu_query)\
            #情况列表
            stu_query.clear()
            answer=input('是否继续查询？y/n\n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('暂无学生信息！')
            return

def show_student(lst):#显示查询结果
    if len(lst)==0:
        print('没有查询到学生信息！')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^8}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容显示格式
    format_date='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^8}\t{:^8}'
    for i in lst:
        print(format_date.format(i.get('id'),
                                 i.get('name'),
                                 i.get('python'),
                                 i.get('english'),
                                 i.get('java'),
                                 int(i.get('english'))+int(i.get('python'))+int(i.get('java'))
                                 ))




def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if student_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='GBK') as file1:
                    student_oid = file1.readlines()
            else:
                student_oid = []
            flag = False  # 表示是否删除
            if student_oid:
                with open(filename, 'w', encoding='GBK') as wfile:
                    d = {}
                    for item in student_oid:
                        d = dict(eval(item))  # 将字符串转成字典 eval去掉双引号
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'ID为{student_id}的学生信息已经删除!')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删完之后显示所有学生信息
            answer = input('是否继续删除？y/n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('请输入ID!')
            continue


def modify():
    while True:
        stu_id=input('请输入要修改的学生ID：')
        if stu_id:
            if os.path.exists(filename):
                with open(filename,'r',encoding='GBK') as file1:
                    stu_oid=file1.readlines()
            else:
                stu_oid=[]
            flag=False
            if stu_oid:
                with open(filename,'w',encoding='GBK') as wfile:
                    d = {}
                    for item in stu_oid:
                        d=dict(eval(item))
                        if d['id']==stu_id:
                            print('已找到学生信息，可以修改')
                            while True:
                                try:
                                    d['name']=input('请输入新姓名:')
                                    if not d['name']:
                                        print('不能为空！')
                                        continue
                                    d['english']=int(input('请输入新的英语成绩：'))
                                    d['python'] = int(input('请输入新的python成绩：'))
                                    d['java'] = int(input('请输入新的java成绩：'))
                                    break
                                except:
                                    print('输入有误，请重新输入')
                            wfile.write(str(d)+'\n')
                            print('修改成功！')
                            flag=True
                        else:
                            wfile.write(item)
                    if not flag:
                        print(f'没有找到ID为{stu_id}的学生信息')
            else:
                print('无学生信息！')
                break
            show()
            answer=input('是否继续修改学生信息？y/n')
            if answer=='y':
                modify()
            else:
                break
        else:
            print('请输入学生ID！')



def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='GBK') as rfile:
            stu_lst=rfile.readlines()
        stu_new=[]
        for i in stu_lst:
            stu_new.append(eval(i))
        asc_or_desc=input('请选择0.升序；1.降序')
        if asc_or_desc=='0':
            asc_or_desc_bool=False
        elif asc_or_desc=='1':
            asc_or_desc_bool=True
        else:
            print('您的输入有误，请重新输入！')
            sort()
        mode=input('请选择排序方式：1.英语成绩；2.Python成绩；3.Java成绩；0.总成绩')
        if mode=='1':
            stu_new.sort(key=lambda stu_new:int(stu_new['english']),reverse=asc_or_desc_bool)#lambda函数读取字典中的特定数据
        elif mode=='2':
            stu_new.sort(key=lambda stu_new:int(stu_new['python']),reverse=asc_or_desc_bool)
        elif mode=='3':
            stu_new.sort(key=lambda stu_new:int(stu_new['java']),reverse=asc_or_desc_bool)
        elif mode=='0':
            stu_new.sort(key=lambda stu_new:int(stu_new['english'])+int(stu_new['python'])+int(stu_new['java']),reverse=asc_or_desc_bool)
        else:
            print('您的输入有误，请重新输入！')
            sort()
        show_student(stu_new)

    else:
        print('暂无文件！')
        return


def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='GBK') as file1:
            students=file1.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有学生信息')
    else:
        print('暂未有文件保存！')


def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='GBK') as rfile:
            student=rfile.readlines()
            for item in student:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
            else:
                print('无学生信息！')

    else:
        print('文件不存在！')


if __name__ == '__main__':
    main()
#这是一个测试
