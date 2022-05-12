from django.http import HttpResponse
from django.shortcuts import redirect, render
from flask import render_template
from soupsieve import select
#from app0.read_database import select_client
from .read_database import select_client,insert_client,search_detail_client,delete_client,edit_client
from .read_database import select_account,delete_account,insert_cheque_account,insert_saving_account,search_detail_account
from .read_database import select_loan,delete_loan,insert_loan,insert_pay
import re


# Create your views here.

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        #TODO:
        hostname=request.POST.get("user")
        password=request.POST.get("pwd")
        if hostname=='root' and password=='123': 
            return redirect("/index")
        else:
            return render(request,'login.html',{"error_msg":"host name or password error!"})

def index(request):
    if request.method=="GET":
        return render(request,'index.html')
    else:
        client_click=request.POST.get("client_but")
        account_click=request.POST.get("account_but")
        loan_click=request.POST.get("loan_but")
        business_click=request.POST.get("business_but")
        if client_click is not None:
            return redirect("/index/client")
        if account_click is not None:
            print("account")
            return redirect("/index/account")
        if loan_click is not None:
            print("loan")
            return redirect("/index/loan")
        if business_click is not None:
            return redirect("/index/business")
        return render(request,'index.html')

def client(request):
    if request.method=='GET':
        client_name=request.GET.get("client_name")
        client_id=request.GET.get("client_id")
        client_list=select_client(client_name,client_id)
        return render(request,'client.html',{"client_list":client_list})
    else:
        new_val=request.POST.get("new_button")
        delete_val=request.POST.get("delete_button")
        if new_val is not None:
            return redirect("/index/client/new")
        if delete_val is not None:
            res=delete_client(delete_val)
            if res=='error!':
                return render(request,'client.html',{"error_msg":"host name or password error!"})
            else:
                return render(request,'client.html',{"error_msg":"deleted successfully!"})

def client_new(request):
    if request.method=="GET":
        return render(request,'client_new.html')
    else:
        client_name=request.POST.get("client_name")
        client_id=request.POST.get("client_id")
        client_tel=request.POST.get("client_tel")
        client_add=request.POST.get("client_add")
        contact_name=request.POST.get("contact_name")
        contact_tel=request.POST.get("contact_tel")
        contact_email=request.POST.get("contact_email")
        contact_rel=request.POST.get("contact_rel")
        if client_name is None or client_id is None or client_tel is None or client_add is None or contact_name is None or contact_tel is None or contact_email is None  or contact_rel is None:
            return render(request,'client_new.html',{"error_msg":"error information!"})
        if len(client_name)>10 or len(client_id)!=18 or len(client_tel)>15 or len(client_add)>30:
            return render(request,'client_new.html',{"error_msg":"error information!"})
        if len(contact_name)>20 or len(contact_tel)>15 or len(contact_email)>30 or len(contact_rel)>20:
            return render(request,'client_new.html',{"error_msg":"error information!"})
        email_pattern=r"[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.com"
        tel_pattern=r"[0-9]+"
        if re.match(email_pattern,contact_email) is None:
            return render(request,'client_new.html',{"error_msg":"error e-mail!"})
        if re.match(tel_pattern,contact_tel) is None or re.match(tel_pattern,client_tel) is None:
            return render(request,'client_new.html',{"error_msg":"error phone number!"})
        insert_client(client_id,client_name,client_tel,client_add,contact_name,contact_tel,contact_email,contact_rel)
        return redirect("/index/client")

def client_detail(request):
    detail_val=request.POST.get("detail_button")
    if detail_val is not None:
        client_info=search_detail_client(detail_val)
        return render(request,'client_detail.html',{"client_info":client_info})

