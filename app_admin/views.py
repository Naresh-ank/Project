from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Login, Home_Policy, Life_Policy, Health_Policy, Car_Policy
from app_user.models import User_Registration,Take_Insurance,Pay_Premium


def loginCheck(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    usertype = request.POST.get('usertype')

    qs = Login.objects.filter(username=username, password=password)
    if qs:
        if usertype == 'Admin':
            return render(request, 'admin/admin_home.html')
        elif usertype == "Official":
            return render(request, 'official/official_home.html')
        else:
            request.session['username'] = username
            return render(request, 'User/user_home.html')

    else:
        if usertype == "Admin":
            messages.error(request, "Invalid Admin")
            return redirect('admin_login')
        elif usertype == "Official":
            messages.error(request, "Invalid Official")
            return redirect('official_login')
        else:
            messages.error(request, "Invalid User")
            return redirect('user_login')


def addHomePolicy(request):
    policy_type = request.POST.get('policy_type')
    # policy_id = request.POST.get('policy_id')
    policy_name = request.POST.get('policy_name')
    description = request.POST.get('description')
    time_duration = request.POST.get('time_duration')
    amount = request.POST.get('amount')
    premium_amount = request.POST.get('premium_amount')
    premium_number = request.POST.get('premium_number')
    rate_of_interest = request.POST.get('rate_of_interest')
    rules = request.POST.get('rules')
    beneficial_amount = request.POST.get('beneficial_amount')
    property_cost = request.POST.get('property_cost')

    Home_Policy(policy_type=policy_type,policy_name=policy_name,description=description,time_duration=time_duration,amount=amount,premium_amount=premium_amount,premium_number=premium_number,rate_of_interest=rate_of_interest,rules=rules,benificial_amount=beneficial_amount,property_cost=property_cost).save()
    messages.error(request, "Home Policy Added")
    return redirect('home_policy')


def addLifePolicy(request):
    policy_type = request.POST.get('policy_type')
    # policy_id = request.POST.get('policy_id')
    policy_name = request.POST.get('policy_name')
    description = request.POST.get('description')
    time_duration = request.POST.get('time_duration')
    amount = request.POST.get('amount')
    premium_amount = request.POST.get('premium_amount')
    premium_number = request.POST.get('premium_number')
    rate_of_interest = request.POST.get('rate_of_interest')
    rules = request.POST.get('rules')
    beneficial_amount = request.POST.get('beneficial_amount')
    accidental_benefit = request.POST.get('accidental_benefit')

    Life_Policy(policy_type=policy_type,policy_name=policy_name, description=description, time_duration=time_duration,
                amount=amount, premium_amount=premium_amount, premium_number=premium_number,
                rate_of_interest=rate_of_interest, rules=rules, benificial_amount=beneficial_amount,
                accidential_benifit=accidental_benefit).save()
    messages.error(request, "Life Policy Added")
    return redirect('life_policy')


def addHealthPolicy(request):
    policy_type = request.POST.get('policy_type')
    # policy_id = request.POST.get('policy_id')
    policy_name = request.POST.get('policy_name')
    description = request.POST.get('description')
    time_duration = request.POST.get('time_duration')
    amount = request.POST.get('amount')
    premium_amount = request.POST.get('premium_amount')
    premium_number = request.POST.get('premium_number')
    coverage_amount = request.POST.get('coverage_amount')
    marital_status = request.POST.get('marital_status')
    number_of_family = request.POST.get('number_of_family')

    Health_Policy(policy_type=policy_type,  policy_name=policy_name,description=description, time_duration=time_duration,
                amount=amount, premium_amount=premium_amount, premium_number=premium_number,
                coverage_amount=coverage_amount,marital_status=marital_status,no_of_family=number_of_family).save()
    messages.error(request, "Health Policy Added")
    return redirect('health_policy')


def addCarPolicy(request):
    policy_type = request.POST.get('policy_type')
    # policy_id = request.POST.get('policy_id')
    policy_name = request.POST.get('policy_name')
    description = request.POST.get('description')
    time_duration = request.POST.get('time_duration')
    amount = request.POST.get('amount')
    premium_amount = request.POST.get('premium_amount')
    premium_number = request.POST.get('premium_number')
    rate_of_interest = request.POST.get('rate_of_interest')
    rules = request.POST.get('rules')
    beneficial_amount = request.POST.get('beneficial_amount')
    type = request.POST.get('type')
    vehicle_no = request.POST.get('vehicle_no')
    company = request.POST.get('company')
    model = request.POST.get('model')

    Car_Policy(policy_type=policy_type,policy_name=policy_name, description=description, time_duration=time_duration,
                amount=amount, premium_amount=premium_amount, premium_number=premium_number,
                rate_of_interest=rate_of_interest, rules=rules, benificial_amount=beneficial_amount,
                type=type,vehicle_no=vehicle_no,company=company,model=model).save()
    messages.error(request, "Car Policy Added")
    return redirect('car_policy')


def deleteHomePolicy(request):
    policy_name = request.GET.get('policy_name')
    Home_Policy.objects.filter(policy_name=policy_name).delete()
    qs = Home_Policy.objects.all()
    return render(request,'admin/admin_view_home_policy.html',{'object_list':qs})


def updateHomePolicy(request):
    policy_name = request.GET.get('policy_name')
    qs = Home_Policy.objects.filter(policy_name=policy_name)
    return render(request,'admin/update_home_policy.html',{'home_data':qs})


def saveHomeUpdate(request):
    policy_type = request.POST.get('policy_type')
    # policy_id = request.POST.get('policy_id')
    policy_name = request.POST.get('policy_name')
    description = request.POST.get('description')
    time_duration = request.POST.get('time_duration')
    amount = request.POST.get('amount')
    premium_amount = request.POST.get('premium_amount')
    premium_number = request.POST.get('premium_number')
    rate_of_interest = request.POST.get('rate_of_interest')
    rules = request.POST.get('rules')
    beneficial_amount = request.POST.get('beneficial_amount')
    property_cost = request.POST.get('property_cost')

    Home_Policy(policy_type=policy_type,  policy_name=policy_name, description=description,
                time_duration=time_duration, amount=amount, premium_amount=premium_amount,
                premium_number=premium_number, rate_of_interest=rate_of_interest, rules=rules,
                benificial_amount=beneficial_amount, property_cost=property_cost).save()

    return redirect('admin_home_policy')


def updateLifePolicy(request):
    policy_name = request.GET.get('policy_name')
    qs = Life_Policy.objects.filter(policy_name=policy_name)
    return render(request, 'admin/update_life_policy.html', {'life_data': qs})


def saveLifeUpdate(request):
    policy_type = request.POST.get('policy_type')
    # policy_id = request.POST.get('policy_id')
    policy_name = request.POST.get('policy_name')
    description = request.POST.get('description')
    time_duration = request.POST.get('time_duration')
    amount = request.POST.get('amount')
    premium_amount = request.POST.get('premium_amount')
    premium_number = request.POST.get('premium_number')
    rate_of_interest = request.POST.get('rate_of_interest')
    rules = request.POST.get('rules')
    beneficial_amount = request.POST.get('beneficial_amount')
    accidental_benefit = request.POST.get('accidental_benefit')

    Life_Policy(policy_type=policy_type,policy_name=policy_name, description=description, time_duration=time_duration,
                amount=amount, premium_amount=premium_amount, premium_number=premium_number,
                rate_of_interest=rate_of_interest, rules=rules, benificial_amount=beneficial_amount,
                accidential_benifit=accidental_benefit).save()
    return redirect('admin_life_policy')


def deleteLifePolicy(request):
    policy_name = request.GET.get('policy_name')
    Life_Policy.objects.filter(policy_name=policy_name).delete()
    qs = Life_Policy.objects.all()
    return render(request, 'admin/admin_view_life_policy.html', {'object_list': qs})


def updateHealthPolicy(request):
    policy_name = request.GET.get('policy_name')
    qs = Health_Policy.objects.filter(policy_name=policy_name)
    return render(request, 'admin/update_health_policy.html', {'health_data': qs})


def saveHealthUpdate(request):
    policy_type = request.POST.get('policy_type')
    # policy_id = request.POST.get('policy_id')
    policy_name = request.POST.get('policy_name')
    description = request.POST.get('description')
    time_duration = request.POST.get('time_duration')
    amount = request.POST.get('amount')
    premium_amount = request.POST.get('premium_amount')
    premium_number = request.POST.get('premium_number')
    coverage_amount = request.POST.get('coverage_amount')
    marital_status = request.POST.get('marital_status')
    number_of_family = request.POST.get('number_of_family')

    Health_Policy(policy_type=policy_type, policy_name=policy_name, description=description,
                  time_duration=time_duration,
                  amount=amount, premium_amount=premium_amount, premium_number=premium_number,
                  coverage_amount=coverage_amount, marital_status=marital_status, no_of_family=number_of_family).save()
    messages.error(request, "Health Policy Added")
    return redirect('admin_health_policy')


def deleteHealthPolicy(request):
    policy_name = request.GET.get('policy_name')
    Health_Policy.objects.filter(policy_name=policy_name).delete()
    qs = Health_Policy.objects.all()
    return render(request, 'admin/admin_view_health_policy.html', {'object_list': qs})


def updateCarPolicy(request):
    policy_name = request.GET.get('policy_name')
    qs = Car_Policy.objects.filter(policy_name=policy_name)
    return render(request, 'admin/update_car_policy.html', {'car_data': qs})


def saveCarUpdate(request):
    policy_type = request.POST.get('policy_type')
    # policy_id = request.POST.get('policy_id')
    policy_name = request.POST.get('policy_name')
    description = request.POST.get('description')
    time_duration = request.POST.get('time_duration')
    amount = request.POST.get('amount')
    premium_amount = request.POST.get('premium_amount')
    premium_number = request.POST.get('premium_number')
    rate_of_interest = request.POST.get('rate_of_interest')
    rules = request.POST.get('rules')
    beneficial_amount = request.POST.get('beneficial_amount')
    type = request.POST.get('type')
    vehicle_no = request.POST.get('vehicle_no')
    company = request.POST.get('company')
    model = request.POST.get('model')

    Car_Policy(policy_type=policy_type,policy_name=policy_name, description=description, time_duration=time_duration,
               amount=amount, premium_amount=premium_amount, premium_number=premium_number,
               rate_of_interest=rate_of_interest, rules=rules, benificial_amount=beneficial_amount,
               type=type, vehicle_no=vehicle_no, company=company, model=model).save()
    return redirect('admin_car_policy')


def deleteCarPolicy(request):
    policy_name = request.GET.get('policy_name')
    Car_Policy.objects.filter(policy_name=policy_name).delete()
    qs = Car_Policy.objects.all()
    return render(request, 'admin/admin_view_car_policy.html', {'object_list': qs})


def saveDetails(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    address = request.POST.get('address')
    contact = request.POST.get('contact')
    date_of_birth = request.POST.get('date_of_birth')
    nominee = request.POST.get('nominee')

    Login(username=username,password=password,usertype='User').save()
    User_Registration(username=username,password=password,address=address,contact=contact,date_of_birth=date_of_birth,nominee=nominee).save()
    messages.error(request,"User Registered Successfully")
    return redirect('user_login')


def policyLogin(request):
    policy_type = request.POST.get('policy_type')
    request.session['policy_type'] = policy_type
    if policy_type == 'Home':
        qs = Home_Policy.objects.all()
        def home():
            l = []
            for x in qs:
                l.append(x.policy_name)
            return l
        policy_name = home()

    elif policy_type == 'Life':
        qs = Life_Policy.objects.all()
        def life():
            l = []
            for x in qs:
                l.append(x.policy_name)
            return l
        policy_name = life()

    elif policy_type == 'Health':
        qs = Health_Policy.objects.all()
        def health():
            l = []
            for x in qs:
                l.append(x.policy_name)
            return l
        policy_name = health()

    else:
        qs = Car_Policy.objects.all()
        def car():
            l = []
            for x in qs:
                l.append(x.policy_name)
            return l
        policy_name = car()

    return render(request,'User/select_policy_name.html',{'policy_name':policy_name})


def selectPolicyName(request):
    policy_name = request.POST.get('policy_name')
    policy_type = request.session['policy_type']
    if policy_type == 'Home':
        qs = Home_Policy.objects.filter(policy_name=policy_name)
        print(qs)

    elif policy_type == 'Life':
        qs = Life_Policy.objects.filter(policy_name=policy_name)

    elif policy_type == 'Health':
        qs = Health_Policy.objects.filter(policy_name=policy_name)

    else:
        qs = Car_Policy.objects.filter(policy_name=policy_name)

    return render(request,'User/previous_policy.html',{'qs':qs})

def autoGenerateId():
    qs = Take_Insurance.objects.all()
    if qs:
        return qs[len(qs)-1].id+1
    else:
        idno = 101
        return idno


def applyPolicy(request):
    name = request.POST.get('name')
    policy_type = request.POST.get('policy_type')
    policy_name = request.POST.get('policy_name')
    date_of_birth = request.POST.get('date_of_birth')
    policy_duration = request.POST.get('policy_duration')
    policy_taking_date = request.POST.get('policy_taking_date')
    premium_amount = request.POST.get('premium_amount')
    beneficial_amount = request.POST.get('beneficial_amount')
    description = request.POST.get('description')

    idno = autoGenerateId()
    Take_Insurance(id=idno,name=name,policy_type=policy_type,policy_name=policy_name,date_of_birth=date_of_birth,policy_duration=policy_duration,policy_taking_date=policy_taking_date,premium_amount=premium_amount,benificial_amount=beneficial_amount,description=description).save()

    return render(request,'User/policy_applied.html',{'idno':idno})


def viewPolicyDetails(request):
    policy_holder_name = request.POST.get('policy_holder_name')
    policy_id = request.POST.get('policy_id')

    qs = Take_Insurance.objects.filter(name=policy_holder_name,id=policy_id)
    if qs:
        qs1 = Take_Insurance.objects.filter(name=policy_holder_name)
        return render(request, 'User/view_policy_details.html',{'qs1':qs1})
    else:
        return render(request,'User/policy_details.html',{'message':'Invalid Details'})


def viewPremiumAmount(request):
    username = request.session['username']
    qs = Take_Insurance.objects.filter(name=username)
    return render(request,'User/view_premium_amount.html',{'qs':qs})


def payPremium(request):
    policy_holder_name = request.POST.get('policy_holder_name')
    policy_payment_date = request.POST.get('policy_payment_date')
    premium_amount = request.POST.get('premium_amount')
    paid_amount = request.POST.get('paid_amount')
    policy_number = request.POST.get('policy_number')
    dd_no = request.POST.get('dd_no')

    Pay_Premium(policy_holder_name=policy_holder_name,policy_payment_date=policy_payment_date,premium_amount=premium_amount,paid_amount=paid_amount,policy_number=policy_number,dd_no=dd_no).save()
    return render(request,'paid.html')