from django.shortcuts import render,redirect

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
	return render(request,'signup.html',{})