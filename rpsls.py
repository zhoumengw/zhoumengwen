#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2019��11��20��
"""

import random
answer=random.randint(0,4)



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	if name=="ʯͷ":
		a=0
	elif name=="ʷ����":
		a=1
	elif name=="ֽ":
		a=2
	elif name=="����":
		a=3
	elif name=="����":
		a=4
	else:
		a=5
   
	return a
    #����Ϸ�����Ӧ����ͬ������

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
	if number==0:
		b="ʯͷ"
	if number==1:
		b="ʷ����"
	if number==2:
		b="ֽ"
	if number==3:
		b="����"
	if number==4:
		b="����"
	return b
    #������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
	player_choice_number=name_to_number(player_choice)
	comp_number=answer
	comp_choice=number_to_name(comp_number)
	print("--------")
	if player_choice_number!=5:
		print("����ѡ��Ϊ:%s"%player_choice)
		print("�������ѡ��Ϊ:%s"%comp_choice)
		if player_choice_number==comp_number:
			print("���ͼ��������һ���ء�")
		elif player_choice_number!=comp_number:
			if player_choice_number==0:
				if comp_number==3 or 4:
					print("��Ӯ��")
				else:
					print("�����Ӯ��")
			elif player_choice_number==1:
			    if comp_number==0 or 4:
				    print("��Ӯ��")
			    else:
				    print("�����Ӯ��")
			elif player_choice_number==2:
				if comp_number==0 or 1:
					print("��Ӯ��")
				else:
					print("�����Ӯ��")
			elif player_choice_number==3:
				if comp_number==1 or 2:
					print("��Ӯ��")
				else:
					print("�����Ӯ��")
			elif player_choice_number==4:
				if comp_number==2 or 3:
					print("��Ӯ��")
				else:
					print("�����Ӯ��")
	elif player_choice_number==5:
		print("Error: No Correct Name.")

	return
				
					
    #�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


