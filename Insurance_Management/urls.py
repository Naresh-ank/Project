"""Insurance_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView

from app_admin import views
from app_admin.models import Home_Policy, Life_Policy, Health_Policy, Car_Policy
from app_user.models import Take_Insurance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name='home/index.html'),name='index'),
    path('admin_login/',TemplateView.as_view(template_name='admin/admin_login.html'),name='admin_login'),
    path('official_login/',TemplateView.as_view(template_name='official/official_login.html'),name='official_login'),
    path('official_home/',TemplateView.as_view(template_name='official/official_home.html'),name='official_home'),
    path('admin_home/',TemplateView.as_view(template_name='admin/admin_home.html'),name='admin_home'),
    path('login_check/',views.loginCheck,name='login_check'),
    path('home_policy/',TemplateView.as_view(template_name='official/add_home_policy.html'),name='home_policy'),
    path('life_policy/',TemplateView.as_view(template_name='official/add_life_policy.html'),name='life_policy'),
    path('health_policy/',TemplateView.as_view(template_name='official/add_health_policy.html'),name='health_policy'),
    path('car_policy/',TemplateView.as_view(template_name='official/add_car_policy.html'),name='car_policy'),
    path('add_home_policy/',views.addHomePolicy,name='add_home_policy'),
    path('add_life_policy/',views.addLifePolicy,name='add_life_policy'),
    path('add_health_policy/',views.addHealthPolicy,name='add_health_policy'),
    path('add_car_policy/',views.addCarPolicy,name='add_car_policy'),
    path('admin_home_policy/',ListView.as_view(template_name='admin/admin_view_home_policy.html',model=Home_Policy,queryset=Home_Policy.objects.all()),name='admin_home_policy'),
    path('admin_life_policy/',ListView.as_view(template_name='admin/admin_view_life_policy.html',model=Life_Policy,queryset=Life_Policy.objects.all()),name='admin_life_policy'),
    path('admin_health_policy/',ListView.as_view(template_name='admin/admin_view_health_policy.html',model=Health_Policy,queryset=Health_Policy.objects.all()),name='admin_health_policy'),
    path('admin_car_policy/',ListView.as_view(template_name='admin/admin_view_car_policy.html',model=Car_Policy,queryset=Car_Policy.objects.all()),name='admin_car_policy'),
    path('delete_home_policy/',views.deleteHomePolicy,name='delete_home_policy'),
    path('delete_life_policy/',views.deleteLifePolicy,name='delete_life_policy'),
    path('delete_health_policy/',views.deleteHealthPolicy,name='delete_health_policy'),
    path('delete_car_policy/',views.deleteCarPolicy,name='delete_car_policy'),
    path('update_home_policy/',views.updateHomePolicy,name='update_home_policy'),
    path('update_life_policy/',views.updateLifePolicy,name='update_life_policy'),
    path('update_health_policy/',views.updateHealthPolicy,name='update_health_policy'),
    path('update_car_policy/',views.updateCarPolicy,name='update_car_policy'),
    path('save_home_update/',views.saveHomeUpdate,name='save_home_update'),
    path('save_life_update/',views.saveLifeUpdate,name='save_life_update'),
    path('save_health_update/',views.saveHealthUpdate,name='save_health_update'),
    path('save_car_update/',views.saveCarUpdate,name='save_car_update'),

    path('user_login/',TemplateView.as_view(template_name='User/user_login.html'),name='user_login'),
    path('user_register/',TemplateView.as_view(template_name='User/user_register.html'),name='user_register'),
    path('save_details/',views.saveDetails,name='save_details'),
    path('user_home/',TemplateView.as_view(template_name='User/user_home.html'),name='user_home'),
    path('take_insurance_home/',TemplateView.as_view(template_name='User/take_insurance_home.html'),name='take_insurance_home'),
    path('policy_login/',views.policyLogin,name='policy_login'),
    path('select_policy_name/',views.selectPolicyName,name='select_policy_name'),
    path('apply_policy/',views.applyPolicy,name='apply_policy'),
    path('policy_details/',TemplateView.as_view(template_name='User/policy_details.html'),name='policy_details'),
    path('view_policy_details/',views.viewPolicyDetails,name='view_policy_details'),
    path('view_premium_amount/',views.viewPremiumAmount,name='view_premium_amount'),
    path('pay_premium/',TemplateView.as_view(template_name='User/pay_premium.html'),name='pay_premium'),
    path('pay/',views.payPremium,name='pay')
]
