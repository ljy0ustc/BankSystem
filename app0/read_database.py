from pymysql import connect

def select_client(name,id):
    try:
        conn = connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123',
            db='BANKSYS',
            charset='utf8'
        )
        cur=conn.cursor()
        name_str='%'+name+'%'
        id_str='%'+id+'%'
        if not cur:
            return "error!"
        sql='select client_id,client_name,client_phone,client_address from Client where client_name like %s and client_id like %s;'
        data=[(name_str,id_str)]
        cur.executemany(sql,data)


        ret = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        print(list(ret))
        return list(ret)

    except Exception as e:
        print(e)
        return "error!"

def insert_client(client_id,client_name,client_tel,client_add,contact_name,contact_tel,contact_email,contact_rel):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        sql1='insert into Client (client_id,client_name,client_phone,client_address) Values (%s,%s,%s,%s)'
        data1=[(client_id,client_name,client_tel,client_add)]
        cur.executemany(sql1,data1)

        sql2='insert into Contacts (client_id,contact_name,contact_phone,contact_email,contact_rel) Values (%s,%s,%s,%s,%s)'
        data2=[(client_id,contact_name,contact_tel,contact_email,contact_rel)]
        cur.executemany(sql2,data2)

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(e)
        return "error!"
    
def search_detail_client(client_id):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        sql1='select Client.client_id,Client.client_name,Client.client_phone,Client.client_address from Client where client_id = %s;'
        sql2='select Contacts.contact_name,Contacts.contact_phone,Contacts.contact_email,Contacts.contact_rel from Contacts where client_id = %s;'
        data=[(client_id)]
        cur.executemany(sql1,data)
        ret1 = cur.fetchone()
        cur.executemany(sql2,data)
        ret2 = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        print(list(ret1)+list(ret2))
        return list(ret1)+list(ret2)

    except Exception as e:
        print(e)
        return "error!"

def delete_client(client_id):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        #TODO:处理外键？
        sql1='select account_number from ClientOpenChequeAccount where client_id = %s;'
        sql2='select account_number from ClientOpenSavingAccount where client_id = %s;'
        sql3='select loan_id from loan_to_client where client_id = %s;'
        sql4='delete from Client where client_id = %s;'
        sql5='delete from Contacts where client_id = %s;'
        sql6='delete from Responsibility where client_id = %s;'
        data=[(client_id)]

        cur.executemany(sql1,data)
        ret1 = cur.fetchall()
        cur.executemany(sql2,data)
        ret2 = cur.fetchall()
        cur.executemany(sql3,data)
        ret3 = cur.fetchall()
        if len(list(ret1)+list(ret2)+list(ret3))>0:
            return "error!"


        cur.executemany(sql5,data)
        cur.executemany(sql6,data)
        cur.executemany(sql4,data)

        print("delete"+str(client_id))

        conn.commit()
        cur.close()
        conn.close()

        return "success"

    except Exception as e:
        print(e)
        return "error!"

def edit_client(originalID,client_id,client_name,client_tel,client_add,contact_name,contact_tel,contact_email,contact_rel):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        #TODO:处理外键？
        sql1='select account_number from ClientOpenChequeAccount where client_id = %s;'
        sql2='select account_number from ClientOpenSavingAccount where client_id = %s;'
        sql3='select loan_id from loan_to_client where client_id = %s;'
        sql4='Update Client Set client_id = %s,client_name = %s,client_phone = %s,client_address = %s where client_id = %s;'
        sql5='Update Contacts Set client_id = %s,contact_name=%s,contact_phone = %s,contact_email = %s,contact_rel = %s where client_id = %s;'
        sql6='Update Responsibility Set client_id = %s where client_id = %s;'
        sql_close='SET FOREIGN_KEY_CHECKS=0;'
        sql_open='SET FOREIGN_KEY_CHECKS=1;'

        data=[(originalID)]
        data4=[(client_id,client_name,client_tel,client_add,originalID)]
        data5=[(client_id,contact_name,contact_tel,contact_email,contact_rel,originalID)]
        data6=[(client_id,originalID)]

        cur.executemany(sql1,data)
        ret1 = cur.fetchall()
        cur.executemany(sql2,data)
        ret2 = cur.fetchall()
        cur.executemany(sql3,data)
        ret3 = cur.fetchall()
        if len(list(ret1)+list(ret2)+list(ret3))>0:
            return "error!"

        cur.execute(sql_close)
        cur.executemany(sql4,data4)
        cur.executemany(sql5,data5)
        cur.executemany(sql6,data6)
        cur.execute(sql_open)

        print("update"+str(client_id))

        conn.commit()
        cur.close()
        conn.close()

        return "success"

    except Exception as e:
        print(e)
        return "error!"

