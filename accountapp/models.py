from django.db.models import *
from django.core.validators import *
# Create your models here.

class CustomerModel(Model):
    id=AutoField(primary_key=True)
    name=CharField(max_length=100,validators=[RegexValidator(regex=r"^[a-zA-Z\s]+$",message="Name must contain chars...")])
    email=EmailField(max_length=100)
    mobile=CharField(max_length=10,validators=[RegexValidator(regex=r"^[0-9]{10}$",message="Mobile Number Must contain 10 digits")])
    gender=CharField(max_length=100)
    birthdate=DateField()
    address=TextField()
    def __str__(self):
        return self.name

class CustomerLoginModel(Model):
    id=AutoField(primary_key=True)
    customer_id=ForeignKey(CustomerModel,CASCADE)
    email=EmailField()
    password=CharField(max_length=200)
    last_login=DateField(auto_now=True)

class AccountModel(Model):
    id=AutoField(primary_key=True)
    accno=BigIntegerField(default=0)
    balance=FloatField(default=0)
    account_type=CharField(max_length=100)
    customer_id=ForeignKey(CustomerModel,CASCADE)
    account_owner=CharField(max_length=100)
    account_status=BooleanField(default=False)

    def depositAmount(self,amount):
        self.balance=self.balance+float(amount)
        self.save()
        
    def withdrawAmount(self,amount):
        if self.balance>=float(amount):
            self.balance=self.balance-float(amount)
            self.save()
            return True
        else:
            return False

    @classmethod
    def getCustomerAccounts(cls,id):
        queryset=cls.objects.filter(customer_id=id)
        return queryset
    @classmethod
    def getCustomerActiveAccounts(cls,id):
        queryset=cls.objects.filter(customer_id=id,account_status=True)
        return queryset
    

class StatmentModel(Model):
    id=AutoField(primary_key=True)
    account=ForeignKey(AccountModel,CASCADE)
    opration=CharField(max_length=200)
    amount=FloatField()
    date=DateField(auto_now=True)
    time=TimeField(auto_now=True)