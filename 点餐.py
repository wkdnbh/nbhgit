#菜单
meau_list=[[1,'牛排',99],[2,'羊排',109],[3,'黑椒牛扒',189],[4,'回锅肉',89],[5,'大盘鸡',79],
           [6,'火腿炒饭',13],[7,'鸡肉炒饭',19],[8,'白米饭',5],[9,'五谷粥',10],[10,'寿司',18],
           [11,'鲜橙汁',8],[12,'牛奶',12],[13,'啤酒',6],[14,'红酒',69],[15,'白酒',49]
           ]

#购买的菜
de_list=[]

#会员
passkeylis=[['123','123'],['124','234'],['111','888'],['134','457'],['135','789']]
zhanghao=['123','124','111','134','135']

#餐桌号
desk=''

#会员注册
def zhuce():
    print('欢迎光临本店!!!')
    while True:
        password=input('请输入会员账号')
        key1=input('请输入密码')
        key2=input("请确认密码")
        if key1==key2 and password not in zhanghao:
            passkey = [password, key1]
            passkeylis.append(passkey)
            zhanghao.append(password)
            print('注册成功!!')
            print('返回首页')
            break
        elif key1==key2 and password  in zhanghao:
            passkey = [password, key1]
            passkeylis.append(passkey)
            zhanghao.append(password)
            print('该账号已存在,请重新注册!!!')
            continue
        else:
            print('两次密码不一致，请重新注册！！')
            continue
        #if key1==key2 :
        #    passkey=[password,key1]
        #    passkeylis.append(passkey)
        #    print('注册成功!!')
        #    print('返回首页')
        #    break
        #else:
        #    print('两次密码不一致，请重新注册！！')
        #    continue

#选择餐桌
def canzhuo():
    print('欢迎光临本餐厅！！！')
    print('尊敬的客人，请选座！！！')
    print("\tX-X\tX-X\tX-X\tX-X\t")
    print("\t|A|\t|B|\t|c|\t|D|\t")
    print("\tX-X\tX-X\tX-X\tX-X\t")
    print()
    print("\tX-X\tX-X\tX-X\tX-X\t")
    print("\t|E|\t|F|\t|G|\t|H|\t")
    print("\tX-X\tX-X\tX-X\tX-X\t")
    print()
    print("\tX-X\tX-X\tX-X\tX-X\t")
    print("\t|I|\t|J|\t|K|\t|L|\t")
    print("\tX-X\tX-X\tX-X\tX-X\t")

#给出菜单
def meau():
    print('编号    \t菜名     \t价格')
    for q in meau_list:
        print(f'{q[0]}    \t{q[1]}     \t{q[2]}')

#输出买的菜
def show():
    if len(de_list)==0:
        print('这没有您喜欢的菜吗？T_T.')
    else:
        print('您点的菜如下:')
        for i in de_list:
            for j in meau_list:
                if i[0]==j[0]:
                    print(j[1]+'x'+str(i[1]))

#点餐
def diancan():
    while True:
        meau()
        while True:
            s=int(input('请输入您要点的餐品数字编号：'))
            if 1<=s<=15:
                break
            else:
                print('请输入正确的餐品编号！！！')
                continue
        while True:
            n = int(input('请输入您要买的数量：'))
            if 1<=n:
                break
            else:
                print('输入错误，请重新输入！！！')
                continue
        a=[s,n]
        de_list.append(a)
        print('是否继续点购？(yes/no)')
        k=input()
        if k=='yes':
            continue
        elif k=='no':
            show()
            break
        else:
            print('输入有误，请您确认点购餐品后重新输入')
            show()
            break