def select_account(account_num):
    try:
        conn = connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123',
            db='BANKSYS',
            charset='utf8'
        )
        cur=conn.cursor()
        account_number='%'+account_num+'%'
        if not cur:
            return "error!"
        sql='select account_number,branch_name,account_balance,account_date from Account where account_number like %s;'
        data=[(account_number)]
        cur.executemany(sql,data)

        ret = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        print(list(ret))
        return list(ret)

    except Exception as e:
        print(e)
        return "error!"

def delete_account(account_number):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        sql1='delete from ClientOpenChequeAccount where account_number = %s;'
        sql2='delete from ClientOpenSavingAccount where account_number = %s;'
        sql3='delete from SavingAccount where account_number = %s;'
        sql4='delete from ChequeAccount where account_number = %s;'
        sql5='delete from Account where account_number = %s;'
        data=[(account_number)]

        cur.executemany(sql1,data)
        cur.executemany(sql2,data)
        cur.executemany(sql3,data)
        cur.executemany(sql4,data)
        cur.executemany(sql5,data)

        print("delete"+str(account_number))

        conn.commit()
        cur.close()
        conn.close()

        return "success!"

    except Exception as e:
        print(e)
        return "error!"

def insert_cheque_account(account_number,branch_name,account_balance,overdraft,client_id):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        sql1='insert into Account (account_number,branch_name,account_balance,account_date) Values (%s,%s,%s,CURDATE())'
        data1=[(account_number,branch_name,account_balance)]
        cur.executemany(sql1,data1)

        sql2='insert into ChequeAccount (account_number,overdraft) Values (%s,%s)'
        data2=[(account_number,overdraft)]
        cur.executemany(sql2,data2)

        sql3='insert into ClientOpenChequeAccount (account_number,client_id,last_visit_cheque_account) Values (%s,%s,CURDATE())'
        data3=[(account_number,client_id)]
        cur.executemany(sql3,data3)

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(e)
        return "error!"

def insert_saving_account(account_number,branch_name,account_balance,interest_rate,currency_type,client_id):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        #TODO:
        sql1='insert into Account (account_number,branch_name,account_balance,account_date) Values (%s,%s,%s,CURDATE())'
        data1=[(account_number,branch_name,account_balance)]
        cur.executemany(sql1,data1)

        sql2='insert into SavingAccount (account_number,interest_rate,currency_type) Values (%s,%s,%s)'
        data2=[(account_number,interest_rate,currency_type)]
        cur.executemany(sql2,data2)

        sql3='insert into ClientOpenSavingAccount (account_number,client_id,last_visit_saving_account) Values (%s,%s,CURDATE())'
        data3=[(account_number,client_id)]
        cur.executemany(sql3,data3)

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(e)
        return "error!"

def search_detail_account(account_number):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        #TODO:
        sql1='select account_number,branch_name,account_balance,account_date from Account where account_number = %s;'
        sql2='select interest_rate,currency_type from SavingAccount where account_number = %s;'
        sql3='select overdraft from ChequeAccount where account_number = %s;'
        data=[(account_number)]
        cur.executemany(sql1,data)
        ret1 = cur.fetchone()
        cur.executemany(sql2,data)
        ret2 = cur.fetchone()
        cur.executemany(sql3,data)
        ret3 = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        if ret2 is None:
            return list(ret1)+list(ret3)
        else:
            return list(ret1)+list(ret2)

    except Exception as e:
        print(e)
        return "error!"

