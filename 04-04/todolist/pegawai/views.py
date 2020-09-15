from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    pegawai = models.Pegawai.objects.all()
    return render(req, 'pegawai/index.html',{
        'data': pegawai,
    })

def new(req):
    form_input = forms.PegawaiForm()
    if req.POST:
        form_input = forms.PegawaiForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/pegawai/')
    return render(req, 'pegawai/new.html',{
        'form' : form_input,
    })

def detail(req, id):
    pegawai = models.Pegawai.objects.filter(pk=id).first()
    return render(req, 'pegawai/detail.html', {
        'data': pegawai,
    })

def delete(req, id):
    models.Pegawai.objects.filter(pk=id).delete()
    return redirect('/pegawai/')

def update(req, id):
    if req.POST:
        pegawai = models.Pegawai.objects.filter(pk=id).update(nama=req.POST['nama'], telp=req.POST['telp'], alamat=req.POST['alamat'], isbn=req.POST['isbn'], desc=req.POST['desc'])
        return redirect('/pegawai/')

    pegawai = models.Pegawai.objects.filter(pk=id).first()
    return render(req, 'pegawai/update.html', {
        'data': pegawai,
    })