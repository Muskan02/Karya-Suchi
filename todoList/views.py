from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
	data=Todo.objects.all()
	return render(request, 'index.html', {'data' : data})

def index1(request):
	data=Todo.objects.all()
	return render(request, 'index.html', {'data' : data})

def add(request):
	if request.method=='POST':
		todo=request.POST['todo']
		if todo!="":
			todoItem=Todo(title=todo)
			todoItem.save()
			return redirect('index1')
		else:
			return redirect('index1')
	else:
		return redirect('index1')

def delete(request, todo_id):
	if request.method=='POST':
		item=Todo.objects.get(id=todo_id)
		item.delete()
		return redirect('index1')
	else:
		return redirect('index1')

def completed(request, todo_id):
	
	item=Todo.objects.get(id=todo_id)
	item.completed=True;
	item.save()
	return redirect('index1')
	


def notcompleted(request, todo_id):
	
	item=Todo.objects.get(id=todo_id)
	item.completed=False;
	item.save()
	return redirect('index1')
	
