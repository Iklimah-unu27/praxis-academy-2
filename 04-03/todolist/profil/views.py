from django.shortcuts import render

def index(req):
    return render(req, 'profil/index.html')
