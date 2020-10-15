from django.shortcuts import render
from django.contrib.auth import get_user_model
from mahasiswa.models import Pkl
from mitra.models import Mitra

def index(req):
    group = req.user.groups.first()
    if group is not None and group.name == 'dosen':
        return render(req, 'dosen/index.html')
    elif group is not None and group.name == 'staf':
        return render(req, 'staf/index.html')
    else:
        return render(req, 'home/index.html')

# def byte_list(request):
#     byte= Byte.objects.count()
#     bytes = Byte.objects.order_by('text')
#     return render(request, 'cloudapp/byte_list.html', {'bytes': bytes,'byte':byte})
    # counts = models.Mitra.objects.count()
    
    # task = Mitra.objects.count()
    # tasks = Mitra.objects.order_by('nama_mitra')

    # return render(req, 'staf/index.html',{
    #     'tasks': tasks,
    #     'task' : task
    # })
def mitra_show(req, id=None):
    context = {}
    context['data'] = Mitra.objects.get(pk=id)
    return render(req, 'staf/index.html', context)

def mitra_show(req):
   return { 'total_user' : Mitra.objects.all().count() }