from django.shortcuts import render

def index(req) :
    return render(req, "task/index.html",{
        'data' : [d +1 for d in range(7)],
    })
