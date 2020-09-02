from django.shortcuts import render, redirect
from . import models

def index(req):
    tasks = models.Task.objects.all()
    return render(req, 'task/index.html',{
        'data': tasks,
    })

def new(req):
    if req.POST:
        models.Task.objects.create(penulis=req.POST['penulis'], judul=req.POST['judul'], pnb=req.POST['pnb'], isbn=req.POST['isbn'], desc=req.POST['desc'])
        return redirect('/')

    tasks = models.Task.objects.all()
    return render(req, 'task/new.html')

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')

def update(req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(penulis=req.POST['penulis'], judul=req.POST['judul'], pnb=req.POST['pnb'], isbn=req.POST['isbn'], desc=req.POST['desc'])
        return redirect('/')

    task = models.Task.objects.filter(pk=id).first()
    return render(req, 'task/update.html', {
        'data': task,
    })