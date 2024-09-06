from django.urls import path
from . import views
urlpatterns = [
    path("",views.indexView,name="index"),
    path("createnewcustomer/",views.createNewCustomerView,name="createnewcustomer"),
    path("dashboard/",views.dashboardView,name="dashboard"),
    path("newaccount/",views.newAccountView,name="newaccount"),
    path("logout/",views.logoutView,name="logout"),
    path("myaccount/",views.MyAccountView,name="myaccount"),
    path("checkaccount/",views.CheckAccountView,name="checkaccount"),
    path("deposit/",views.depositView,name="deposit"),
    path("withdraw/",views.withdrawView,name="withdraw"),
    path("statment/",views.statmentView,name="statement"),
]