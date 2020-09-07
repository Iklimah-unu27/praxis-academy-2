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

#################################################### Crud 2 ##################################################################


def pinjam(req):
    tasks = models.Pinjam.objects.all()
    return render(req, 'Pinjam/pinjam.html',{
        'data': tasks,
    })
    
def new2(req):
    if req.POST:
        models.Pinjam.objects.create(penulis=req.POST['penulis'], judul=req.POST['judul'], pnb=req.POST['pnb'], isbn=req.POST['isbn'], desc=req.POST['desc'])
        return redirect('/')

    tasks = models.Pinjam.objects.all()
    return render(req, 'pinjam/pinjam.html')

def detail2(req, id):
    task = models.Pinjam.objects.filter(pk=id).first()
    return render(req, 'pinjam/detail.html', {
        'data': task,
    })

def delete2(req, id):
    models.Pinjam.objects.filter(pk=id).delete()
    return redirect('/')

def update2(req, id):
    if req.POST:
        task = models.Pinjam.objects.filter(pk=id).update(nama=req.POST['nama'], nim=req.POST['nim'], judulbuku=req.POST['judulbuku'], tgl_masuk=req.POST['tgl_masuk'])
        return redirect('/')

    task = models.Pinjam.objects.filter(pk=id).first()
    return render(req, 'pinjam/update.html', {
        'data': task,
    })

