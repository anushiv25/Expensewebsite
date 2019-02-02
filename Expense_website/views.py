from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import signup_form
from django.contrib.auth import authenticate,login,get_user_model,logout

User=get_user_model()

def index(request):
	return render(request,'index.html',{})

def about(request):
	return render(request,'about.html',{})

def contact(request):
	return render(request,'contact.html',{})

def Help(request):
	return render(request,'help.html',{})

def query(request):
	return render(request,'query.html',{})

def signin(request):
	return render(request,'signin.html',{})

def signup(request):
	form_class=signup_form(request.POST or None)
	context={
		"form":form_class
	}
	if form_class.is_valid():
		name=form_class.cleaned_data.get("name")
		email=form_class.cleaned_data.get("email")
		password=form_class.cleaned_data.get("password")
		new_user= User.objects.create_user(email,email,password)
		user_profile=profile(
				user=new_user,
				name=name,
			)
		user_profile.save()
		if new_user is not None:
			return redirect("/index")
	return render(request,'signup.html',context)