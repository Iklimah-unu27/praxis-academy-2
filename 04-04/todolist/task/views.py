from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    tasks = models.Task.objects.all()
    return render(req, 'task/index.html',{
        'data': tasks,
    })

def new(req):
    form_input = forms.TaskForm()
    if req.POST:
        form_input = forms.TaskForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/task/')
    return render(req, 'task/new.html',{
        'form' : form_input,
    })

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/task/')

def update(req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(penulis=req.POST['penulis'], judul=req.POST['judul'], pnb=req.POST['pnb'], isbn=req.POST['isbn'], desc=req.POST['desc'])
        return redirect('/task/')

    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/update.html', {
        'data': task,
    })