from django.shortcuts import render,redirect
from .models import *
from app_user.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'app_admin/index.html')

def log_in(request):
    return render(request,'app_admin/log_in.html')

def log_inaction(request):
    u_name=request.POST['user_name']
    p_word=request.POST['password']
    admin_check=admin_tb.objects.filter(user_name=u_name,password=p_word)
    user_check=register_tb.objects.filter(user_name=u_name,password=p_word)
    hobbies=hobby_name_tb.objects.all()
    seasons=season_tb.objects.all()
    age_factor=agefactor_tb.objects.all()
    if admin_check.count()>0:   
        messages.add_message(request,messages.INFO,"admin logged in successfully.")
        return render(request,'app_admin/admin_home.html',{'key':hobbies,'cat':seasons,'age':age_factor})
    elif user_check.count()>0:
        name=user_check[0].user_name
        request.session['yourself']=user_check[0].id 
        messages.add_message(request,messages.INFO,f"{u_name} logged in Successfully!!")
        return render(request,'app_user/user_home.html',{'key':hobbies,'cat':seasons,'you':name,'age':age_factor})
    else:
        messages.add_message(request,messages.INFO,'User Not Found, Please Register or Check your entry')
        return redirect('log_in')
def add_hobby(request):
    hobby_name=request.POST['hobby']
    hobby=hobby_name_tb(hobby_name=hobby_name)
    hobby.save()
    hobbies=hobby_name_tb.objects.all()
    seasons=season_tb.objects.all()
    # messages.add_message(request,messages.INFO,'hobby added to the database')
    return render(request,'app_admin/admin_home.html',{'key':hobbies,'cat':seasons})
def add_hobby_factor(request):
    factor_name=request.POST['factor_name']
    hobby_id=request.POST['id']
    factor=hobby_factor_tb(factor_name=factor_name,hobby_id_id=hobby_id)
    factor.save()
    hobbies=hobby_name_tb.objects.all()
    seasons=season_tb.objects.all()
    # messages.add_message(request,messages.INFO,'hobby factor added to the database')
    hobbies=hobby_name_tb.objects.all()
    return render(request,'app_admin/admin_home.html',{'key':hobbies,'cat':seasons})

def add_season(request):
    season_name=request.POST['season']
    season=season_tb(season_name=season_name)
    season.save()
    hobbies=hobby_name_tb.objects.all()
    seasons=season_tb.objects.all()
    # messages.add_message(request,messages.INFO,'season added to the database')
    return render(request,'app_admin/admin_home.html',{'key':hobbies,'cat':seasons})
def add_season_factor(request):
    factor_name=request.POST['factor_name']
    season_id=request.POST['id']
    factor=season_factor_tb(factor_name=factor_name,season_id_id=season_id)
    factor.save()
    # messages.add_message(request,messages.INFO,'season factor added to the database')
    seasons=season_tb.objects.all()
    return render(request,'app_admin/admin_home.html',{'cat':seasons})

def security_question(request):
    s_question=request.POST['security_question']
    add_sq=security_question_tb(question=s_question)
    add_sq.save()
    seasons=season_tb.objects.all()
    hobbies=hobby_name_tb.objects.all()
    return render(request,'app_admin/admin_home.html',{'cat':seasons,'key':hobbies})

def log_out(request):
    request.session.flush()
    return redirect('index')

def forgot(request):
    return render(request,'app_admin/forgot.html')

def recover_id(request):
    dob=request.POST['dob']
    mobile=request.POST['mobile']
    user_name=register_tb.objects.filter(dob=dob,phone=mobile)
    if user_name.count()>0:
        u_name=user_name[0].user_name
        messages.add_message(request,messages.INFO,f"Your user Name is :{u_name}")
        return redirect('log_in')
    else:
        messages.add_message(request,messages.INFO,"User not found in our database, check your entry")
        return redirect('forgot')
    
def start_password_reset(request):
    u_name=request.POST['user_name']
    dob=request.POST['dob']
    mobile=request.POST['mobile']
    check_user=register_tb.objects.filter(user_name=u_name,dob=dob,phone=mobile)
    
    if check_user.count()>0:
        mail=check_user[0].user_name
        return render(request,'app_admin/reset_password.html',{'key':mail})
    else:
        messages.add_message(request,messages.INFO,"User not found in our database, check your entry")
        return redirect('forgot')
    
def reset_password(request):
    user_name=request.POST['user_name']
    new_pass=request.POST['new_password']
    conf_pass=request.POST['confirm_password']
    if conf_pass==new_pass:
        register_tb.objects.filter(user_name=user_name).update(password=conf_pass)
        messages.add_message(request,messages.INFO,"Password Reset Successful.")
        return redirect('index')
    else:
        messages.add_message(request,messages.INFO,"Confirm password not matches with New password")
        return redirect('reset_password')

def add_age_factor(request):
    min_age=request.POST['min_age']
    max_age=request.POST['max_age']
    factor_name=request.POST['factor_name']
    hobbies=hobby_name_tb.objects.all()
    seasons=season_tb.objects.all()
    age_factor=agefactor_tb(min_age=min_age,max_age=max_age,factor_name=factor_name)
    age_factor.save()
    messages.add_message(request,messages.INFO,'Age Factor added successfully!')
    return render(request,'app_admin/admin_home.html',{'key':hobbies,'cat':seasons})