# encoding=GBK
# ����ʱ�䣺2023/4/16 13:26
# ������ K a r r i g a n
import os

filename = 'student.txt'


def main():
    while True:
        menu()
        try:
            choice = int(input('��ѡ��'))
        except:
            print('������0-7������')
            continue

        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('��ȷ��Ҫ�˳�ϵͳ��y/n')
                if answer == 'y' or 'Y':
                    print('лл����ʹ��')
                    break  # �˳�ϵͳ
                else:
                    continue
            elif choice == 1:
                insert()  # ¼��ѧ����Ϣ����
            elif choice == 2:
                search()  # ����ѧ����Ϣ
            elif choice == 3:
                delete()  # ɾ��ѧ����Ϣ
            elif choice == 4:
                modify()  # �޸�ѧ����Ϣ
            elif choice == 5:
                sort()  # ����
            elif choice == 6:
                total()  # ͳ��ѧ��������
            elif choice == 7:
                show()  # ��ʾ����ѧ����Ϣ
        else:
            print('������0-7������')


def menu():
    print('===================ѧ����Ϣ����ϵͳ==========================')
    print('-----------------------���ܲ˵�----------------------------')
    print('\t\t\t\t\t1.¼��ѧ����Ϣ')
    print('\t\t\t\t\t2.����ѧ����Ϣ')
    print('\t\t\t\t\t3.ɾ��ѧ����Ϣ')
    print('\t\t\t\t\t4.�޸�ѧ����Ϣ')
    print('\t\t\t\t\t5.����')
    print('\t\t\t\t\t6.ͳ��ѧ��������')
    print('\t\t\t\t\t7.��ʾ����ѧ����Ϣ')
    print('\t\t\t\t\t0.�˳�ϵͳ')
    print('----------------------------------------------------------')


def insert():
    stu_list = []
    while True:
        id = input('������ѧ����ID��')
        if not id:
            break
        name = input('������������')
        if not name:
            break

        try:
            english = int(input('������Ӣ��ɼ���'))
            python = int(input('������Python�ɼ���'))
            java = int(input('������Java�ɼ���'))
        except:
            print('������Ч�������������ɼ�')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        stu_list.append(student)
        answer = input('�Ƿ������ӣ�y/n')
        if answer == 'y':
            continue
        else:
            break

    save(stu_list)
    print('ѧ����Ϣ¼����ϣ�')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='GBK')
    except:
        stu_txt = open(filename, 'w', encoding='GBK')
    for i in lst:
        stu_txt.write(str(i) + '\n')
    stu_txt.close()


def search():#��ȡѧ����Ϣ��д���б�
    stu_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            try:
                mode = int(input('��ѡ����ҷ�ʽ��1.ID��2.����'))
            except:
                print('��ѡ��1����2!')
                continue
            if mode == 1:
                id=input('������ѧ����ID��')
            elif mode == 2:
                name=input('������ѧ��������:')
            else:
                print('��ѡ��1����2!')
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
            #��ʾ��ѯ���
            show_student(stu_query)\
            #����б�
            stu_query.clear()
            answer=input('�Ƿ������ѯ��y/n\n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('����ѧ����Ϣ��')
            return

def show_student(lst):#��ʾ��ѯ���
    if len(lst)==0:
        print('û�в�ѯ��ѧ����Ϣ��')
        return
    #���������ʾ��ʽ
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^8}\t{:^8}'
    print(format_title.format('ID','����','Ӣ��ɼ�','Python�ɼ�','Java�ɼ�','�ܳɼ�'))
    #����������ʾ��ʽ
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
        student_id = input('������Ҫɾ����ѧ����ID��')
        if student_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='GBK') as file1:
                    student_oid = file1.readlines()
            else:
                student_oid = []
            flag = False  # ��ʾ�Ƿ�ɾ��
            if student_oid:
                with open(filename, 'w', encoding='GBK') as wfile:
                    d = {}
                    for item in student_oid:
                        d = dict(eval(item))  # ���ַ���ת���ֵ� evalȥ��˫����
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'IDΪ{student_id}��ѧ����Ϣ�Ѿ�ɾ��!')
                    else:
                        print(f'û���ҵ�IDΪ{student_id}��ѧ����Ϣ')
            else:
                print('��ѧ����Ϣ')
                break
            show()  # ɾ��֮����ʾ����ѧ����Ϣ
            answer = input('�Ƿ����ɾ����y/n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('������ID!')
            continue


def modify():
    while True:
        stu_id=input('������Ҫ�޸ĵ�ѧ��ID��')
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
                            print('���ҵ�ѧ����Ϣ�������޸�')
                            while True:
                                try:
                                    d['name']=input('������������:')
                                    if not d['name']:
                                        print('����Ϊ�գ�')
                                        continue
                                    d['english']=int(input('�������µ�Ӣ��ɼ���'))
                                    d['python'] = int(input('�������µ�python�ɼ���'))
                                    d['java'] = int(input('�������µ�java�ɼ���'))
                                    break
                                except:
                                    print('������������������')
                            wfile.write(str(d)+'\n')
                            print('�޸ĳɹ���')
                            flag=True
                        else:
                            wfile.write(item)
                    if not flag:
                        print(f'û���ҵ�IDΪ{stu_id}��ѧ����Ϣ')
            else:
                print('��ѧ����Ϣ��')
                break
            show()
            answer=input('�Ƿ�����޸�ѧ����Ϣ��y/n')
            if answer=='y':
                modify()
            else:
                break
        else:
            print('������ѧ��ID��')



def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='GBK') as rfile:
            stu_lst=rfile.readlines()
        stu_new=[]
        for i in stu_lst:
            stu_new.append(eval(i))
        asc_or_desc=input('��ѡ��0.����1.����')
        if asc_or_desc=='0':
            asc_or_desc_bool=False
        elif asc_or_desc=='1':
            asc_or_desc_bool=True
        else:
            print('���������������������룡')
            sort()
        mode=input('��ѡ������ʽ��1.Ӣ��ɼ���2.Python�ɼ���3.Java�ɼ���0.�ܳɼ�')
        if mode=='1':
            stu_new.sort(key=lambda stu_new:int(stu_new['english']),reverse=asc_or_desc_bool)#lambda������ȡ�ֵ��е��ض�����
        elif mode=='2':
            stu_new.sort(key=lambda stu_new:int(stu_new['python']),reverse=asc_or_desc_bool)
        elif mode=='3':
            stu_new.sort(key=lambda stu_new:int(stu_new['java']),reverse=asc_or_desc_bool)
        elif mode=='0':
            stu_new.sort(key=lambda stu_new:int(stu_new['english'])+int(stu_new['python'])+int(stu_new['java']),reverse=asc_or_desc_bool)
        else:
            print('���������������������룡')
            sort()
        show_student(stu_new)

    else:
        print('�����ļ���')
        return


def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='GBK') as file1:
            students=file1.readlines()
            if students:
                print(f'һ����{len(students)}��ѧ��')
            else:
                print('��û��ѧ����Ϣ')
    else:
        print('��δ���ļ����棡')


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
                print('��ѧ����Ϣ��')

    else:
        print('�ļ������ڣ�')


if __name__ == '__main__':
    main()