#vip积分
def vip(total):
    a=0
    x=0
    print('您是否为本店会员？(yes/no)')
    while True:
        k = input ()
        if k== "yes" :
            print('您可为您的账户累计消费积分（1元=1分）')
            print('请登录您的账户!!!')
            while True:
                password = input('请输入会员账号:')
                key = input('请输入密码:')
                #'''for i in passkeylis:
                #    if i[0] == password and i[1] == key:
                #       print('恭喜您登录成功!')
                #        print(f'已成功累计消费积分：{total}（1元=1分)')
                #        a=1
                #        break
                #else:
                #    print('密码不正确，请重新输入!!!')'''
                if password not in zhanghao:
                    print('没有此账号，很遗憾本次积分作废!!!')
                else:
                    for i in passkeylis:
                        if i[0] == password and i[1] == key:
                            print('恭喜您登录成功!')
                            print(f'已成功累计消费积分：{total}（1元=1分)')
                            a = 1
                            break
                    else:
                        print('密码不正确，请确认密码是否有误!!!')
                if a==1:
                    break
                print('是否继续登录？(yes/no)')
                kk=input()
                while True:
                    if kk == 'yes':
                        break
                    elif kk == 'no':
                        x=1
                        break
                    else:
                        print('输入有误，请重新输入！！！')
                        continue
                if x==1:
                    break
            if a==1 :
                break
            elif x==1:
                print('很遗憾您放弃积分机会 T_T')
                break



            #    '''for i in passkeylis:
            #        if i[0]==password:
            #            if i[1]==key:
            #                print('恭喜您登录成功!')
            #                print(f'已成功累计消费积分：{total}（1元=1分)')
            #                break
            #            else:
            #                print('密码不正确，请重新输入!!!')
            #        else :
            #            print('没有此账号，很遗憾本次  '
            #                  '---------------------------+积分作废!!!')
            #            break
            #    break
            #break'''
        elif k=='no':
            print('很遗憾你不能获得积分，无法享受更多优惠，建议您下次加入我们会员大家庭享受更多权益!!!')
            break

#购物评分
def pingjia():
    print('请为您本次用餐体验打分:')
    print('非常满意:A')
    print('满意:B')
    print('不满意:C')
    print('很不满意:D')
    while True:
        x=input()
        if x=='A':
            print('感谢您的支持，祝您生活愉快！！！')
            break
        elif x=='B':
            print('感谢您的评价，我们将做得更好，祝您生活愉快！！！')
            break
        elif x=='C':
            print('抱歉让您就餐不满意，我们将深刻反思，祝您生活愉快！！！')
            break
        elif x=='D':
            print('我们深感抱歉，请您到前台反应您的不愉快，我们将为您提供一对一处理，祝您生活愉快！！！')
            break
        else:
            print('输入有误，请你们你重新输入')
            

#结算
def jiesuan():
    print('餐品名   单价 数量 总价')
    total=0
    for i in de_list:
        for j in meau_list:
            if i[0] in j:
                print(f'{j[1]} \t{j[2]} \t{i[1]} \t{j[2]*i[1]}')
                total+=j[2]*i[1]
    print('共计消费：{}元'.format(total))
    vip(total)
    pingjia()
    de_list.clear()

#本店聚餐结算
def jiucan_1():
    global desk
    canzhuo()
    while True:
        kk = input('请输入餐桌号：').upper()
        if 'A'<=kk<='L':
            desk = kk
            print(f'您成功选座{desk}桌')
            break
        else:
            print('本店没有该桌,请您确认后重新选择!!!')
            continue
    #kk = input('请输入餐桌号：').upper()
    #desk = kk
    while True:
        diancan()
        print('是否继续选购？(yes/no)')
        k=input()
        if k=='yes':
            continue
        elif k=='no':
            break
    print('柜台结账:')
    print(desk+'桌结算如下:')
    jiesuan()
    print()
    print('欢迎下次光临！！！')

#回家结算
def jiucan_2():
    while True:
        diancan()
        print('是否继续选购？(yes/no)')
        k = input()
        if k == 'yes':
            continue
        elif k == 'no':
            break
    print('柜台结账:')
    print('您的结算信息如下:')
    jiesuan()
    print()
    print('欢迎下次光临！！！')

#就餐场地选择
def jiucan():
    print('欢迎光临！！！')
    print('请问您在店就餐或者带走？')
    print('1.在店就餐')
    print('2.带走')
    while True:
        k=input('按序号选择:')
        if k=='1':
            jiucan_1()
            break
        elif k=='2':
            jiucan_2()
            break
        else:
            print('输入错误，请重新输入')
    input('按任意键退回...')

#主函数
def main():
    while True:
        print('欢迎光临！！！')
        print('1.会员注册！！！')
        print('2.就餐')
        print('3.离开')
        k=input('请选择操作......')
        if k=='1':
            zhuce()
        elif k=='2':
            jiucan()
        elif k=='3':
            break
        else:
            print('输入错误，请重新输入!!!')

main()











