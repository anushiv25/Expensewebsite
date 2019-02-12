from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
def data(request):
	return render(request,'data.html',{})
def common(request):
	return render(request,'common.html',{})

def signup(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['password1']:
			try:
				user=User.objects.get(username=request.POST['name'])
				return render(request,'signup.html',{'error':'Username is taken'})
			except User.DoesNotExist:
				user=User.objects.create_user(request.POST['name'], email=request.POST['email'], password=request.POST['password'])
				auth.login(request, user)
				return redirect('/index')
		else:	
			return render(request,'signup.html',{'error':'Password does not Matched'})	
	else:	
		return render(request,'signup.html',{})