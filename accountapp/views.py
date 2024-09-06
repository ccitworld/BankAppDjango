from django.shortcuts import render,redirect
from django.contrib import messages
from . import forms
from . import models
# Create your views here.

def indexView(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        Customer=models.CustomerLoginModel.objects.filter(email=email,password=password).count()
        if Customer>0:
            customer_id=models.CustomerModel.objects.get(email=email).id
            request.session['customer_id']=customer_id
            request.session['email']=email
            return redirect("dashboard/")
        else:
            messages.error(request,"Email/Password is Invaild")        
    LoginForm=forms.CustomerLoginForm()
    return render(request,"index.html",{'LoginForm':LoginForm})

def createNewCustomerView(request):
    if request.method=="POST":
        NewCustomerForm=forms.CustomerForm(request.POST)
        if  NewCustomerForm.is_valid():
            messages.success(request,"New Customer is created...")
            Customer=NewCustomerForm.save()
            email=request.POST['email']
            password=request.POST['password']
            models.CustomerLoginModel.objects.create(email=email,password=password,customer_id=Customer)
        else:
            return render(request,"createNewCustomer.html",{"NewCustomerForm":NewCustomerForm})             
    NewCustomerForm=forms.CustomerForm()
    return render(request,"createNewCustomer.html",{"NewCustomerForm":NewCustomerForm})

def dashboardView(request):
    return render(request,"dashboard.html")

def newAccountView(request):
    if request.method=="POST":
        account_type=request.POST['account_type']
        account_owner=request.POST['account_owner']
        customer=models.CustomerModel.objects.get(email=request.session['email'])
        LastAccountId=models.AccountModel.objects.last().id
        id=customer.id
        accountno="10202024"+str(id).rjust(4,"0")+str(LastAccountId+1).rjust(4,"0")
        models.AccountModel.objects.create(accno=accountno,account_type=account_type,
                                           account_owner=account_owner,customer_id=customer)
    NewAccountForm=forms.NewAccountForm()
    return render(request,"newaccount.html",{"NewAccountForm":NewAccountForm})

def logoutView(request):
    request.session.clear()
    return redirect("index")

def MyAccountView(request):
    accountList=models.AccountModel.getCustomerAccounts(request.session['customer_id'])
    return render(request,"myaccount.html",{'accountList':accountList})

def CheckAccountView(request):
    accountActiveList=models.AccountModel.getCustomerActiveAccounts(request.session['customer_id'])
    if request.method=="POST":
        accno=request.POST['accno']
        account=models.AccountModel.objects.get(accno=accno)
        return render(request,"checkaccount.html",{"accountActiveList":accountActiveList,"account":account})
    return render(request,"checkaccount.html",{"accountActiveList":accountActiveList})

def depositView(request):
    if request.method=="POST":
        accno=request.POST['accno']
        amount=request.POST['amount']
        account=models.AccountModel.objects.get(accno=accno)
        account.depositAmount(amount)
        models.StatmentModel.objects.create(account=account,opration="Deposit",amount=amount)
        messages.success(request,"Amount Deposited successfully...")
    accountActiveList=models.AccountModel.getCustomerActiveAccounts(request.session['customer_id'])
    return render(request,"deposit.html",{"accountActiveList":accountActiveList})

def withdrawView(request):
    if request.method=="POST":
        accno=request.POST['accno']
        amount=request.POST['amount']
        account=models.AccountModel.objects.get(accno=accno)
        if account.withdrawAmount(amount):
            models.StatmentModel.objects.create(account=account,opration="Withdraw",amount=amount)
            messages.success(request,"Amount Withdraw successfully...")
        else:
            messages.warning(request,"Insufficient balance....")
    accountActiveList=models.AccountModel.getCustomerActiveAccounts(request.session['customer_id'])
    return render(request,"withdraw.html",{"accountActiveList":accountActiveList})

def statmentView(request):
    accountActiveList=models.AccountModel.getCustomerActiveAccounts(request.session['customer_id'])
    if request.method=="POST":
        accno=request.POST['accno']
        account=models.AccountModel.objects.get(accno=accno)
        statements=models.StatmentModel.objects.filter(account=account.id)
        return render(request,"statement.html",{"accountActiveList":accountActiveList,"statements":statements})
    return render(request,"statement.html",{"accountActiveList":accountActiveList})