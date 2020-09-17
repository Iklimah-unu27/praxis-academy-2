from django.shortcuts import render

def index(req):
    return render(req, 'staf/index.html')