def client_edit(request):
    if request.method=="GET":
        edit_val=request.GET.get("edit_button")
        print("edit_val",edit_val)
        if edit_val is not None:
            return render(request,'client_edit.html',{"originalID":edit_val})
    else:
        client_name=request.POST.get("client_name")
        client_id=request.POST.get("client_id")
        client_tel=request.POST.get("client_tel")
        client_add=request.POST.get("client_add")
        contact_name=request.POST.get("contact_name")
        contact_tel=request.POST.get("contact_tel")
        contact_email=request.POST.get("contact_email")
        contact_rel=request.POST.get("contact_rel")
        originalID=request.POST.get("originalID")
        print('originalID',originalID)
        if client_name is None or client_id is None or client_tel is None or client_add is None or contact_name is None or contact_tel is None or contact_email is None  or contact_rel is None:
            return render(request,'client_new.html',{"error_msg":"error information!"})
        if len(client_name)>10 or len(client_id)!=18 or len(client_tel)>15 or len(client_add)>30:
            return render(request,'client_new.html',{"error_msg":"error information!"})
        if len(contact_name)>20 or len(contact_tel)>15 or len(contact_email)>30 or len(contact_rel)>20:
            return render(request,'client_new.html',{"error_msg":"error information!"})
        email_pattern=r"[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.com"
        tel_pattern=r"[0-9]+"
        if re.match(email_pattern,contact_email) is None:
            return render(request,'client_new.html',{"error_msg":"error e-mail!"})
        if re.match(tel_pattern,contact_tel) is None or re.match(tel_pattern,client_tel) is None:
            return render(request,'client_edit.html',{"error_msg":"error phone number!"})
        edit_client(originalID,client_id,client_name,client_tel,client_add,contact_name,contact_tel,contact_email,contact_rel)
        return redirect("/index/client")

def account(request):
    if request.method=='GET':
        account_number=request.GET.get("account_number")
        print("account_number:",account_number)
        account_list=select_account(account_number)
        return render(request,'account.html',{"account_list":account_list})
    else:
        cheque_new_val=request.POST.get("cheque_new_button")
        saving_new_val=request.POST.get("saving_new_button")
        delete_val=request.POST.get("delete_button")
        if cheque_new_val is not None:
            return redirect("/index/account/cheque_new")
        if saving_new_val is not None:
            return redirect("/index/account/saving_new")
        if delete_val is not None:
            res=delete_account(delete_val)
            if res=='error!':
                return render(request,'account.html',{"error_msg":"error!"})
            else:
                return render(request,'account.html',{"error_msg":"deleted successfully!"})

def IsFloatNum(str):
    s=str.split('.')
    if len(s)>2:
        return False
    else:
        for si in s:
            if not si.isdigit():
                return False
        return True

def cheque_account_new(request):
    if request.method=="GET":
        return render(request,'cheque_account_new.html')
    else:
        account_number=request.POST.get("account_number")
        branch_name=request.POST.get("branch_name")
        account_balance=request.POST.get("account_balance")
        overdraft=request.POST.get("overdraft")
        client_id=request.POST.get("client_id")
        if account_number is None or branch_name is None or account_balance is None or overdraft is None or client_id is None:
            return render(request,'cheque_account_new.html',{"error_msg":"error information!"})
        if len(account_number)!=20 or len(client_id)!=18 or len(branch_name)>30:
            return render(request,'cheque_account_new.html',{"error_msg":"error information!"})
        if not account_balance.isdigit():
            return render(request,'cheque_account_new.html',{"error_msg":"error information!"})
        
        if insert_cheque_account(account_number,branch_name,account_balance,overdraft,client_id)=="error!":
            return render(request,'cheque_account_new.html',{"error_msg":"error information!"})
        else:
            return redirect("/index/account")

