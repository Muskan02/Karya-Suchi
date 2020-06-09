from django.shortcuts import render, redirect
from .models import Todo
from .models import theme

# Create your views here.

def index(request):
	data=Todo.objects.all()
	t=theme.objects.all()
	return render(request, 'index.html', {'data' : data, 't' : t})

def index1(request):
	data=Todo.objects.all()
	return render(request, 'index.html', {'data' : data})

def add(request):
	if request.method=='POST':
		todo=request.POST['todo']
		if todo!="":
			todoItem=Todo(title=todo)
			todoItem.save()
			return redirect('index')
		else:
			return redirect('index')
	else:
		return redirect('index')

def addtheme(request):
	if request.method=='POST':
		t=request.POST['theme']
		if t!="":
			tItem=theme(light=t)
			tItem.save()
			return redirect('index')
		else:
			return redirect('index')
	else:
		return redirect('index')

def delete(request, todo_id):
	if request.method=='POST':
		item=Todo.objects.get(id=todo_id)
		item.delete()
		return redirect('index')
	else:
		return redirect('index')

def completed(request, todo_id):
	item=Todo.objects.get(id=todo_id)
	item.completed=True;
	item.save()
	return redirect('index')
	


def notcompleted(request, todo_id):
	item=Todo.objects.get(id=todo_id)
	item.completed=False;
	item.save()
	return redirect('index')

def lighttheme(request, tt_id):
	t=theme.objects.get(id=tt_id)
	t.light=True;
	t.save()
	return redirect('index')
	
	
def darktheme(request, tt_id):
	t=theme.objects.get(id=tt_id)
	t.light=False;
	t.save()
	return redirect('index')
	

	
