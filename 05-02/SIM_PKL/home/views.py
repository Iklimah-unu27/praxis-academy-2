from django.shortcuts import render

def mahasiswa(req):
    return render(req, 'home/index.html')
def staf(req):
    return render(req, 'staf/index.html')
def dosen(req):
    return render(req, 'dosen/index.html')

