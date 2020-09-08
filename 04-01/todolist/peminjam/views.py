from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    tasks = models.Pinjam.objects.all()
    return render(req, 'pinjam/index.html',{
        'data': tasks,
    })
    
def new(req):
    form_input = forms.PinjamForm()

    if req.POST:
        form_input = forms.PinjamForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/peminjam/')
    return render(req, 'pinjam/new.html',{
        'form' : form_input,
    })

def detail(req, id):
    task = models.Pinjam.objects.filter(pk=id).first()
    return render(req, 'pinjam/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Pinjam.objects.filter(pk=id).delete()
    return redirect('/peminjam/')

def update(req, id):
    if req.POST:
        task = models.Pinjam.objects.filter(pk=id).update(nama=req.POST['nama'], nim=req.POST['nim'], judulbuku=req.POST['judulbuku'], tgl_masuk=req.POST['tgl_masuk'])
        return redirect('/peminjam/')

    task = models.Pinjam.objects.filter(pk=id).first()
    return render(req, 'pinjam/update.html', {
        'data': task,
    })

