from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    tasks = models.Mitra.objects.all()
    form_input = forms.MitraForm()

    if req.POST:
        form_input = forms.MitraForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mitra/')

    return render(req, 'mitra/index.html',{
        'data': tasks,
        'form' : form_input,
    })

def index_staf(req):
    tasks = models.Mitra.objects.all()
    form_input = forms.MitraForm()

    if req.POST:
        form_input = forms.MitraForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mitras/')

    return render(req, 'mitras/index.html',{
        'data': tasks,
        'form' : form_input,
    })


def new(req):
    form_input = forms.MitraForm()

    if req.POST:
        form_input = forms.MitraForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mitra/')
    return render(req, 'mitra/new.html',{
        'form' : form_input,
    })

def new_staf(req):
    form_input = forms.MitraForm()

    if req.POST:
        form_input = forms.MitraForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mitras/')
    return render(req, 'mitras/new.html',{
        'form' : form_input,
    })


def detail(req, id):
    mitra = models.Mitra.objects.filter(pk=id).first()
    return render(req, 'mitra/detail.html', {
        'data': mitra,
    })

def detail_staf(req, id):
    mitra = models.Mitra.objects.filter(pk=id).first()
    return render(req, 'mitras/detail.html', {
        'data': mitra,
    })


def delete(req, id):
    models.Mitra.objects.filter(pk=id).delete()
    return redirect('/mitra/')

def delete_staf(req, id):
    models.Mitra.objects.filter(pk=id).delete()
    return redirect('/mitras/')

def update(req, id):
    if req.POST:
        mitra = models.Mitra.objects.filter(pk=id).update(nama_mitra=req.POST['nama_mitra'], alamat=req.POST['alamat'], deskripsi=req.POST['deskripsi'], pic=req.POST['pic'], telp=req.POST['telp'])
        return redirect('/mitra/')

    mitra = models.Mitra.objects.filter(pk=id).first()
    return render(req, 'mitra/update.html', {
        'data': mitra,
    })

def update_staf(req, id):
    if req.POST:
        mitra = models.Mitra.objects.filter(pk=id).update(nama_mitra=req.POST['nama_mitra'], alamat=req.POST['alamat'], deskripsi=req.POST['deskripsi'], pic=req.POST['pic'], telp=req.POST['telp'])
        return redirect('/mitras/')

    mitra = models.Mitra.objects.filter(pk=id).first()
    return render(req, 'mitras/update.html', {
        'data': mitra,
    })