def saving_account_new(request):
    if request.method=="GET":
        return render(request,'saving_account_new.html')
    else:
        account_number=request.POST.get("account_number")
        branch_name=request.POST.get("branch_name")
        account_balance=request.POST.get("account_balance")
        interest_rate=request.POST.get("interest_rate")
        currency_type=request.POST.get("currency_type")
        client_id=request.POST.get("client_id")
        if account_number is None or branch_name is None or account_balance is None or interest_rate is None or currency_type is None or client_id is None:
            return render(request,'saving_account_new.html',{"error_msg":"error information!"})
        if len(account_number)!=20 or len(client_id)!=18 or len(branch_name)>30:
            return render(request,'saving_account_new.html',{"error_msg":"error information!"})
        if not account_balance.isdigit() or not IsFloatNum(interest_rate):
            return render(request,'saving_account_new.html',{"error_msg":"error balance or interest!"})

        if not (float(interest_rate)<1 and float(interest_rate)>0):
            return render(request,'saving_account_new.html',{"error_msg":"error interest!"})

        if insert_saving_account(account_number,branch_name,account_balance,interest_rate,currency_type,client_id)=="error!":
            return render(request,'saving_account_new.html',{"error_msg":"error information!"})
        else:
            return redirect("/index/account")

def account_detail(request):
    detail_val=request.POST.get("detail_button")
    if detail_val is not None:
        print(detail_val)
        account_info=search_detail_account(detail_val)
        print(account_info)
        account_info[2]=str(account_info[2])
        account_info[3]=str(account_info[3])
        account_info[4]=str(account_info[4])
        if len(account_info)==5:
            return render(request,'cheque_account_detail.html',{"account_info":account_info})
        else:
            return render(request,'saving_account_detail.html',{"account_info":account_info})

def account_edit(request):
    #TODO:
    return HttpResponse("Account")

def loan(request):
    if request.method=='GET':
        loan_id=request.GET.get("loan_id")
        loan_list=select_loan(loan_id)
        print("loan_id:",loan_id)
        print("loan list:",loan_list)
        if loan_list is None:
            loan_list=[]
        else:
            loan_list=[loan_list]
        return render(request,'loan.html',{"loan_list":loan_list})
    else:
        new_val=request.POST.get("new_button")
        delete_val=request.POST.get("delete_button")
        if new_val is not None:
            return redirect("/index/loan/new")
        if delete_val is not None:
            res=delete_loan(delete_val)
            if res=='error!':
                return render(request,'loan.html',{"error_msg":"delete error!"})
            else:
                return render(request,'loan.html',{"error_msg":"deleted successfully!"})

def pay_loan(request):
    #TODO:没有约束放款次数，没有约束放款金额
    if request.method=="GET":
        return render(request,'pay_loan.html')
    else:
        pay_id=request.POST.get("pay_id")
        loan_id=request.POST.get("loan_id")
        pay_money=request.POST.get("pay_money")
        if loan_id is None or pay_id is None or pay_money is None:
            return render(request,'pay_loan.html',{"error_msg":"blank information!"})
        if len(loan_id)!=20 or len(pay_id)!=20:
            return render(request,'pay_loan.html',{"error_msg":"error length!"})
        if not IsFloatNum(pay_money):
            return render(request,'pay_loan.html',{"error_msg":"error pay money!"})
        if insert_pay(pay_id,loan_id,pay_money)=="error!":
            return render(request,'pay_loan.html',{"error_msg":"error!"})
        else:
            return redirect("/index/loan")

def loan_new(request):
    if request.method=="GET":
        return render(request,'loan_new.html')
    else:
        loan_id=request.POST.get("loan_id")
        branch_name=request.POST.get("branch_name")
        loan_money=request.POST.get("loan_money")
        pay_cnt=request.POST.get("pay_cnt")
        client_id=request.POST.get("client_id")
        if loan_id is None or branch_name is None or loan_money is None or pay_cnt is None or client_id is None:
            return render(request,'loan_new.html',{"error_msg":"blank information!"})
        if len(loan_id)!=20:
            return render(request,'loan_new.html',{"error_msg":"error length!"})
        if not pay_cnt.isdigit() or not IsFloatNum(loan_money):
            return render(request,'loan_new.html',{"error_msg":"error number!"})
        if insert_loan(loan_id,branch_name,loan_money,pay_cnt,client_id)=="error!":
            return render(request,'loan_new.html',{"error_msg":"error!"})
        else:
            return redirect("/index/loan")

def business(request):
    return HttpResponse("Business")