def select_loan(loan_id):
    try:
        conn = connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123',
            db='BANKSYS',
            charset='utf8'
        )
        cur=conn.cursor()
        if not cur:
            return "error!"
        sql='select Loan.loan_id,Loan.branch_name,Loan.loan_money,Loan.pay_cnt,Pay.pay_money from Loan,Pay where Loan.loan_id = %s and Pay.loan_id = %s;'
        data=[(loan_id,loan_id)]
        cur.executemany(sql,data)
        res = cur.fetchall()

        res=list(res)
        print("res",res)

        ret=[]
        if len(res)>0:
            paid_money=0
            for item in res:
                paid_money+=item[4]
            print("paid_money:",paid_money)
            state=""
            if paid_money==0:
                state="unpaid"
            else:
                if res[0][2]>paid_money:
                    state="paying"
                else:
                    state="paid"
            print("state:",state) 
            ret=list(res[0])[0:4]
            ret.append(state)    
            print("ret:",ret)  
        else:
            sql='select loan_id,branch_name,loan_money,pay_cnt from Loan where loan_id = %s;'
            data=[(loan_id)]
            cur.executemany(sql,data)
            res = cur.fetchone()
            res=list(res)
            print("res",res)
            if len(res)>0:
                ret=res
                ret.append("unpaid")
                print("ret:",ret)

        conn.commit()
        cur.close()
        conn.close()
        print(ret)
        return ret

    except Exception as e:
        print(e)

def delete_loan(loan_id):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"

    #TODO:只有unpaid贷款才能删
    sql1='delete from loan_to_client where loan_id = %s;'
    sql3='delete from Pay where loan_id = %s;'
    sql2='delete from Loan where loan_id = %s;'
    data=[(loan_id)]

    try:
        cur.executemany(sql1,data)
        cur.executemany(sql2,data)
        cur.executemany(sql3,data)

        print("delete"+str(loan_id))

        conn.commit()
        cur.close()
        conn.close()

        return "success!"

    except Exception as e:
        print(e)
        return "error!"

def insert_loan(loan_id,branch_name,loan_money,pay_cnt,client_id):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        sql1='insert into Loan (loan_id,branch_name,loan_money,pay_cnt) Values (%s,%s,%s,%s)'
        data1=[(loan_id,branch_name,loan_money,pay_cnt)]
        cur.executemany(sql1,data1)

        sql2='insert into loan_to_client (client_id,loan_id) Values (%s,%s)'
        data2=[(client_id,loan_id)]
        cur.executemany(sql2,data2)

        conn.commit()
        cur.close()
        conn.close()

        return "success!"

    except Exception as e:
        print(e)
        return "error!"

def insert_pay(pay_id,loan_id,pay_money):
    conn = connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='BANKSYS',
        charset='utf8'
    )
    cur=conn.cursor()
    if not cur:
        return "error!"
    try:
        #TODO:??????????解决贷款发放次数和金额的限制问题

        print("begin try")

        sql='select Loan.loan_id,Loan.branch_name,Loan.loan_money,Loan.pay_cnt,Pay.pay_money from Loan,Pay where Loan.loan_id = %s and Pay.loan_id = %s;'
        data=[(loan_id,loan_id)]
        cur.executemany(sql,data)
        loan_condition = cur.fetchall()
        loan_condition=list(loan_condition)

        print("select loan and pay")

        if len(loan_condition)>0:
            sum=float(pay_money)
            for item in loan_condition:
                sum+=float(item[4])
            print("sum",sum)
            if float(pay_money)>float(loan_condition[0][2]):
                print("1*************")
                return "error!"
            if len(loan_condition)+1>loan_condition[0][3]:
                print("2*************")
                return "error!"
        else:
            sql='select loan_id,branch_name,loan_money,pay_cnt from Loan where Loan.loan_id = %s;'
            data=[(loan_id)]
            cur.executemany(sql,data)
            loan_condition = cur.fetchall()
            loan_condition=list(loan_condition)

            print("select loan")

            if len(loan_condition)==0:
                print("3*************")
                return "error!"

        print("insert pay")
        sql='insert into Pay (pay_id,loan_id,pay_date,pay_money) Values (%s,%s,CURDATE(),%s)'
        data=[(pay_id,loan_id,pay_money)]
        cur.executemany(sql,data)

        conn.commit()
        cur.close()
        conn.close()

        return "success!"

    except Exception as e:
        print(e)
        print("4**********")
        return "error!"

if __name__ == '__main__':
    search_detail_client("510105200101010000")
    edit_client('510105200101010000','510105200101010000','Joy','18900000000','chengdu','Jennie','18900000010','jennie@gmail.com','friend')
