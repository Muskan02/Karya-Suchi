from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Todo
from .models import theme

# Create your views here.


def index(request):
	message=None
	if 'message' in request.session:
		message=request.session.get('message')
	else:
		return render(request,'index.html')
	log_user=request.user
	data=Todo.objects.filter(user=log_user)
	t=theme.objects.all()
	return render(request, 'welcome.html', {'data' : data, 't' : t, 'message':message})

def signup(request):
	message=None
	if 'message' in request.session:
		message=request.session.get('message')
		log_user=request.user
		data=Todo.objects.filter(user=log_user)
		t=theme.objects.all()
		return render(request, 'welcome.html', {'data' : data, 't' : t, 'message':message})
	else:
		if request.method=='POST':
			error=[]
			username=request.POST['username']
			pass1=request.POST['pass1']

			if(User.objects.filter(username=username).exists()):
				error.append('Username is taken.')
				username=""
			elif(username==""):
				error.append('Username cannot be empty.')
				username=""
			elif(username.isalnum()==False):
				error.append('Username must contain only letters and alphabets.')
				username=""
			elif(len(username)<4 or len(username)>10):
				error.append('Username should conatin atleast 4 and atmost 10 characters.')
				username=""

			if(pass1==""):
				error.append('Password cannot be empty')
			elif(len(pass1)<4):
				error.append('Password should be atleast 4 characters long.')

			if(len(error)>0):
				return render(request, 'signup.html', {'warning':error})

				
			user=User.objects.create_user(username=username, password=pass1)
			user.save();
			return redirect('signin')
			
		else:
			return render(request, 'signup.html')
		


def signin(request):
	message=None
	if 'message' in request.session:
		message=request.session.get('message')
		log_user=request.user
		data=Todo.objects.filter(user=log_user)
		t=theme.objects.all()
		return render(request, 'welcome.html', {'data' : data, 't' : t, 'message':message})
	else:
		if request.method=='POST':
				username=request.POST['username']
				password=request.POST['password']
				error=[]

				user=auth.authenticate(username=username, password=password)

				if user is not None:
					auth.login(request,user)
					request.session['message']="{}".format(user.username)
					return  redirect('welcome')
				else:
					error.append('Invalid credentials.')
					return render(request,'signin.html',{'warning':error})
		else:
			return render(request, 'signin.html')


def signout(request):
	request.session['is_logged'] = False
	auth.logout(request)
	return render(request,'index.html')	

def welcome(request):
	message=None
	if 'message' in request.session:
		message=request.session.get('message')
		log_user=request.user
		data=Todo.objects.filter(user=log_user)
		t=theme.objects.all()
		return render(request, 'welcome.html', {'data' : data, 't' : t, 'message':message})
	else:
		if request.method!='POST':
			return render(request, 'signin.html')


def add(request):
	if request.method=='POST':
		todo=request.POST['todo']
		if todo!="":
			todoItem=Todo(title=todo, user=request.user)
			todoItem.save()
			return redirect('welcome')
		else:
			return redirect('welcome')
	else:
		return redirect('welcome')



def delete(request, todo_id):
	if request.method=='POST':
		item=Todo.objects.get(id=todo_id)
		item.delete()
		return redirect('welcome')
	else:
		return redirect('welcome')

def completed(request, todo_id):
	item=Todo.objects.get(id=todo_id)
	item.completed=True;
	item.save()
	return redirect('welcome')
	


def notcompleted(request, todo_id):
	item=Todo.objects.get(id=todo_id)
	item.completed=False;
	item.save()
	return redirect('welcome')

def lighttheme(request, tt_id):
	t=theme.objects.get(id=tt_id)
	t.light=True;
	t.save()
	return redirect('welcome')
	
	
def darktheme(request, tt_id):
	t=theme.objects.get(id=tt_id)
	t.light=False;
	t.save()
	return redirect('welcome')
	

	
