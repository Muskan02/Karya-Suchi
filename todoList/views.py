from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
	data=Todo.objects.all()
	return render(request, 'index.html', {'data' : data})

def add(request):
	if request.method=='POST':
		todo=request.POST['todo']
		if todo!="":
			todoItem=Todo(title=todo)
			todoItem.save()
			return render(request, 'index.html')
		else:
			return render(request, 'index.html')
	else:
		return render(request, 'index.html')

def delete(request, todo_id):
	if request.method=='POST':
		item=Todo.objects.get(id=todo_id)
		item.delete()
		return render(request, 'index.html')
	else:
		return render(request, 'index.html')

