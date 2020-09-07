from django.shortcuts import render, redirect
from . import models

def pinjam(req):
    tasks = models.Pinjam.objects.all()
    return render(req, 'Pinjam/pinjam.html',{
        'data': tasks,
    })
    
def new(req):
    if req.POST:
        models.Pinjam.objects.create(penulis=req.POST['penulis'], judul=req.POST['judul'], pnb=req.POST['pnb'], isbn=req.POST['isbn'], desc=req.POST['desc'])
        return redirect('/')

    tasks = models.Pinjam.objects.all()
    return render(req, 'pinjam/pinjam.html')

def detail(req, id):
    task = models.Pinjam.objects.filter(pk=id).first()
    return render(req, 'pinjam/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Pinjam.objects.filter(pk=id).delete()
    return redirect('/')

def update(req, id):
    if req.POST:
        task = models.Pinjam.objects.filter(pk=id).update(nama=req.POST['nama'], nim=req.POST['nim'], judulbuku=req.POST['judulbuku'], tgl_masuk=req.POST['tgl_masuk'])
        return redirect('/')

    task = models.Pinjam.objects.filter(pk=id).first()
    return render(req, 'pinjam/update.html', {
        'data': task,
    })

