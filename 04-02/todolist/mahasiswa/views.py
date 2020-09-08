from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    tasks = models.Mhs.objects.all()
    return render(req, 'mahasiswa/index.html',{
        'data': tasks,
    })

def new(req):
    form_input = forms.MhsForm()
    if req.POST:
        form_input = forms.MhsForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/mahasiswa/')
    return render(req, 'mahasiswa/new.html',{
        'form' : form_input,
    })

def detail(req, id):
    mhs = models.Mhs.objects.filter(pk=id).first()
    return render(req, 'mahasiswa/detail.html', {
        'data': mhs,
    })

def delete(req, id):
    models.Mhs.objects.filter(pk=id).delete()
    return redirect('/mahasiswa/')

def update(req, id):
    if req.POST:
        mhs = models.Mhs.objects.filter(pk=id).update(nama=req.POST['nama'], nim=req.POST['nim'], status=req.POST['status'], telp=req.POST['telp'], alamat=req.POST['alamat'])
        return redirect('/mahasiswa/')

    mhs = models.Mhs.objects.filter(pk=id).first()
    return render(req, 'mahasiswa/update.html', {
        'data': mhs,
    })